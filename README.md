# Utility for phylogenetic analysis

## Dockerfiles

|tool name||
|---|---|
|trimal|remove not conserved sites in multiple alignment|
|RAxML-ng-mpi|phylognetic analysis by maximum likelihood method|
|Mrbayes|phylognetic analysis by baysian inference|
|gs2|phylogenetic analysis by graph splitting method|

## Workflow

### Maximum Likelihood and Baysian Inference Methods

1. Multiple Alignment (MUSCLE, MAFFT etc.,)
2. Removing not conserved sites (Manual removing or using tools such as trimal)
3. Construct Phylognetic tree (PhyML, RAxML, FastTree, Mrbayes etc.,)
4. Visualization

### Graph Splitting Methods

1. Construct Phylogenetic tree from a raw fasta file (gs2)
2. Visualization

#### Popular tools for visualization

|tool name|type|description|
|---|---|---|
|[FigTree](https://github.com/rambaut/figtree/releases)|Software||
|[Icytree](https://icytree.org)|Web||
|[iToL](https://itol.embl.de)|Web||

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

**example**

run gs container

```bash
docker run --rm -it -v $(pwd):/local_volume gs:latest
```

### trimal

Please read [MANUAL](http://trimal.cgenomics.org/use_of_the_command_line_trimal_v1.2)

**example:**

removing not conserved sites for maximum likelihood method

```bash
# in trimal container
trimal -in seqs.afa -out seqs_trim.afa -automated1
```

### gs2

Please read [github](https://github.com/MotomuMatsui/gs)

**example:**
construct phylogenetic tree with bootstrap and lables

```bash
# in gs container
gs2 -e 1000 -l example/200.faa > 200.nwk
```

### RAxML-ng

Please read [github wiki]()

**example:**
construct phylogenetic tree by maximum likelihood method (ML search + bootsrap) with 8 core cpus

```bash
# in raxml-ng-mpi container
raxml-ng-mpi --msa input.afa --all --model LG+G+I --bs-trees 1000 --threads 8
```

Output file with the extension `.support` is best tree with bootstrap values.

### MrBayes

You should make the nexus format file from multiple alignment fasta.

Please read [MANUAL](https://nbisweden.github.io/MrBayes/manual.html)

**example:** Making nexus format file and run mrbayes with 8 core cpus

```bash
# in utils container

## check duplicates in multiple alignment fasta and removing them
check_duplicates -i seqs_trim.afa -o seqs_remove_duplicates.afa -m remove

## converting fasta to nexus and add mrbayes default parameters
fasta_to_nexus -i seqs_remove_duplicates.afa -o seqs_mrbayes.nex --mrbayes


# run mrbayes in mrbayes container
mpirun --allow-run-as-root -np 8 /MrBayes/src/mb
>MrBayes execute seqs_mrbayes.nex
```

## Reference

1. trimAl: a tool for automated alignment trimming in large-scale phylogenetic analyses Salvador Capella-Gutiérrez, José M. Silla-Martínez and Toni Gabaldón∗ Bioinformatics. 2009 Aug 1;25(15):1972-3.7
2. Frederic Lemoine, Jean-Baka Domelevo Entfellner, Eduan Wilkinson, Damien Correia, Miraine Davila Felipe, Tulio De Oliveira, and Olivier Gascuel, Renewing Felsensteins phylogenetic bootstrap in the era of big data, Nature, 2018
Motomu Matsui and Wataru Iwasaki, Graph Splitting: A Graph-Based Approach for Superfamily-Scale Phylogenetic Tree Reconstruction, Systematic Biology, 2019
3. Alexey M. Kozlov, Diego Darriba, Tomáš Flouri, Benoit Morel, and Alexandros Stamatakis (2019) RAxML-NG: A fast, scalable, and user-friendly tool for maximum likelihood phylogenetic inference. Bioinformatics, btz305 doi:10.1093/bioinformatics/btz305
4. Ronquist, F., M. Teslenko, P. van der Mark, D.L. Ayres, A. Darling, S. Höhna, B. Larget, L. Liu, M.A. Suchard, and J.P. Huelsenbeck. 2012. MRBAYES 3.2: Efficient Bayesian phylogenetic inference and model selection across a large model space. Syst. Biol. 61:539-542.