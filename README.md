[![DOI](https://zenodo.org/badge/516426969.svg)](https://zenodo.org/badge/latestdoi/516426969)

This repository contains code and data related to the paper: 

Ramponi A, Testa B, Tonelli S, Jezek E. 2022. **Addressing religious hate online: from taxonomy creation to automated detection**. *PeerJ Computer Science* 8:e1128 [[cite]](#citation) [[paper]](https://peerj.com/articles/cs-1128/)

## Repository content

- `code/`: this folder contains the code used to run the experiments. Specifically:
  - `baselines-and-ml-models/`: this folder contains a set of notebooks to preprocess data and run experiments using the random and the always abusive/not abusive/religious hate/not religious hate baselines, as well as mulinomial naive Bayes, decision tree, linear support vector classifier, and logistic regression;
  - `pretrained-language-models/`: this folder contains the code to run experiments using BERT, RoBERTa, AlBERTo, UmBERTo, mBERT, and XLM-Roberta.

- `data/`: this folder contains the Italian and English portions of the dataset (in the form of tweet IDs and labels), both aggregated and disaggregated. Specifically:
  - `dataset_en-portion.tsv`: English portion of the dataset in an aggregate form;
  - `dataset_en-portion_raw.tsv`: English portion of the dataset in a disaggregate form;
  - `dataset_it-portion.tsv`: Italian portion of the dataset in an aggregate form;
  - `dataset_it-portion_raw.tsv`: Italian portion of the dataset in a disaggregate form.

## Citation

If you use or build on top of this work, please cite our paper as follows:

```
@article{peerj-cs.1128,
    title={Addressing religious hate online: from taxonomy creation to automated detection},
    author={Ramponi, Alan and Testa, Benedetta and Tonelli, Sara and Jezek, Elisabetta},
    journal={PeerJ Computer Science},
    volume={8},
    pages={e1128},
    year={2022},
    publisher={PeerJ Inc.},
    doi={https://doi.org/10.7717/peerj-cs.1128}
}
```
