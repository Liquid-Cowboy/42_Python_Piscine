#!/usr/bin/env python3

import sys
from site import getsitepackages
from os.path import basename


def get_prefix() -> str:
    """While using venv to create a virtual environment, if we want
    to check whether we're operating inside the virtual environment
    or not, it's enough to check if the python interpreter used to
    create the environment ("sys.base_prefix") differs from the system prefix
    ("sys.prefix"). However if we use older versions of virtualenv (<v.20)
    to create the environment, we just have to check if "sys.real_prefix"
    exists (this attribute is created along with the virtual environment).
    Although we probably won't encounter such circunstances, this checker
    handles legacy cases that could occur with python versions prior to 3.4"""
    return (
            getattr(sys, "base_prefix", None)
            or getattr(sys, "real_prefix", None)
            or sys.prefix
        )


if __name__ == '__main__':
    if get_prefix() != sys.prefix:
        print('\nMATRIX STATUS: Welcome to the construct\n')
        print('Current Python:', sys.executable)
        print('Virtual Environment:', basename(sys.prefix))
        print('Environment Path:', sys.prefix)
        print('\nSUCCESS: You\'re in an isolated environment!')
        print('Safe to install packages without affecting\nthe global system.')
        print('\nPackage installation path:\n', getsitepackages(), sep='')

    else:
        print('\nMATRIX STATUS: You\'re still plugged in\n')
        print('Current Python:', sys.executable)
        print('Virtual Environment: None detected')
        print('\nWARNING: You\'re in the global environment!')
        print('The machines can see everything you install.')
        print('\nTo enter the construct, run:')
        print('python -m venv matrix_env')
        print('source matrix_env/bin/activate\t# On Unix')
        print('matrix_env')
        print('Scripts')
        print('activate\t# On Windows')
        print('\nThen run this program again.')
