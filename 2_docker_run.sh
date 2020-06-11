#!/bin/bash

sudo rm -rf "$PWD"/coverage/*

docker run --rm --name eplodn_container -p 127.0.0.1:5005:5005/tcp --env COLLECT_COVERAGE=1  --env PYTHONPATH=/eplodn  --volume "$PWD"/coverage:/coverage --volume "$PWD"/py_packages/app/app:/eplodn/app/ --volume "$PWD"/py_packages/infra/infra:/eplodn/infra/ eplodn_image &

sleep 3
