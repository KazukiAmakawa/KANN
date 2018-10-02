include tmp
t=1
p=0

main:
	@python3 main.py -t ${p} ${t}

test:
	@python3 main.py -t ${p} ${t}

cinit:
	@python3 main.py -ci ${p} ${t}

ctest:
	./cpptest ${ModelFolder}/model.dumped ${TestFolder}/tmp  ${OutputFolder}/Result.out
	rm -rf ${ModelFolder}/model.dumped
	rm -rf ${TestFolder}/tmp

train:
	@python3 main.py -l ${p} ${t}

clean:
	@bash clean.sh

help:
	@sh help.sh

install:
	@python3 main.py -i ${p} ${t}

set:
	@vi Setting.py

