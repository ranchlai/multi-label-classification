# -*- coding: utf-8 -*-
import json
import os
import random
import sys

from datasets import load_dataset


def get_label_text(dataset, split="train"):
    label_list = []
    data = []
    for label, text, title in zip(
        dataset[split]["topics"], dataset[split]["text"], dataset[split]["title"]
    ):
        if len(label) == 0:
            continue
        data.append({"sentence": title + text, "label": label})
        label_list += label
    label_list = list(set(label_list))
    return data, label_list


def remove_unlabeled(data, labels):
    new_data = []
    for d in data:
        is_valid = True
        for label in d["label"]:
            if label not in labels:
                is_valid = False
                break
        if is_valid:
            new_data.append(d)
    return new_data


if __name__ == "__main__":
    random.seed(42)
    if len(sys.argv) != 2:
        print("Usage: python process_ModApte.py [ModApte|ModHayes|ModLewis]")
        exit(1)
    config = sys.argv[1]
    assert config in [
        "ModApte",
        "ModHayes",
        "ModLewis",
    ], "config should be one of ModApte, ModHayes, ModLewis"

    dataset = load_dataset("reuters21578", config)
    train_data, train_label_list = get_label_text(dataset, "train")
    test_data, test_label_list = get_label_text(dataset, "test")
    labels = set(train_label_list) & set(test_label_list)

    print(labels)
    print(f"there are {len(labels)} labels")

    new_train = remove_unlabeled(train_data, labels)
    new_test = remove_unlabeled(test_data, labels)

    # split the data into train and valiation
    ntrain = int(len(new_train) * 0.9)
    os.makedirs(f"./data/{config}", exist_ok=True)

    train_file = f"./data/{config}/train.json"
    with open(train_file, "w") as f:
        json.dump(new_train[:ntrain], f, indent=4)
        print(f"there are {len(new_train[:ntrain])} train data")
        print("save train data to {}".format(train_file))

    val_file = f"./data/{config}/val.json"
    with open(val_file, "w") as f:
        json.dump(new_train[ntrain:], f, indent=4)
        print(f"there are {len(new_train[ntrain:])} val data")
        print("save train data to {}".format(val_file))

    test_file = f"./data/{config}/test.json"
    with open(test_file, "w") as f:
        json.dump(new_test, f, indent=4)
        print(f"there are {len(new_test)} test data")
        print("save train data to {}".format(test_file))
