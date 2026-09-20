############################################################ IDENT(1)
#
# $Title: Makefile for installing condy $
# $Copyright: 2020-2026 Devin Teske. All rights reserved. $
# $FrauBSD: condy/GNUmakefile 2026-09-19 10:29:22 -0700 Devin Teske $
#
############################################################ INFORMATION
#
# DO NOT USE GNU EXTENSIONS IN THIS FILE
# THIS FILE MUST REMAIN USABLE BY NON-GNU MAKE
#
############################################################ CONFIGURATION

PREFIX?=	/usr/local
DESTDIR=	
BINDIR=		$(DESTDIR)$(PREFIX)/bin
MANDIR=		$(DESTDIR)$(PREFIX)/share/man/man1
EXAMPLEDIR=	$(DESTDIR)$(PREFIX)/share/examples/condy

############################################################ PATHS

CP_F=		cp -f
CP_R=		cp -Rf
MKDIR_P=	mkdir -p
NOT_EXISTS=	test ! -e
RM_F=		rm -f
RM_RF=		rm -rf
RMDIR=		rmdir
SED=		sed
CHMOD=		chmod
TOUCH=		touch
PYTHON?=	python3

############################################################ OBJECTS

CONDYIN=	condy.in
CONDY=		condy
MANIN=		condy.1.in
MAN=		condy.1
CONFSAMPLEIN=	samples/condy.conf.in
CONFSAMPLE=	samples/condy.conf
MKWALL=		tools/mk-sample-wallpapers.py
WALLGEN=	tools/.wallpapers
WALLPAPERS=	theme/wallpaper/sample-dusk.png \
		theme/wallpaper/sample-field.png \
		theme/wallpaper/sample-night.png \
		theme/tallpaper/sample-dusk.png \
		theme/tallpaper/sample-field.png \
		theme/tallpaper/sample-night.png

############################################################ TARGETS

all: $(CONDY) $(MAN) $(CONFSAMPLE) $(WALLGEN)

$(CONDY): $(CONDYIN) GNUmakefile
	$(SED) -e 's|@PREFIX@|$(PREFIX)|g' $(CONDYIN) > $(CONDY)
	$(CHMOD) +x $(CONDY)

$(MAN): $(MANIN) GNUmakefile
	$(SED) -e 's|@PREFIX@|$(PREFIX)|g' $(MANIN) > $(MAN)

$(CONFSAMPLE): $(CONFSAMPLEIN) GNUmakefile
	$(SED) -e 's|@PREFIX@|$(PREFIX)|g' $(CONFSAMPLEIN) > $(CONFSAMPLE)

$(WALLGEN): $(MKWALL)
	$(MKDIR_P) theme/wallpaper theme/tallpaper
	$(PYTHON) $(MKWALL)
	$(TOUCH) $(WALLGEN)

install: all
	$(MKDIR_P) $(BINDIR)
	$(MKDIR_P) $(MANDIR)
	$(MKDIR_P) $(EXAMPLEDIR)
	$(CP_F) $(CONDY) $(BINDIR)/
	$(CP_F) $(MAN) $(MANDIR)/
	$(CP_R) theme autostart $(EXAMPLEDIR)/
	$(CP_F) $(CONFSAMPLE) $(EXAMPLEDIR)/

uninstall:
	$(RM_F) $(BINDIR)/$(CONDY)
	$(RM_F) $(MANDIR)/$(MAN)
	$(RM_RF) $(EXAMPLEDIR)

clean:
	$(RM_F) $(CONDY) $(MAN) $(CONFSAMPLE) $(WALLPAPERS) $(WALLGEN)
	$(NOT_EXISTS) theme/wallpaper || $(RMDIR) theme/wallpaper || \
		: errors ignored
	$(NOT_EXISTS) theme/tallpaper || $(RMDIR) theme/tallpaper || \
		: errors ignored

################################################################################
# END
################################################################################
