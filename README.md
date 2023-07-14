# Multi-label classification using huggingface transformers and Reuters dataset

This is a simple example of multi-label classification using huggingface transformers and[ Reuters-21578](https://huggingface.co/datasets/reuters21578) dataset.

## Model
We can use any of the huggingface transformers models for multi-label classification, as long as the model supports multi-label classification. For example, we can use the `bert-base-uncased` model. The model is available in the `model_name_or_path` parameter.

## Data processing
Following from the paper[1], we can use the ModApte split of Reuters-21578 dataset. The dataset is available in the huggingface datasets library. The dataset is split into train, validation and test sets. The train and validation sets are further split into train and validation sets. The splits are available in the `dataset_config_name` parameter. The splits are as follows:
```bash
python process.py ModApte
```

Now you can simply train the model using the following command:
```bash
./train.sh ModApte
```

## Results
The following table shows the
Micro F1 score on test set for different splits of Reuters-21578 dataset.
| Config | # train |  # val | # test | # labels | Micro F1 (val) |Micro F1 (test)|
|--------|---------|--------|--------|----------|----------------|---------------|
| ModApte | 6947    | 772   | 3016   | 90    | 0.875    | 0.870 |
| ModHayes | 9608    | 1068   | 563   | 75    |  0.9233   | 0.8005 |
| ModLewis | 6951    | 773   | 3019   | 90    |  0.884   |  |




## Training on raw dataset
You can also train the model on the raw dataset. The raw dataset is available in the `dataset_name` parameter.
But the raw dataset contains empty labels and empty text. Further,the text and title are in different columns.
 So we recommend to first process the dataset using the `process.py` script, as shown above.
```bash
python run_glue.py \
  --model_name_or_path bert-base-uncased \
  --dataset_name reuters21578  \
  --dataset_config_name ModApte \
  --label_column_name topics \
  --text_column_name text \
  --do_train \
  --do_eval \
  --no_pad_to_max_length \
  --do_predict \
  --max_seq_length 512 \
  --per_device_train_batch_size 8 \
  --learning_rate 2e-5 \
  --num_train_epochs 15 \
  --output_dir ./outputs/ \
  --save_steps 2000 \
  --save_total_limit 1 \
  --overwrite_output_dir
```


## References
- [1] Yiming Yang and Xin Liu. 1999. A re-examination of text categorization methods. In Proceedings of the 22nd annual international ACM SIGIR conference on Research and development in information retrieval (SIGIR '99). Association for Computing Machinery, New York, NY, USA, 42–49. https://doi.org/10.1145/312624.312647
