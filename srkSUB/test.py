#!/usr/bin/python3
# https://github.com/polkascan/py-substrate-interface
from substrateinterface import *
from scalecodec.type_registry import load_type_registry_file, SUPPORTED_TYPE_REGISTRY_PRESETS


def main():
    crust = {
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

    khala = {
         # https: // github.com / Phala - Network / typedefs / blob / main / src / khala.ts
        'url': "wss://khala-api.phala.network/ws",
        'ss58_format': 30,
        'type_registry_file': '../pha/khala.json',
        'type_registry_preset': 'substrate-node-template',
        'type_registry': None
    }

    chainConf = {
        'crust': crust,
        'polkadot': polkadot,
        'kusama': kusama,
        'khala': khala,
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
    storage函数为存储函数，查询使用
    call为调用函数，可执行操作
    
    查询块中的某storage函数
    print(substrate.query(module='Session',storage_function='Validators'))
    
    获取所有支持的模块（包含storage，call  funcation）
    for i in substrate.get_metadata_modules():
        print('module_name: {}'.format(i['name']))
        
    获取对应模块下面的所有可调用的storage函数
    for f in substrate.get_metadata_module(name='Session')['storage']['entries']:
        print(f['name'])
        
    获取对应模块下面storage函数的具体含义及参数
    print(substrate.get_metadata_storage_function(module_name='Session', storage_name='Validators'))
    
    获取所有call funcation
    for i in substrate.get_metadata_call_functions():
        print('call func: [{}], module name: [{}]'.format(i['call_name'], i['module_name']))
        
    查询某call funcation用法
    print(substrate.get_metadata_call_function(module_name="PhalaStakePool", call_function_name="create"))
    
    call 函数调用示例（创建一个池子）
    k = Keypair.create_from_mnemonic(mnemonic=mnemonic, ss58_format=chainConf[chainName]['ss58_format'])

    call = substrate.compose_call(call_module='PhalaStakePool', call_function='create')
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=k)
    
    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    print("Extrinsic '{}' sent and included in block '{}'".format(receipt.extrinsic_hash, receipt.block_hash))
    
    '''
    # print(substrate.get_metadata_call_function(module_name="Balances", call_function_name="transfer"))

    print(substrate.token_decimals)
    # print(substrate.get_metadata_storage_function(module_name='PhalaStakePool', storage_name='StakePools'))
    # print(substrate.query(module='PhalaStakePool', storage_function='StakePools', params=[2151]))
    # print(substrate.query(module='PhalaStakePool', storage_function='MiningEnabled'))

    # mnemonic = Keypair.generate_mnemonic()
    # result = Keypair.create_from_mnemonic(mnemonic=mnemonic, ss58_format=66)
    # print('addr: %s, privkey: %s' % (result.ss58_address, result.mnemonic))

    # print(substrate.get_block_number(substrate.get_chain_head()))
    # currentEra = substrate.query(module='Staking', storage_function='CurrentEra')
    # print(currentEra)
    # print(substrate.query(module='Session', storage_function='Validators'))
    # print(substrate.query(module='Staking', storage_function='ErasRewardPoints', params=[currentEra]))
    # input()
    # lst = [[str(i[0]),str(i[1])] for i in substrate.query(module='Staking', storage_function='ErasRewardPoints', params=[currentEra])['individual'] if addr in i]
    # if len(lst):
    #     return str(currentEra), lst[0][0], lst[0][1]
    # return 'ok, {} era is not validator.'.format(currentEra)
    # a = substrate.query(module='System', storage_function='Properties')
    # return a


if __name__ == '__main__':
    # chainName = sys.argv[1]
    # with open('addr.txt', 'r') as f:
    #     addr = f.read()
    chainName = 'khala'
    mnemonic = "frost glue salad ring depart knee sport wall recipe will orbit dentist"
    addr = '445GqYJ9EFxeAPfaAyrQjzzapRB419JTKnbR4Yz8JrKxAdhG'
    # chainName = 'polkadot'
    # addr = '1gpCRov55rqmNaoEVRNAUCCYVzSGghitLNabng8UHVGwv1g'
    main()