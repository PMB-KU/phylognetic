#!/usr/local/bin/python

import argparse
import os

from Bio import SeqIO, Nexus, Alphabet


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True)
    parser.add_argument("-o", "--output", type=str, default=None)
    parser.add_argument("--mrbayes", action='store_true')
    args = parser.parse_args()

    if args.output is None:
        output_path = args.input.split(".")[0] + ".nex"
    else:
        output_path = args.output

    SeqIO.convert(args.input, 'fasta', output_path, "nexus", alphabet=Alphabet.IUPAC.protein)

    mrbayes_parameter = \
        [
        "begin mrbayes;",
        "log start append;",
        "set autoclose=no nowarn=yes;",
        "lset rates=invgamma ngammacat=4;",
        "prset aamodelpr=mixed;",
        "mcmc starttree=random ngen=11000000 nruns=2 nchains=4 temp=0.2 printfreq=1000 samplefreq=200 relburnin=yes burninfrac=0.25 savebrlens=yes mcmcdiagn=yes diagnfreq=50000 stoprule=yes stopval=0.01;",
        "sump;",
        "sumt;",
        "log stop;",
        "end;",
        ]

    if args.mrbayes:
        with open(output_path, 'r') as f:
            lines = f.readlines()
        lines.append("\n".join(mrbayes_parameter))
        with open(output_path, 'w') as f:
            f.write("".join(lines))

if __name__ == "__main__":
    main()