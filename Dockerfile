FROM python:slim
MAINTAINER Sean Jain Ellis <sellis@bandarji.com>

RUN pip install pytest pylint

ENV EXAMPLE_ENVVAR="howdy"

