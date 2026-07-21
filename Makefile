VENV=.venv
PYTHON=$(VENV)/bin/python3
PIP=$(VENV)/bin/pip

install:
	@echo "Setting up virtal environement..."
	@test -f $(VENV) || python3 -m venv $(VENV)
	@echo "Install dependencies..."
	$(PIP) install -r requirements.txt 

run:
	$(PYTHON) fly-in.py

debug:
	$(PYTHON) -m pdb fly-in.py

clean:
	find . -name "__pycache__" -type d -exec rm -rd {} +
	find . -name "mypy_cache" -type d -exec rm -rd {} +
	find . -name "*:Zone.Identifier" -type f -delete

lint:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports \
	 --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(PYTHON) -m flake8 .
	$(PYTHON) -m mypy --strict .