# GNU Makefile for KBook

PREFIX    := $(HOME)/.local

PACKAGE   := KBook
TARGET    := kbook
RELEASE   := 1.0

DIRSRC    := src
DIRSHARE  := share
SYSBINDIR := $(PREFIX)/bin
SYSDIRKBOOK := $(PREFIX)/kbook

SRC := $(DIRSRC)/build_summary.py
SRC += $(DIRSRC)/generate_book.py

install:
	mkdir -p $(DESTDIR)$(SYSDIRKBOOK)
	cp -rf $(SRC) $(DESTDIR)$(SYSDIRKBOOK)
	cp -rf $(DIRSHARE) $(DESTDIR)$(SYSDIRKBOOK)/html
	install -D $(DIRSRC)/kbook.py $(DESTDIR)$(SYSBINDIR)/$(TARGET)

uninstall:
	rm -rf $(DESTDIR)$(SYSDIRKBOOK)
	rm -rf $(DESTDIR)$(SYSBINDIR)/$(TARGET)
