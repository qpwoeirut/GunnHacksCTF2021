SUBDIRS := $(wildcard */.)

all: $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@

.PHONY: all $(SUBDIRS)

BUNDLE: shell_manager install-bundle bundle.json
