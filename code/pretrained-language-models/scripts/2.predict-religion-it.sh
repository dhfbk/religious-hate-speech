declare -a PRETRAINED_MODELS=("alberto" "umberto" "mbert" "xlm")
declare -a DATASETS=("religion")
declare -a SPLIT_IDS=("1" "2" "3" "4" "5")

RESULTS_FOLDER="results_rel"
LANG_RESULTS_FOLDER="results_rel/it"
TEST_DATA_FOLDER="machamp/data/it"
LANG="it"


for PRETRAINED_MODEL in "${PRETRAINED_MODELS[@]}"
do
    for SOURCE_DATASET in "${DATASETS[@]}"
    do
        for SPLIT_ID in "${SPLIT_IDS[@]}"
        do
            # alberto.abusive.it.3
            MODEL_NAME=$PRETRAINED_MODEL.$SOURCE_DATASET.$LANG.$SPLIT_ID
            MODEL_FILEPATH=$(ls -td logs/$MODEL_NAME/*/ | head -1)

            echo "Testing '$MODEL_NAME' on '$SOURCE_DATASET'..."
            python machamp/predict.py \
                $MODEL_FILEPATH/model.tar.gz \
                $TEST_DATA_FOLDER/$SOURCE_DATASET/test_$SPLIT_ID.tsv \
                $LANG_RESULTS_FOLDER/$MODEL_NAME.out \
                --device 0
            echo "==> Done."
            # results/it/alberto.abusive.it.3.out
        done

        # alberto.abusive.it [.3.out]
        CURR_BASE_MODEL_NAME=$PRETRAINED_MODEL.$SOURCE_DATASET.$LANG
        # # results/it/alberto.abusive.it
        CURR_BASE_FILEPATH=$LANG_RESULTS_FOLDER/$CURR_BASE_MODEL_NAME
        python scripts/compute_avg_scores_religion_it.py -I $CURR_BASE_FILEPATH -T $SOURCE_DATASET -N 5
    done
done