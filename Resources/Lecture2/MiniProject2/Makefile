MOUNT=/mnt/local
IMAGE=my_docker

build_docker:
	docker build -t ${IMAGE}  .

run_docker:
	docker run \
	--mount type=bind,source=${PWD},target=${MOUNT} \
	-it "${IMAGE}" /bin/bash

clean_docker:
	docker rm  $$(docker ps -q -a)
	docker image prune -a
