python run_glue.py \
    --model_name_or_path bert-base-uncased \
    --do_train \
    --do_eval \
    --do_predict \
    --train_file ./data/tiny.json \
    --validation_file ./data/tiny.json \
    --test_file ./data/tiny.json \
    --max_seq_length 256 \
    --learning_rate 1e-5 \
    --num_train_epochs 400.0 \
    --output_dir ./tmp/glue \
    --overwrite_output_dir \
    --per_device_train_batch_size 16 \
    --save_total_limit 1 \