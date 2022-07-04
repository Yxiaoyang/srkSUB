# srkSUB



## 说明

> - 底层使用的是[polkascan](https://github.com/polkascan)的 [substrate-interface框架](https://github.com/polkascan/py-substrate-interface)，教程点链接可以查看的到
> - 该库只是解决了一些`substrate-interface`不支持的波卡生态下的 链的 `type definitions`转换问题，仅此而已



## 安装

```shell
pip install srkSUB
```



## 简单使用



### 连接`crust`

```python
from srkSUB.base import SUB
s = SUB()
cru = s.connect("crust")
print(cru.token_decimals)
```



### 连接`khala`

```python
from srkSUB.base import SUB
s = SUB()
kha = s.connect("khala")
print(kha.token_decimals)
```



> 实例之后的详细使用方法请查看`substrate-interface`文档