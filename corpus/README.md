# 目录说明

- sources 语料原始词汇集
- merged_data_sets 合并sources目录下语料生成的总语料词汇集
- merge.sh 合并sources下所有语料生成一个最新语料并按日期命名后存放在 merged_data_sets 目录下

这个目录中存放的都是原料数据，想用来:

1. 都是靠谱，没有敏感词的网络资源中提取的词汇，可以用来过滤词
2. 都是常用内容提取的词汇，可以用来做对错对照词
3. 可以做其他统计类工作，如实用性，频率等
4. 可以用来做输入法推荐词库
5. 其他

## 词库加解密

本目录下的词汇都是用 shirkhan lib中的encode算法来加密的，需要时可以使用对应的decode解密来。

使用python代码加密解密指南：

```python
from shirkhan import decode, encode

encode("xxxx")
decode("yyy")

```

## merge.sh

```shell
chmod +x merge.sh
./merge.sh
```
