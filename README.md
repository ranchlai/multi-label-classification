# multi-label-classification
multi-label-classification using huggingface transformers

# Data preparation
Download the data by
```bash
wget https://github.com/soumik12345/multi-label-text-classification/releases/download/v0.2/arxiv_data.csv -P ./data/
```
Convert to data to json

```bash
python to_json.py ./data/arxiv_data.csv ./data/arxiv_data.json
```

plit to train and val
```bash
python split_data.py ./data/arxiv_data.json ./data/
```

The data should be in the following json(or jsonl) format:
```json
[
 {
  "sentence": "Recent advances in deep learning have enabled the development of automated\nframeworks for analysing medical images ....",
  "label": ["cs.CV","cs.LG"]
 },
 {
  "sentence": "Methods for object detection and segmentation rely on ...",
  "label": ["cs.CV"]
 }
]
```

## Training

```
python run_glue.py \
    --model_name_or_path bert-base-uncased \
    --do_train \
    --do_eval \
    --train_file ./data/train.json \
    --validation_file ./data/val.json \
    --max_seq_length 128 \
    --learning_rate 2e-5 \
    --num_train_epochs 100.0 \
    --output_dir /tmp/glue \
    --overwrite_output_dir \
    --per_device_train_batch_size 2 \
    --push_to_hub false \
```

## Fast checking
To check that the repo is working fine, run the following command
```
bash fast_check.sh
```
It will load a [tiny](./data/tiny.json) dataset and run the training and validation for 400 epochs
The final eval accuracy should be around 1.0 and the prediciton file will will located at `./tmp/predict_results_None.txt `
