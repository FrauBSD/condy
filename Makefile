############################################################ IDENT(1)
#
# $Title: Makefile for installing nsadmin on non-GNU systems $
# $Copyright: 2019 Devin Teske. All rights reserved. $
# $FrauBSD: condy/Makefile 2020-01-25 20:48:56 -0800 freebsdfrau $
#
############################################################ CONFIGURATION

DESTDIR=
TARGETS=	all \
		install \
		uninstall

############################################################ TARGETS

$(TARGETS):
	$(MAKE) -f GNUmakefile $(MFLAGS) $(@)

################################################################################
# END
################################################################################
