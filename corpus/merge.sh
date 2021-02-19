#!/usr/bin/env bash

if [ ! -d merged_data_sets ]; then
  mkdir merged_data_sets
fi

echo "每个语料的统计信息:"
ls ./sources/**/*.txt | xargs -n 1 -I {} wc -l {}

echo "处理之前语料总量统计信息:"
ls ./sources/**/*.txt | xargs -n 1 -I {} wc -l {} | awk -F " " '{sum += $1} END {print sum}'

merge_id=$(date +%Y%m%d%H%M%S)
new_file="merged_data_sets/v1_${merge_id}".txt

cat ./sources/**/*.txt >>$merge_id
# 去重
sort -u $merge_id >$new_file
rm $merge_id

echo "已合并，统计信息如下:"
wc -l $new_file
