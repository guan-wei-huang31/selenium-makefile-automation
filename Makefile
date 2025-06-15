#  Python venv
VENV_PY = ./venv/Scripts/python.exe

.PHONY: test report clean

test:
	@echo "Testing Start"
	@$(VENV_PY) -m pytest -v navbar_testing.py download_testing.py --junitxml=report.xml
	@status=$$?; \
	if [ $$status -eq 0 ]; then \
		echo "Test passed!"; \
	else \
		echo "Test Failed. Exit code: $$status"; \
	fi; \
	exit $$status

report:
	cat report.xml

clean:
	rm -f report.xml
