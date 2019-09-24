# -*- coding: utf-8 -*
from PIL import Image


def watermark(img_source, img_water, img_new):
    try:
        im = Image.open(img_source)
        wm = Image.open(img_water)
        w_x, w_y = wm.size
        i_x, i_y = im.size
        layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
        # layer.paste(wm, (im.size[0] - w_x, im.size[1] - w_y))
        layer.paste(wm, (im.size[0] - i_x, im.size[1] - i_y))
        newIm = Image.composite(layer, im, layer)
        newIm.save(img_new)

    except Exception as e:
        print(">>>>>>>>>>> WaterMark EXCEPTION:  " + str(e))
        return False
    else:
        return True


def main():
    watermark("/Users/lee/Documents/图片/lwj.jpg", "/Users/lee/Documents/图片/flag-resize-2.jpg",
              "/Users/lee/Documents/图片/afterwater.jpg")
    print('生成图片成功')


if __name__ == '__main__':
    main()
