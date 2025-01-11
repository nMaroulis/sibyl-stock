FROM ubuntu:latest
LABEL authors="nick_maroulis"

ENTRYPOINT ["top", "-b"]