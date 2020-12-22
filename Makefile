build:
	rm -f dist/*
	python3 setup.py sdist 
upload:
	twine upload dist/*

.PHONY: build upload