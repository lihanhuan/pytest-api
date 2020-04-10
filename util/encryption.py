
# hashlib是一个提供字符加密功能的模块，包含MD5和SHA的加密算法，具体支持md5,sha1, sha224, sha256, sha384, sha512等算法
# base64 base32
import hashlib


def md5_data(data):
    """
    md5加密
    创建加密对象
    对字符串进行算法加密
    展示
    """
    # 创建hashlib的md5对象
    m1 = hashlib.md5()
    # 将字符串载入到md5对象中，获得md5算法加密
    m1.update(data.encode("utf-8"))
    # 通过hexdigest()方法，获得new_md5对象的16进制md5显示
    data = m1.hexdigest()
    return data


if __name__ == "__main__":
    print(md5_data("123456"))