alphabet = "".join(["ئ", "ا", "ە", "ب", "پ", "ت", "ج", "چ", "خ", "د", "ر", "ز", "ژ", "س", "ش", "غ", "ف", "ق",
                    "ك", "گ", "ل", "ڭ", "م", "ن", "ھ", "و", "ۇ", "ۆ", "ۈ", "ۋ", "ې", "ى", "ي"])
codebook = "".join(["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l",
                    "z", "x", "c", "v", "b", "n", "m", "7", "6", "5", "4", "3", "2", "1"])


def encode(target_contents: str):
    """
    shirkhan 加密器
    :param target_contents:
    :return:
    """
    for i in range(0, len(alphabet)):
        target_contents = target_contents.replace(alphabet[i], codebook[i])
    return target_contents


def decode(target_contents: str):
    """
    shirkhan 加密对应的解码器
    :param target_contents:
    :return:
    """
    for i in range(0, len(alphabet)):
        target_contents = target_contents.replace(codebook[i], alphabet[i])
    return target_contents


if __name__ == '__main__':
    pass
    target_context = "سالام دۇنيا"
    encode_example = encode(target_context)
    print("target_context,encode_example", target_context, " ---", encode_example)

    print("---" * 20)
    decode_example = decode(encode_example)
    print("encode_example,decoded_example", encode_example, " ---", decode_example)
