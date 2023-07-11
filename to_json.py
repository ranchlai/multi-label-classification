# -*- coding: utf-8 -*-
import json
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

    new_data = []
    for i in range(len(data)):
        label = data["label"][i]
        "['cs.CV', 'cs.LG']"
        label = label.replace('"', "").replace("'", "")
        label = label.replace("[", "").replace("]", "")
        label = label.split(",")
        label = [l.strip() for l in label]
        label = [l for l in label if l.startswith("cs.")]

        # assert len(label) > 0, f"invalid label: {data['label'][i]}"
        if len(label) == 0:
            continue

        data["label"][i] = label

        new_data.append({"sentence": data["sentence"][i], "label": label})

    with open(ofile, "w") as f:
        json.dump(new_data, f, indent=2)

    print(f"writed {len(data)} lines to {ofile}")
