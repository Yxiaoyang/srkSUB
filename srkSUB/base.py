#!/usr/bin/python3
# https://github.com/polkascan/py-substrate-interface
import substrateinterface as sub
from scalecodec.type_registry import load_type_registry_file, SUPPORTED_TYPE_REGISTRY_PRESETS

baseDir = sub.__file__.split("substrateinterface")[0] + "srkSUB\\"


class SUB(object):
    """
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
    k = Keypair.create_from_mnemonic(mnemonic=mnemonic, ss58_format=chainConf[chain_name]['ss58_format'])

    call = substrate.compose_call(call_module='PhalaStakePool', call_function='create')
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=k)

    receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=True)
    print("Extrinsic '{}' sent and included in block '{}'".format(receipt.extrinsic_hash, receipt.block_hash))

    """

    def __init__(self):
        self.crust = {
            # https: // github.com/crustio/crust.js/blob/mainnet/packages/type - definitions/src/json /types.json
            'url': "wss://rpc-crust-mainnet.decoo.io/",
            'ss58_format': 66,
            'type_registry_file': baseDir+'cru.json',
            'type_registry_preset': 'substrate-node-template',
            'type_registry': None
        }

        self.polkadot = {
            'url': "wss://rpc.polkadot.io",
            'ss58_format': 0,
            'type_registry_file': None,
            'type_registry_preset': 'polkadot',
            'type_registry': None
        }
        self.kusama = {
            'url': "wss://kusama-rpc.polkadot.io/",
            'ss58_format': 2,
            'type_registry_file': None,
            'type_registry_preset': 'kusama',
            'type_registry': None
        }

        self.khala = {
            # https: // github.com/Phala - Network/typedefs/blob/main/src/khala.ts
            'url': "wss://khala-api.phala.network/ws",
            'ss58_format': 30,
            'type_registry_file': baseDir+'khala.json',
            'type_registry_preset': 'substrate-node-template',
            'type_registry': None
        }

        self.chainConf = {
            'crust': self.crust,
            'polkadot': self.polkadot,
            'kusama': self.kusama,
            'khala': self.khala,
        }

    def connect(self, chain_name):
        if chain_name not in SUPPORTED_TYPE_REGISTRY_PRESETS:
            custom_type_registry = load_type_registry_file(self.chainConf[chain_name]['type_registry_file'])
            self.chainConf[chain_name]['type_registry'] = custom_type_registry

        substrate = sub.SubstrateInterface(
            url=self.chainConf[chain_name]['url'],
            ss58_format=self.chainConf[chain_name]['ss58_format'],
            type_registry_preset=self.chainConf[chain_name]['type_registry_preset'],
            type_registry=self.chainConf[chain_name]['type_registry']
        )
        return substrate
