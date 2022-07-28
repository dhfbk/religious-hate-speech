import argparse
import numpy as np
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score

accuracy = []
macro_precision = []
macro_recall = []
macro_f1 = []


def compute_score(input_base_filepath, target_dataset, number_of_splits):
    scores = []
    # results/it/alberto.abusive.it.results
    output_filepath = input_base_filepath + ".results"
    output_file = open(output_filepath, "w")

    for i in range(number_of_splits):
        # results/it/alberto.abusive.it.(i+1).out
        pred_filepath = input_base_filepath + "." + str(i+1) + ".out"
        gold_filepath = "machamp/data/it/" + target_dataset + "/test_" + str(i+1) + ".tsv"
        preds = []
        golds = []

        with open(pred_filepath, "r") as f:
            for line in f:
                if len(line) > 2:
                    pred = line.rstrip().split("\t")[0]
                    preds.append(pred)

        with open(gold_filepath, "r") as f:
            for line in f:
                if len(line) > 2:
                    gold = line.rstrip().split("\t")[0]
                    golds.append(gold)

        assert len(golds) == len(preds)
        accuracy.append(accuracy_score(golds, preds))
        macro_precision.append(precision_score(golds, preds, average='macro'))
        macro_recall.append(recall_score(golds, preds, average='macro'))
        macro_f1.append(f1_score(golds, preds, average='macro'))

    mean_acc = round(np.mean(accuracy)*100, 2)
    stddev_acc = round(np.std(accuracy, ddof=1)*100, 1)

    mean_prec = round(np.mean(macro_precision)*100, 2)
    stddev_prec = round(np.std(macro_precision, ddof=1)*100, 1)

    mean_rec = round(np.mean(macro_recall)*100, 2)
    stddev_rec = round(np.std(macro_recall, ddof=1)*100, 1)

    mean_f1 = round(np.mean(macro_f1)*100, 2)
    stddev_f1 = round(np.std(macro_f1, ddof=1)*100, 1)

    output_file.write("macro F1  : " + str(mean_f1) + " +-" + str(stddev_f1) + "\n")
    output_file.write("macro Prec: " + str(mean_prec) + " +-" + str(stddev_prec) + "\n")
    output_file.write("macro Rec : " + str(mean_rec) + " +-" + str(stddev_rec) + "\n")
    output_file.write("macro Acc : " + str(mean_acc) + " +-" + str(stddev_acc) + "\n")

    output_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-I", "--input_base_filepath", type=str, required=True, 
        help="The path to the raw input folder.")
    parser.add_argument("-T", "--target_dataset", type=str, required=True, 
        help="The target dataset name.")
    parser.add_argument("-N", "--number_of_splits", type=int, required=True,
        help="The number of splits.")
    args = parser.parse_args()

    compute_score(args.input_base_filepath, args.target_dataset, args.number_of_splits)
