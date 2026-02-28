UNICODE_MAX = 0x110000
KEY = 1627

def encrypt(plaintext):
    # 1단계: 뒤집기
    reversed_text = plaintext[::-1]

    # 2단계: 유니코드 안전 시프트
    encrypted_chars = []
    for char in reversed_text:
        code = (ord(char) + KEY) % UNICODE_MAX
        encrypted_chars.append(chr(code))

    return ''.join(encrypted_chars)


def decrypt(ciphertext):
    decrypted_chars = []
    for char in ciphertext:
        code = (ord(char) - KEY) % UNICODE_MAX
        decrypted_chars.append(chr(code))

    # 다시 뒤집기
    return ''.join(decrypted_chars)[::-1]