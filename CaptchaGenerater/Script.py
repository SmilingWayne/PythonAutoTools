import os
import random
from captcha.image import ImageCaptcha
# pip install captcha


def random_captcha_text(num):
    captcha_text = []
    for i in range(10):  # 0 - 9
        captcha_text.append(str(i))
    for i in range(65, 91):  # A - Z ASCII
        captcha_text.append(chr(i))
    for i in range(97, 123):  # a - z ASCII
        captcha_text.append(chr(i))
    example = random.sample(captcha_text, num)
    verification_code = ''.join(example)
    return verification_code
# 生成字符对应的验证码


def generate_captcha_image():
    image = ImageCaptcha()
    captcha_text = random_captcha_text(6)
    captcha_text = ''.join(captcha_text)
    path = './Result/'
    if not os.path.exists(path):
        os.makedirs(path)
    print("生成的验证码的图片为：", captcha_text)
    image.write(captcha_text, path + captcha_text + '.png')
if __name__ == '__main__':
    number = 30
    for i in range(number):
        generate_captcha_image()
