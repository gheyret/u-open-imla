import os

from shirkhan import File, encode


def get_all_words(target_folder="shirkhan-salon"):
    all_words = []
    for file in os.listdir(target_folder):
        fileHandler = File(os.path.join("./", target_folder, file))
        all_words.extend(fileHandler.get_u_words())
    return all_words


def write_words(all_words: list, target_file_name="result.txt"):
    with open(target_file_name, mode="w", encoding="utf-8") as f:
        f.write("\n".join(sorted(set(all_words))))


if __name__ == '__main__':
    pass
    """
    遍历指定目录下的所有文件[都是纯文本文件] 
    提取内容中的所有母语词汇
    写入结果集文件中农
    """
    target_foldername = "shirkhan-salon"
    result_file_name = "shirkhan-salon.txt"
    write_words([encode(word) for word in get_all_words(target_foldername)], result_file_name)
