#!/usr/bin/env python
# zhaoyafei 20181105
import os
import os.path as osp

# from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha


save_dir = './rlt_captcha'
if not osp.exists(save_dir):
    os.makedirs(save_dir)

save_base_fn = 'captcha_'

width = 160
height = 60
# font_sizes = None
font_sizes = (42, 50, 56)

# width = 320
# height = 120
# font_sizes = [84, 100, 112]

print 'output width: ', width
print 'output height: ', height

print 'font sizes: ', font_sizes

# audio = AudioCaptcha(voicedir='/path/to/voices')
# image = ImageCaptcha(fonts=['/path/A.ttf', '/path/B.ttf'])

# fonts = None
fonts = ['./fonts/arialbi.ttf']
# fonts = ['./fonts/courbd.ttf']
# fonts = ['./fonts/timesbi.ttf']

# fonts_dir = './fonts'
# fn_list = os.listdir(fonts_dir)
# fonts = []
# for f in fn_list:
#     if f.endswith('.ttf'):
#         fonts.append(osp.join(fonts_dir, f))

print 'using fonts: ', fonts

image = ImageCaptcha(width, height, fonts=fonts, font_sizes=font_sizes)

# # data = audio.generate('1234')
# # audio.write('1234', 'out.wav')

# # data = image.generate('1234', noise_dots=False, noise_curve=False
# #                       )

for i in range(10):
    save_fn = osp.join(save_dir, save_base_fn + str(i) + '.png')
    image.write('1234', save_fn, noise_dots=False, noise_curve=False)
