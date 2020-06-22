from .escapeSequences import *


_FORMATS = {
    'info': [
            '*',
            'cyan',
            'blue_l'
            ],
    'warn': [
            '!',
            'yellow_l',
            'yellow'
            ],
    'good': [
            '+',
            'green_l',
            'green'
            ],
    'bad': [
            '-',
            'red_l',
            'red'
            ],
    'takenInput': [
                    '<',
                    'purple_l',
                    'italic'
                    ]
        }


def _generateFunction(_format, formats):
    """
    Generate Fucntion, based on specified format from dict above (_FORMATS)

        Parameters:
            _format (str): Format for this function, to generate funcion from `formats` (dict) above

        Returns:
            func (str): Returns a string, which is a function to `exec()`
    """
    func = 'def '+_format+'(text,color=True):\n\t"""\n\tRich style '+_format+'\n\n\t\tNote:\n\t\t\tIf you want to print `['+formats[_format][0]+'] foo: bar`, then pass text parameter as `foo -> bar` and see the fanciness\n\n\t\tParameters:\n\t\t\ttext (str): Text to be printed\n\t\t\tcolor (bool): Shall colors be used via ANSI Escape Sequence\n\t\t\n\t\tReturns:\n\t\t\tstr: Fancily styled string, which is just ready to print!\n\t"""\n\ttext=str(text)\n\tif len(text.split(\' -> \'))==2:\n\t\t\ttext=text.split(\' -> \')\n\tif color:\n\t\tif type(text)==str:\n\t\t\treturn f\'{rst}[{rst+bold+'+formats[_format][1]+'}'+formats[_format][0]+'{rst+white}] {rst+'+formats[_format][2]+'}{text}{rst}\'\n\t\telif type(text)==list:\n\t\t\treturn f\'{rst+white}[{rst+bold+'+formats[_format][1]+'}'+formats[_format][0]+'{rst+white}]{rst+'+formats[_format][2]+'} {text[0]}: {rst+'+formats[_format][1]+'+italic}{text[1]}{rst}\'\n\telse:\n\t\tif type(text)==str:\n\t\t\treturn f\'['+formats[_format][0]+'] {text}\'\n\t\telif type(text)==list:\n\t\t\treturn f\'['+formats[_format][0]+'] {text[0]}: {text[1]}\''
    return func


for _format in _FORMATS:
    func = _generateFunction(_format, _FORMATS)
    exec(func)
