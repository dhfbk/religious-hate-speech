# Training.

# Variables declaration
declare -a PRETRAINED_MODELS=("mbert" "xlm" "alberto" "umberto" "bert" "roberta")
declare -a DATASETS=("religion")
declare -a SPLITS=("1" "2" "3" "4" "5")

for MODEL in "${PRETRAINED_MODELS[@]}"
do
    for DATASET in "${DATASETS[@]}"
    do
        for SPLIT in "${SPLITS[@]}"
        do
            python machamp/train.py \
                --dataset_config machamp/configs/$DATASET.iten.$SPLIT.json \
                --parameters_config machamp/configs/params.$MODEL.json \
                --name $MODEL.$DATASET.iten.$SPLIT \
                --device -0
        done
    done
done