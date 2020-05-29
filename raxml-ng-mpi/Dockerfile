FROM debian

RUN apt-get update && \
    apt-get install -y wget unzip build-essential pkg-config make gcc cmake openmpi-doc openmpi-bin libopenmpi-dev && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log && \
    mkdir -p /workspace

WORKDIR /workspace

RUN wget https://github.com/amkozlov/raxml-ng/releases/download/0.9.0/raxml-ng_v0.9.0_linux_x86_64_MPI.zip && \
    unzip raxml-ng_v0.9.0_linux_x86_64_MPI.zip

RUN bash install.sh 

ENV PATH=/workspace/bin:$PATH

RUN mkdir -p /local_volume
WORKDIR /local_volume