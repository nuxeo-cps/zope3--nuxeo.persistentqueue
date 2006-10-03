# Copyright 2006 Nuxeo SAS <http://nuxeo.com>
# Author: Julien Anguenot <ja@nuxeo.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
#
"""nuxeo.persistentqueue

$Id: __init__.py 29888 2006-02-07 14:08:03Z janguenot $
"""

from zLOG import LOG, DEBUG

import os
import sys

# this allows the nuxeo.persistentqueue package to be installed as a
# Zope product.  It will add the src directory to the PYTHONPATH.
# Note that this strictly optional, just makes deployment with Zope
# more easy.
    
product_dir, filename = os.path.split(__file__)
src_path = os.path.join(product_dir, 'src')
if 'nuxeo' in sys.modules:
    nx_path = os.path.join(src_path, 'nuxeo')
    sys.path.insert(0, nx_path)
    import persistentqueue
    sys.modules['nuxeo.persistentqueue'] = persistentqueue
else:
    sys.path.insert(0, src_path)

LOG("nuxeo.persistentqueue", DEBUG, src_path)

from nuxeo.persistentqueue.persistentqueue import PersistentQueue

def initialize(context):
    pass
