import sys
import os

# 현재 파일 기준 상위 디렉터리 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import crypt_utils
test_enc = crypt_utils.encrypt('123')
print(test_enc)
test_dec = crypt_utils.decrypt(test_enc)
print(test_dec)