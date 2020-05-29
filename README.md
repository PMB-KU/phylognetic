# Utility for phylogenetic analysis

## Dockerfiles

|tool name||
|---|---|
|trimal|remove not conserved sites in multiple alignment|
|RAxML-ng-mpi|phylognetic analysis by maximum likelihood method|
|gs2|phylogenetic analysis by graph splitting method|

## Usage

### general

#### build

```bash
docker build -t container_name:version container_directory
```

**example**

building gs image

```bash
docker build -t gs:latest ./gs
```

#### run

```bash
docker run --rm -it -v $(pwd):/local_volume container_name
```

### trimal

Please read [MANUAL](http://trimal.cgenomics.org/use_of_the_command_line_trimal_v1.2)

**example:**

to construct phylogenetic tree by maximum likelihood method

```bash
trimal -in seqs.afa -out seqs_trim.afa -automated1
```

### gs2

Please read [github](https://github.com/MotomuMatsui/gs)

**example:**
construct phylogenetic tree with bootstrap and lables

```
gs2 -e 1000 -l example/200.faa > 200.nwk
```

### RAxML-ng

Please read [github wiki]()

**example:**
construct phylogenetic tree by maximum likelihood method (ML search + bootsrap) with 8 core cpus

```
raxml-ng-mpi --msa input.afa --all --model LG+G+I --bs-trees 1000 --threads 8
```

Outputfile with the extension `.support` is besttree with bootstrap values.

## Reference

1. trimAl: a tool for automated alignment trimming in large-scale phylogenetic analyses Salvador Capella-Gutiérrez, José M. Silla-Martínez and Toni Gabaldón∗ Bioinformatics. 2009 Aug 1;25(15):1972-3.7
2. Frederic Lemoine, Jean-Baka Domelevo Entfellner, Eduan Wilkinson, Damien Correia, Miraine Davila Felipe, Tulio De Oliveira, and Olivier Gascuel, Renewing Felsensteins phylogenetic bootstrap in the era of big data, Nature, 2018
Motomu Matsui and Wataru Iwasaki, Graph Splitting: A Graph-Based Approach for Superfamily-Scale Phylogenetic Tree Reconstruction, Systematic Biology, 2019
3. Alexey M. Kozlov, Diego Darriba, Tomáš Flouri, Benoit Morel, and Alexandros Stamatakis (2019) RAxML-NG: A fast, scalable, and user-friendly tool for maximum likelihood phylogenetic inference. Bioinformatics, btz305 doi:10.1093/bioinformatics/btz305