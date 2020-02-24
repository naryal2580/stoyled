from .genStyls import *


def fetchFormatedTime():
    from datetime import datetime
    now = datetime.now()
    dd = str(now.day)
    mm = str(now.month)
    yyyy = str(now.year)
    HH = str(now.hour)
    MM = str(now.minute)
    SS = str(now.second)
    now = (dd, mm, yyyy, HH, MM, SS)
    now = now[0]+'.'+now[1]+'.'+now[2]+' '+now[3]+':'+now[4]+':'+now[5]
    return now


def coolExit(exitCode=0, color=True):
    now = fetchFormatedTime()
    print(info(f'Halted [at] -> {now}', color))
    exit(exitCode)


def coolInput(prompt='Prompt', color=True):
    try:
        if color:
            prompt = f'{ rst + white }[{ bold + purple_l }<{ rst + white }]{ rst + purple_l } { prompt }: { rst + white + italic }'
        else:
            prompt = f'[<] {prompt}: '
        _input = input(prompt)
        if color:
            print(rst, end='')
        return _input
    except KeyboardInterrupt:
        print('Null'+rst)
        print(bad('Exitting -> recvd. SIGINT'))
        coolExit(1)
    except EOFError:
        print('Null'+rst)
        print(bad('Terminating -> EOFError'))
        coolExit(1)
