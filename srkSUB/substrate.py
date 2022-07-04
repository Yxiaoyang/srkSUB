#!/usr/bin/python3
# https://github.com/polkascan/py-substrate-interface
from substrateinterface import *
from scalecodec.type_registry import load_type_registry_file, SUPPORTED_TYPE_REGISTRY_PRESETS
import sys


def main():
    crust = {
        # https: // github.com / crustio / crust.js / blob / mainnet / packages / type - definitions / src / json / types.json
        'url': "wss://rpc-crust-mainnet.decoo.io/",
        'ss58_format': 66,
        'type_registry_file': 'cru.json',
        'type_registry_preset': 'substrate-node-template',
        'type_registry': None
    }

    polkadot = {
        'url': "wss://rpc.polkadot.io",
        'ss58_format': 0,
        'type_registry_file': None,
        'type_registry_preset': 'polkadot',
        'type_registry': None
    }
    kusama = {
        'url': "wss://kusama-rpc.polkadot.io/",
        'ss58_format': 2,
        'type_registry_file': None,
        'type_registry_preset': 'kusama',
        'type_registry': None
    }

    chainConf = {
        'crust': crust,
        'polkadot': polkadot,
        'kusama': kusama
    }
    if chainName not in SUPPORTED_TYPE_REGISTRY_PRESETS:
        custom_type_registry = load_type_registry_file(chainConf[chainName]['type_registry_file'])
        chainConf[chainName]['type_registry'] = custom_type_registry

    substrate = SubstrateInterface(
        url=chainConf[chainName]['url'],
        ss58_format=chainConf[chainName]['ss58_format'],
        type_registry_preset=chainConf[chainName]['type_registry_preset'],
        type_registry=chainConf[chainName]['type_registry']
    )
    '''
    获取对应模块下面函数的具体含义及参数
    # print(substrate.get_metadata_storage_function(module_name='Session', storage_name='Validators'))
    获取对应模块下面的所有可调用的函数
    # for f in substrate.get_metadata_module(name='Session')['storage']['entries']:
    #     print(f)
    调用模块中的某函数
    # print(substrate.query(module='Session',storage_function='Validators'))
    
    获取所有支持的模块
    # for i in substrate.get_metadata_modules():
    #     print('module_name: {}'.format(i['name']))
    
    获取所有call funcation
    # for i in substrate.get_metadata_call_functions():
    #     print('call func: [{}], module name: [{}]'.format(i['call_name'], i['module_name']))
    '''
    validator_lists = substrate.query(module='Session', storage_function='Validators')
    activeEra = str(substrate.query(module='Staking', storage_function='ActiveEra')['index'])
    if addr not in validator_lists:
        return 'ok, [{}] in [{}] era is not validator.'.format(addr, activeEra)
    for i in substrate.query(module='Staking', storage_function='ErasRewardPoints', params=[activeEra])['individual']:
        if addr in i:
            return activeEra, i[0].value, i[1].value
    return 'faild, validator [{}] in [{}] era bad'.format(addr, activeEra)

if __name__ == '__main__':
    chainName = sys.argv[1]
    # chainName = 'crust'
    # addr = 'cTHCagRurm2D5r3vygwRWmRMHMrue3bk432MByyfXUEVNX8VV'
    with open('/etc/zabbix/addr.txt', 'r') as f:
        addr = f.read().strip('\r\n')
    print(main())
