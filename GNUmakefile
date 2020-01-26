############################################################ IDENT(1)
#
# $Title: Makefile for installing condy $
# $Copyright: 2020 Devin Teske. All rights reserved. $
# $FrauBSD: condy/GNUmakefile 2020-01-25 20:48:56 -0800 freebsdfrau $
#
############################################################ INFORMATION
#
# DO NOT USE GNU EXTENSIONS IN THIS FILE
# THIS FILE MUST REMAIN USABLE BY NON-GNU MAKE
#
############################################################ CONFIGURATION

DESTDIR=	
BINDIR=		$(DESTDIR)/usr/local/bin

############################################################ PATHS

CP_F=		cp -f
MKDIR_P=	mkdir -p
RM_F=		rm -f

############################################################ OBJECTS

CONDY=		condy

############################################################ TARGETS

all:

install:
	$(MKDIR_P) $(BINDIR)
	$(CP_F) $(CONDY) $(BINDIR)/

uninstall:
	$(RM_F) $(BINDIR)/$(NSADMIN)

################################################################################
# END
################################################################################
