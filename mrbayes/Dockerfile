FROM debian

RUN apt-get update && \
    apt-get install -y autoconf \
        g++ \
        git \
        libreadline-dev \
        libtool \
        make \
        ocl-icd-opencl-dev \
        pocl-opencl-icd \
        libopenmpi-dev && \
    git clone --depth=1 https://github.com/beagle-dev/beagle-lib.git && \
    git clone --depth=1 --branch=develop https://github.com/NBISweden/MrBayes.git && \
    mkdir -p /local_volume 


WORKDIR /beagle-lib

RUN ./autogen.sh && \
    ./configure --without-jdk LDFLAGS=Wl,-rpath=/usr/local/lib && \
    make -j2 && \
    make install

WORKDIR /MrBayes

RUN ./configure --with mpi && \
    make -j2

WORKDIR /local_volume