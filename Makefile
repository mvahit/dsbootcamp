# GITHUB


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

req:
	pip freeze > requirements.txt

compush: commit push