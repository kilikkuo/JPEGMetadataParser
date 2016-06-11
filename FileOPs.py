BYTE_ALIGN_INTEL    = 0x4949
BYTE_ALIGN_MOTOROLA = 0x4d4d

def nowAt(f):
    assert not not f
    assert hasattr(f, "tell")
    return f.tell()

def seekTo(f, tarPos):
    assert not not f
    assert hasattr(f, "seek")
    f.seek(tarPos)

def getChar(f, size=1):
    assert not not f
    assert hasattr(f, "read")
    return f.read(size)

def getCharToOrd(f):
    c = getChar(f)
    if c == '':
        return -1
    return ord(c)

def getBytes2(f, order=BYTE_ALIGN_MOTOROLA):
    # 0x4d4d for MM / 0x4949 for II.
    L = getCharToOrd(f)
    H = getCharToOrd(f)
    if order == BYTE_ALIGN_MOTOROLA:
        return L << 8 | H
    else:
        return L | H << 8

def getBytes4(f, order=BYTE_ALIGN_MOTOROLA):
    # 0x4d4d for MM / 0x4949 for II.
    LL = getCharToOrd(f)
    LH = getCharToOrd(f)
    HL = getCharToOrd(f)
    HH = getCharToOrd(f)
    if order == BYTE_ALIGN_MOTOROLA:
        return LL << 24 | LH << 16 | HL << 8 | HH
    else:
        return LL | LH << 8 | HL << 16 | HH << 24

def getBytes8(f, order=BYTE_ALIGN_MOTOROLA):
    # 0x4d4d for MM / 0x4949 for II.
    LLL = getCharToOrd(f)
    LLH = getCharToOrd(f)
    LHL = getCharToOrd(f)
    LHH = getCharToOrd(f)
    HLL = getCharToOrd(f)
    HLH = getCharToOrd(f)
    HHL = getCharToOrd(f)
    HHH = getCharToOrd(f)
    if order == BYTE_ALIGN_MOTOROLA:
        return LLL << 56 | LLH << 48 | LHL << 40 | LHH << 32 |\
                HLL << 24 | HLH << 16 | HHL << 8 | HHH
    else:
        return LLL | LLH << 8 | LHL << 16 | LHH << 24 |\
                HLL << 32 | HLH << 40 | HHL << 48 | HHH << 56
