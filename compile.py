import subprocess, sys
from enum import Enum

class CommandType(Enum):
    PDF = 'pdflatex',
    BIB = 'bib'

OUTPUT_DIRECTORY = 'output'
PDF_COMMAND = 'pdflatex'
BIB_COMMAND = 'bibtex'

commands = {
    CommandType.PDF : [PDF_COMMAND, '-output-directory', OUTPUT_DIRECTORY, f'{sys.argv[1]}.tex'],
    CommandType.BIB : [BIB_COMMAND, f'{OUTPUT_DIRECTORY}/{sys.argv[1]}.aux']
}

full_compile_sequence = [
    CommandType.PDF,
    CommandType.BIB,
    CommandType.PDF,
    CommandType.PDF
]

for c in full_compile_sequence:
    print(c)
    subprocess.call(commands[c], shell=True)