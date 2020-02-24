from .escSeqs import *


formats = {
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


def retnFunc(_format):
    func = "def "+_format+"(text,color=True):\n\ttext=str(text)\n\tif len(text.split(\' -> \'))==2:\n\t\ttext=text.split(\' -> \')\n\tif color:\n\t\tif type(text)==str:\n\t\t\treturn f\'{rst}[{rst+bold+"+formats[_format][1]+"}"+formats[_format][0]+"{rst+white}] {rst+"+formats[_format][2]+"}{text}{rst}\'\n\t\telif type(text) == list:\n\t\t\treturn f\'{rst+white}[{rst+bold+"+formats[_format][1]+"}"+formats[_format][0]+"{rst+white}]{rst+"+formats[_format][2]+"} {text[0]}: {rst+"+formats[_format][1]+"+italic}{text[1]}{rst}\'\n\telse:\n\t\tif type(text)==str:\n\t\t\treturn f\'["+formats[_format][0]+"] {text}\'\n\t\telif type(text)==list:\n\t\t\treturn f\'["+formats[_format][0]+"] {text[0]}: {text[1]}\'"
    return func


for _format in formats:
    func = retnFunc(_format)
    exec(func)


del _format, func, formats, STYLS, COLRS, genEscSeqs, retnFunc
