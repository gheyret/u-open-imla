import re


def text_to_words(context: str):
    """
    从给定内容中去掉所有非母语内容，只保留母语部分
    [从给定内容中提取词]
    :param context: 需要提出词汇的内容
    :return : 返回提取后的词汇集合
    """
    context = context.strip()
    if len(context) == 0:
        return []

    context = re.sub("[^چۋېرتيۇڭوپھسداەىقكلزشغۈبنمئلاۆجخگفژٴحعۉۅ]", " ", context)  # 非母语替换成空白
    return context.split()


if __name__ == '__main__':
    pass
    target_contents = "你好么,hello -world, ياخشىمۇ سىز"
    print("target_contents,txt_to_words", target_contents, text_to_words(target_contents))
