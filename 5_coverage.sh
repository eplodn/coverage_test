#!/bin/bash
cd coverage
python3.6 -m coverage combine
python3.6 -m coverage report -m -i

