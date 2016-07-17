# coding: utf-8
"""
setup
"""
import setuptools

version = '0.1.1'

setuptools.setup(
    name='filer2', # パッケージ名
    version=version, # バージョン
    description="A simple library for file edition", # 一言で説明
    # 詳細は http://pypi.python.org/pypi?:action=list_classifiers を参照
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    # キーワードを書いておく
    keywords='csv, tsv, dump, read, write',
    # 作者の名前
    author='kenchin110100',
    # 連絡先
    author_email='kenchin110100@yahoo.co.jp',
    # GitHubのリポジトリとか
    url='http://orenotame.com/',
    # ライセンス
    license='MIT',
    packages=setuptools.find_packages(exclude=['examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    # Pypiのページで表示する説明文(README)
    long_description='README.rst',
    # インストールする依存パッケージ
    install_requires=["numpy"],
)