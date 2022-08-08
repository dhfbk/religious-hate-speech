This repository contains code and data related to the manuscript *"Addressing religious hate online: From taxonomy creation to automated detection"* (currently under review).

## Repository content

- `code/`: this folder contains the code used to run the experiments. Specifically:
  - `baselines-and-ml-models/`: this folder contains a set of notebooks to preprocess data and run experiments using the random and the always abusive/not abusive/religious hate/not religious hate baselines, as well as mulinomial naive Bayes, decision tree, linear support vector classifier, and logistic regression;
  - `pretrained-language-models/`: this folder contains the code to run experiments using BERT, RoBERTa, AlBERTo, UmBERTo, mBERT, and XLM-Roberta.

- `data/`: this folder contains the Italian and English portions of the dataset (in the form of tweet IDs and labels), both aggregated and disaggregated. Specifically:
  - `dataset_en-portion.tsv`: English portion of the dataset in an aggregate form;
  - `dataset_en-portion_raw.tsv`: English portion of the dataset in a disaggregate form;
  - `dataset_it-portion.tsv`: Italian portion of the dataset in an aggregate form;
  - `dataset_it-portion_raw.tsv`: Italian portion of the dataset in a disaggregate form;