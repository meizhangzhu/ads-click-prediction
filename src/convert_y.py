with open("valid_trn.dat") as fin, open("valid_trn_converted.dat", "w+") as fout:
    for line in fin.readlines():
        if line.strip() != "":
            elements = line.strip().split(" ")
            y = elements[0]
            x = elements[1:]
            y = "1" if y == "1" else "-1"
            fout.write("{} {}\n".format(y, " ".join(x)))

with open("valid_tst.dat") as fin, open("valid_tst_converted.dat", "w+") as fout:
    for line in fin.readlines():
        if line.strip() != "":
            elements = line.strip().split(" ")
            y = elements[0]
            x = elements[1:]
            y = "1" if y == "1" else "-1"
            fout.write("{} {}\n".format(y, " ".join(x)))
