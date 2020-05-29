FROM debian

RUN apt-get update && \
    apt-get install -y git build-essential pkg-config make && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log && \
    mkdir -p /workspace /local_volume 

WORKDIR /workspace

RUN git clone https://github.com/scapella/trimal.git 

WORKDIR /workspace/trimal/source

RUN make

WORKDIR /local_volume

ENV PATH=/workspace/trimal/source:$PATH
