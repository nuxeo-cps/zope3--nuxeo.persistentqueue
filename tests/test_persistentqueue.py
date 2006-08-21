# (C) Copyright 2006 Nuxeo SAS <http://nuxeo.com>
# Author: Florent Guillaume <fg@nuxeo.com>
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
# $Id: test_persistentqueue.py 28842 2006-01-09 21:39:54Z fguillaume $
"""Basic tests.
"""

import unittest
from zope.testing.doctest import DocFileTest

def test_suite():
    return unittest.TestSuite((
        DocFileTest('test_persistentqueue.txt'),
        ))

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
