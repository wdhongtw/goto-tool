BIN_DIR = $(HOME)/.local/bin
BASH_CONFIG_DIR = $(HOME)/.config/bashrc.d

BACKEND_SRC = $(abspath backend.py)
BACKEND_BIN = $(BIN_DIR)/_goto_backend

FRONTEND_SRC = $(abspath frontend.bash)
FRONTEND_BASH = $(BASH_CONFIG_DIR)/goto.bash

.PHONY: install uninstall

install:
	mkdir -p "$(BIN_DIR)"
	ln -s "$(BACKEND_SRC)" "$(BACKEND_BIN)"
	mkdir -p "$(BASH_CONFIG_DIR)"
	ln -s "$(FRONTEND_SRC)" "$(FRONTEND_BASH)"

uninstall:
	$(RM) $(BACKEND_BIN)
	$(RM) $(FRONTEND_BASH)
