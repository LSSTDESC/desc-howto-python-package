
import os
import desc_howto_python_package

TOPDIR = os.path.abspath(os.path.dirname(desc_howto_python_package.__file__))

def test_data():

    files = [
        'i_knew.txt',
        'oh_you_will.txt',
        'sir_john_davies.txt'
    ]

    for a_file in files:
        full_path = os.path.join(TOPDIR, 'data', a_file)
        with open(full_path) as fin:
            fin.read()


