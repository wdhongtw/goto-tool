BIN_DIR = $(HOME)/.local/bin

BACKEND_SRC = $(abspath backend.py)
BACKEND_BIN = $(BIN_DIR)/_goto_backend

.PHONY: install uninstall

install:
	mkdir -p "$(BIN_DIR)"
	ln -s "$(BACKEND_SRC)" "$(BACKEND_BIN)"

uninstall:
	$(RM) $(BACKEND_BIN)
