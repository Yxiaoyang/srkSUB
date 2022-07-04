from setuptools import setup, find_packages

GFICLEE_VERSION = '1.0'

setup(
    name='srkSUB',
    version=GFICLEE_VERSION,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ['cfastproject = fastproject.main:main']
    },
    install_requires=[
        "substrate-interface", "scalecodec"
    ],
    url='https://github.com/Yxiaoyang/',
    license='GNU General Public License v3.0',
    author='srank',
    author_email='625593240@qq.com',
    description='Support More Substrate Chain Package'
)
