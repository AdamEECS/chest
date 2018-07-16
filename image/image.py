from PIL import Image


def cut(x, y, w, h, name):
    img = Image.open('enemy.png')
    reg = (x, y, x + w, y + h)
    print(reg)
    crop = img.crop(reg)
    crop.save(name)


def main():
    w = 32
    h = 32
    # cut(32 * 4, 0, 32, 32, 'lm_bullet.png')
    for i in range(4):
        name = 'enemy_lg3_{}.png'.format(i)
        x = 0 + i * w
        y = 161
        cut(x, y, w, h, name)


if __name__ == '__main__':
    main()
