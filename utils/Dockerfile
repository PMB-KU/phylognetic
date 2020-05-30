FROM python:3.8.0


RUN pip install -U pip && \
    pip install biopython && \
    mkdir -p /local_volume /workspace

ADD . /workspace
ENV PATH=/workspace:$PATH

RUN ln /workspace/check_duplicate.py /workspace/check_duplicate && \
    ln /workspace/fasta_to_nexus.py /workspace/fasta_to_nexus

