#!/usr/local/bin/python

import argparse

def read_fasta(path):
    id_seq = {}
    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                id = line.rstrip("\n").split(" ")[0]
                id_seq.setdefault(id, "")
            else:
                id_seq[id] += line.rstrip("\n") 
    return id_seq

def write_fasta(path, id_seq):
    with open(path, "w") as f:
        for k, v in id_seq.items():
            f.write(k + "\n" + v + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True)
    parser.add_argument("-m", "--mode", choices=["remove", "check"], default="check")
    parser.add_argument("-o", "--output", type=str, default=None)
    args = parser.parse_args()

    id_seq = read_fasta(args.input)

    checker = {}

    for id1, seq1 in id_seq.items():
        for id2, seq2 in id_seq.items():
            if id1 == id2:
                continue
            if seq1 == seq2:
                checker[":".join(sorted([id1, id2]))] = seq1

    if args.mode == "check":
        print("-"*10, "check results", "-"*10)
        print(f'The {args.input} has {len(checker)} duplicated')
        for idx, seq in checker.items():
            id1, id2 = map(lambda x: x.lstrip(">"), idx.split(":"))
            print('+'*10)
            print(f'{id1} and {id2} is duplicated. The sequence is below')
            print(seq)

        print("-"*10, "check is done!", "-"*10)
        print("if you would like to remove duplicates, please run this script with mode 'remove'")

    if args.mode == "remove" and args.output is not None:
        remove_keys = list(map(lambda x: x.split(":")[0], checker.keys()))
        print("-"*10, "removing duplicates", "-"*10)
        for k in remove_keys:
            print("removeing", k)
        print("-"*10, "removing duplicates is done!", "-"*10)

        output_idx_seq = {}

        for idx, seq in id_seq.items():
            if idx in remove_keys:
                continue
            output_idx_seq[idx] = seq

        write_fasta(args.output, output_idx_seq)

if __name__ == "__main__":
    main()