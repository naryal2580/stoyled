def _generateEscapeSequence(styleSequence, preNum=0):
    """
    Generate Escape Sequence

        Parameters:
            styleSequence (list): Sequenced list of escape sequence
            preNum (int): Number, that prepends before sequence count
        
        Returns:
            variables (str): Newline separated list consisting set of
                                variables to be later used, instead
                                of escape sequences
    """
    count = 1
    variables = ''
    if preNum:
        postStyle = ''
        if int(preNum) == 9:  # if preNum is 9, then color from escape sequence is light
            postStyle = '_l'
        for style in styleSequence:
            style += postStyle
            variables += f"{style} = '\\x1b[{preNum}{count}m'\n"
            count += 1
    else:
        for _ in styleSequence:
            variables += f"{_} = '\\x1b[{count}m'\n"
            count += 1
    return variables


_STYLES = (
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

_COLORS = (
            'red',
            'green',
            'yellow',
            'blue',
            'purple',
            'cyan',
            'white'
        )


exec(_generateEscapeSequence(_STYLES))
exec(_generateEscapeSequence(_COLORS, 3))
exec(_generateEscapeSequence(_COLORS, 9))


rst = '\x1b[0m'  # Fixed escape sequence :p
