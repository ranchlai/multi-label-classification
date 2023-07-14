fconfig=$1
if [ -z "$config" ]
then
    echo "Please provide a config name [ModApte|ModHayes|ModLewis]"
    exit 1
fi
model=bert-base-uncased
python run_glue.py \
    --model_name_or_path $model \
    --do_train \
    --do_eval \
    --train_file ./data/$config/train.json \
    --validation_file ./data/$config/val.json \
    --max_seq_length 256 \
    --learning_rate 2e-5 \
    --num_train_epochs 15.0 \
    --output_dir ./outputs-$model-$config \
    --overwrite_output_dir \
    --per_device_train_batch_size 8 \
    --save_total_limit 1 \
    --save_steps 2000 \
