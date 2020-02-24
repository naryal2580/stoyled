def genEscSeqs(stylSeq, preNum=''):
    count = 1
    out = ''
    if preNum:
        postStyl = ''
        if int(preNum) == 9:
            postStyl = '_l'
        for _ in stylSeq:
            _ += postStyl
            out += f"{_} = '\\x1b[{preNum}{count}m'\n"
            count += 1
    else:
        for _ in stylSeq:
            out += f"{_} = '\\x1b[{count}m'\n"
            count += 1
    return out


STYLS = (
    'bold',
    'dim',
    'italic',
    'uline',
    'blink',
    'normal',
    'invert',
    'hidden',
    'strike'
        )

COLRS = (
    'red',
    'green',
    'yellow',
    'blue',
    'purple',
    'cyan',
    'white'
        )

exec(genEscSeqs(STYLS))
exec(genEscSeqs(COLRS, 3))
exec(genEscSeqs(COLRS, 9))
rst = '\x1b[0m'
