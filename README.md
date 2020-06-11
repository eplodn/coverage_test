# coverage_test

This project aims to show how coverage.py can be used for the coverage of python apps running in Docker containers.

There are two Python packages: `infra` and `app`. `app` is a Flask app that calls code from `infra`.

How to run:

 - git clone
 - run `1.sh` to build a Docker image with the app inside.
 - run `2.sh` to run the Docker container based on the image.
 - run `3.sh` to issue calls to application inside the Docker container.
 - run `4.sh` to stop the Docker container and create coverage reports.
 - run `5.sh` to combine coverage reports into one report.
 
 
