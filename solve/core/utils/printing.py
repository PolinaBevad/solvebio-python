import os
import sys
import subprocess
import locale

locale.setlocale(locale.LC_ALL, 'en_US')

from solve.core.solvelog import solvelog
from solve.core.solveconfig import solveconfig

if sys.stdout.isatty():
    try:
        with open(os.devnull, 'w') as fnull:
            rows, cols = subprocess.check_output(['stty', 'size'],
                                            stderr=fnull).split()
            solveconfig.TTY_ROWS = int(rows)
            solveconfig.TTY_COLS = int(cols)
    except:
        solvelog.warn('Cannot detect terminal column width')
else:
    solveconfig.TTY_COLORS = False


def pretty_int(num):
    return locale.format("%d", int(num), grouping=True)


# Basic color support

def green(text):
    if not solveconfig.TTY_COLORS:
        return text
    return '\033[32m' + text + '\033[39m'


def red(text):
    if not solveconfig.TTY_COLORS:
        return text
    return '\033[31m' + text + '\033[39m'


def yellow(text):
    if not solveconfig.TTY_COLORS:
        return text
    return '\033[33m' + text + '\033[39m'


def blue(text):
    if not solveconfig.TTY_COLORS:
        return text
    return '\033[34m' + text + '\033[39m'


def solve_bio():
    return blue('SolveBio')