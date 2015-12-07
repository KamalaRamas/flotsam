FROM golang
# Modified from https://github.com/docker-library/golang/tree/master/1.4/onbuild

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

# this will be built below. go-wrapper is from golang.
CMD ["go-wrapper", "run"]

RUN apt-get update && apt-get install -y \
  iptables \
  unzip \
  wget \
  curl

RUN curl -L https://github.com/coreos/etcd/releases/download/v2.2.2/etcd-v2.2.2-linux-amd64.tar.gz -o etcd-v2.2.2-linux-amd64.tar.gz -O /tmp/etcd.zip
RUN mkdir -p /tmp/etcd-unzip
RUN unzip /tmp/etcd -d /tmp/etcd-unzip/
RUN mv /tmp/etcd-unzip/*/* /go/src/app/
RUN go-wrapper download
RUN go-wrapper install
