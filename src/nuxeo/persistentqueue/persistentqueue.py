# Copyright 2006 Nuxeo SAS <http://nuxeo.com>
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
# $Id: persistentqueue.py 29888 2006-02-07 14:08:03Z janguenot $
"""
Conflict-aware persistent queue.
"""

try:
    from persistent.list import PersistentList
except ImportError:
    # Compattibility ZODB 3.2.x
    from ZODB.PersistentList import PersistentList

from ZODB.POSException import ConflictError

def difference(c1, c2):
    diff = []
    for v in c1:
        if v not in c2:
            diff.append(v)
    return diff

class PersistentQueue(PersistentList):
    """Conflict-aware persistent queue.

    This is basically a persistent list with better conflict resolution
    for the cases of simultaneous pop(0) and append().

    """

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return 'PersistentQueue(%r)' % (self.data,)

    def __getstate__(self):
        return self.data

    def __setstate__(self, v):
        self.data = v

    def _p_independent(self):
        # State doesn't depend on or affect the state of other objects
        return 1

    def _p_resolveConflict(self, old, saved, new):
        saved_removed = difference(old, saved)
        saved_added = difference(saved, old)

        new_removed = difference(old, new)
        new_added = difference(new, old)

        if saved_removed and new_removed:
            # Only one thread is allowed to pop
            raise ConflictError

        for val in saved_added:
            if val in new_added:
                new_added.remove(val)

        for val in saved_removed:
            if val in new_removed:
                new_removed.remove(val)

        for val in saved_removed:
            old.remove(val)

        for val in new_removed:
            old.remove(val)

        old.extend(saved_added)
        old.extend(new_added)

        return old
