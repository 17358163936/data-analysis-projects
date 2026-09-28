def decrypt_price(encrypted_price):
    # 创建一个空字符串来存储解密后的价格
    decrypted_price = ""
    decryption_dict = {
        '%': '8', '+': '2', '-': '9', '/': '0', '¥': '5', '万': '1', '元': '3', '折': '4', '时': '6', '起': '7'
    }

    # 遍历加密价格字符串中的每个字符
    for char in encrypted_price:
        # 如果字符在解密字典中，替换为对应的数字
        if char in decryption_dict:
            decrypted_price += str(decryption_dict[char])
        # 如果字符不在字典中，直接添加到解密字符串中
        else:
            decrypted_price += char

    return decrypted_price

# 解密字典
decryption_dict = {
    '%': '8', '+': '2', '-': '9', '/': '0', '¥': '5', '万': '1', '元': '3', '折': '4', '时': '6', '起': '7'
}

# 示例加密价格字符串
encrypted_price = "万+时.%/"

# 解密价格
decrypted_price = decrypt_price(encrypted_price)

# 输出解密后的价格
print("解密后的价格:", decrypted_price)