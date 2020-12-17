################################
# GITHUB
################################

commit:
	git commit -am "commit from make file"

push:
	git push origin main

pull:
	git pull origin main

fetch:
	git fetch origin main

reset:
	rm -f .git/index
	git reset

compush: commit push


################################
# PYPI
################################
versionup:


sdist:
	python setup.py sdist

upload:
	twine upload dist/*