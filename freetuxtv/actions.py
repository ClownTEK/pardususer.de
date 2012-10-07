#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("Makefile.in", "^(freetuxtvdocdir\s*=)\s*.*", r"\1 /usr/share/doc/%s" % get.srcNAME())
    autotools.configure("--disable-static --enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

# By PiSiDo 2.0.0
