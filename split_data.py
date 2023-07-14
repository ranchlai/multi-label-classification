# -*- coding: utf-8 -*-

import json
import os
import random
import sys

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python split_data.py <input_file>  <output_dir>")
        sys.exit(1)

    random.seed(42)
    ifile = sys.argv[1]
    odir = sys.argv[2]
    os.makedirs(odir, exist_ok=True)
    data = json.load(open(ifile))
    random.shuffle(data)
    n = len(data)
    ntrain = int(n * 0.8)

    train = data[:ntrain]
    val = data[ntrain:]

    with open(os.path.join(odir, "train.json"), "w") as f:
        json.dump(train, f, indent=1)

    with open(os.path.join(odir, "val.json"), "w") as f:
        json.dump(val, f, indent=1)

    print(f"train: {len(train)} lines, val: {len(val)} lines")
    print("done")
