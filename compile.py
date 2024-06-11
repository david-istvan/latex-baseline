import subprocess, sys
from enum import Enum

class CommandType(Enum):
    PDF = 'pdflatex',
    BIB = 'bib',
    MULTIBIB = 'multibib'

OUTPUT_DIRECTORY = 'output'
PDF_COMMAND = 'pdflatex'
BIB_COMMAND = 'bibtex'

commands = {
    CommandType.PDF : [PDF_COMMAND, '-output-directory', OUTPUT_DIRECTORY, f'{sys.argv[1]}.tex'],
    CommandType.BIB : [BIB_COMMAND, f'{OUTPUT_DIRECTORY}/{sys.argv[1]}.aux'],
    # CommandType.MULTIBIB : [BIB_COMMAND, f'{OUTPUT_DIRECTORY}/{sys.argv[2]}.aux'] -- Uncomment if multibib is used (e.g., with ACM)
}

full_compile_sequence = [
    CommandType.PDF,
    CommandType.BIB,
    # CommandType.MULTIBIB, -- Uncomment if multibib is used (e.g., with ACM)
    CommandType.PDF,
    CommandType.PDF
]

for c in full_compile_sequence:
    print(c)
    subprocess.call(commands[c], shell=True)

"""
Compile with:
    python .\compile.py [main tex/bib name] ([multibib name]).
Example:
    python .\compile.py main -- without multibib
    python .\compile.py main PS -- with multibib
"""