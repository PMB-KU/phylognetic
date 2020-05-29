import sys

def main():
    arg = sys.argv[1]
    print(arg)

    id_seq = {}
    with open(arg) as f:
        for line in f:
            if line.startswith(">"):
                id = line.rstrip("\n")
                id_seq.setdefault(id, "")
            else:
                id_seq[id] += line.rstrip("\n") 

    for id1, seq1 in id_seq.items():
        for id2, seq2 in id_seq.items():
            if id1 == id2:
                continue
            if seq1 == seq2:
                print(id1, "and", id2, "is duplicated!")


if __name__ == "__main__":
    main()