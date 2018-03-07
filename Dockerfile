FROM alpine:edge

MAINTAINER <Gao.Ge> me@youyaochi.me

RUN mkdir -p /code
WORKDIR /code
EXPOSE 5000

COPY requirements.txt /code
RUN apk add --no-cache python3 \
                       python3-dev \
                       build-base \
                       git && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
	pip3 install --no-cache-dir -r /code/requirements.txt && \
	apk del python3-dev \
            build-base \
            git && \
    rm -r /root/.cache

COPY . /code/
CMD ["/usr/bin/python3", "run.py"]
