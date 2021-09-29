# trebor_sux

FROM python:rc-bullseye

MAINTAINER Sean Jain Ellis <sellis@bandarji.com>

# ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get update
# RUN apt-get --yes --force-yes install kmod kbd

RUN pip install --upgrade pip
RUN pip install blessed pybraille

WORKDIR /treborsux

# ENTRYPOINT ["python", "/treborsux/game.py"]
ENTRYPOINT ["/bin/bash"]
