#!/usr/bin/env python3

import os
import sys
import yangvoodoo

if 'YANGPATH' not in os.environ:
    print('YANGPATH environment variable not set')
    sys.exit(1)


session = yangvoodoo.DataAccess()
session.connect('hello')
root = session.get_node()
print(root)

