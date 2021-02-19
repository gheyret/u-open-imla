#!/usr/bin/env bash
echo "正在打包....."
python3 setup.py sdist bdist_wheel
# 友情提醒
# python setup.py bdist_wheel 报错的处理办法
# 多半是setuptools版本不正确或者你的环境中没有安装wheel， 请使用一下命令升级：
# pip install wheel
# pip install --upgrade setuptools
# pip install twine

echo "正在发布，过程需要提供账户和密码......"
twine upload dist/*
echo "正在清理发布产生的目录信息......"
rm -rf build dist
echo "发布完成!"