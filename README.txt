$Id: README.txt 29890 2006-02-07 14:14:08Z janguenot $

Persistent Queue that is conflict-aware.
See tests/test_persistentqueue.txt for more.

Zope2 package 
==============

To install it as a Zope2 Package you need to rename the top level package to
something else than nuxeo.persistentqueue since it contains a '.' (dot) in it.

For instance this would be fine :

svn co 
https://svn.nuxeo.org/priv/nuxeo.persistentqueue/trunk nuxPersistentQueue
