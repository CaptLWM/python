# 패키지 사용하기
from image.io_file.imgread import pngread as jread  # 5
from image.io_file.imgread import pngread as pread  # 5
from image.io_file import imgread as img  # 4
from image.io_file.imgread import *  # 3
from image.io_file import imgread  # 2
import image.io_file.imgread  # 1

# 1
image.io_file.imgread.pngread()
image.io_file.imgread.jpgread()
'''
pngread in imgread module
jpgread in imgread module
'''
# 2
imgread.pngread()
imgread.jpgread()

# 3
pngread()
jpgread()


# 4
img.pngread()
img.jpgread()


# 5
pread()
jread()
