# -*- coding: utf-8 -*-
import sys

import pandas as pd

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python to_json.py <input_file> <output_file>")
        sys.exit(1)

    ifile = sys.argv[1]
    ofile = sys.argv[2]

    # read csv file, ignore error lines
    data = pd.read_csv(ifile, error_bad_lines=False)

    # replace summaries to sentence, terms to label
    data = data.rename(columns={"summaries": "sentence", "terms": "label"})

    for i in range(len(data)):
        label = data["label"][i]
        "['cs.CV', 'cs.LG']"
        label = label.replace('"', "").replace("'", "")
        label = label.replace("[", "").replace("]", "")
        label = label.split(",")
        label = [l.strip() for l in label]

        data["label"][i] = label

    data.to_json(ofile, orient="records", indent=2)

    print(f"writed {len(data)} lines to {ofile}")
