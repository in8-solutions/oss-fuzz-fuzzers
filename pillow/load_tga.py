import sys, os, warnings
import subprocess
from shutil import copyfile

copyfile(os.path.dirname(sys.executable) + '/libjpeg.so.8', '/usr/lib/x86_64-linux-gnu/libjpeg.so.8')
copyfile(os.path.dirname(sys.executable) + '/libtiff.so.5', '/usr/lib/x86_64-linux-gnu/libtiff.so.5')
copyfile(os.path.dirname(sys.executable) + '/libjbig.so.0', '/usr/lib/x86_64-linux-gnu/libjbig.so.0')
copyfile(os.path.dirname(sys.executable) + '/libwebp.so.5', '/usr/lib/x86_64-linux-gnu/libwebp.so.5')
copyfile(os.path.dirname(sys.executable) + '/libwebpmux.so.1', '/usr/lib/x86_64-linux-gnu/libwebpmux.so.1')
copyfile(os.path.dirname(sys.executable) + '/libwebpdemux.so.1', '/usr/lib/x86_64-linux-gnu/libwebpdemux.so.1')

sys.path.append(os.path.join(os.path.dirname(sys.path[-1]), 'pillow/src/'))
warnings.simplefilter("ignore")

import PIL

PIL._plugins[:] = ["TgaImagePlugin"]

from PIL import Image, ImageFile, WebPImagePlugin

def FuzzerRunOne(FuzzerInput):
    p = ImageFile.Parser()
    try:
        p.feed(FuzzerInput)
        im = p.close()
        im.load()
        im.close()
    except:
        pass
