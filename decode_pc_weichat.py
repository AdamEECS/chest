import re


def _decode_pc_dat(datfile):
    with open(datfile, 'rb') as f:
        buf = bytearray(f.read())

    magic = 0xff ^ list(buf)[0] if buf else 0x00
    print(magic)

    imgfile = re.sub(r'.dat$', '.jpg', datfile)
    with open(imgfile, 'wb') as f:
        newbuf = bytearray(map(lambda b: b ^ magic, list(buf)))
        f.write(newbuf)


if __name__ == '__main__':
    _decode_pc_dat(datfile='XXXXS.dat')
