############################################################ IDENT(1)
#
# $Title: Makefile for installing condy on non-GNU systems $
# $Copyright: 2019-2026 Devin Teske. All rights reserved. $
# $FrauBSD: condy/Makefile 2026-09-19 10:29:22 -0700 Devin Teske $
#
############################################################ CONFIGURATION

DESTDIR=
TARGETS=	all \
		clean \
		install \
		uninstall

############################################################ TARGETS

$(TARGETS):
	$(MAKE) -f GNUmakefile $(MFLAGS) $(@)

################################################################################
# END
################################################################################
