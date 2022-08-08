This folder contains the code to run experiments using BERT, RoBERTa, AlBERTo, UmBERTo, mBERT, and XLM-Roberta. Specifically, from this folder you can run the following scripts for training/evaluating models:

Training:
- `sh scripts/1.train-abusive-en.sh`: train pretrained language models on the abusive language detection task on English data;
- `sh scripts/1.train-abusive-it.sh`: train pretrained language models on the abusive language detection task on Italian data;
- `sh scripts/1.train-abusive-iten.sh`: train pretrained language models on the abusive language detection task on both English and Italian data;
- `sh scripts/1.train-religion-en.sh`: train pretrained language models on the religious hate speech detection task on English data;
- `sh scripts/1.train-religion-it.sh`: train pretrained language models on the religious hate speech detection task on Italian data;
- `sh scripts/1.train-religion-iten.sh`: train pretrained language models on the religious hate speech  detection task on both English and Italian data.

Prediction and evaluation:
- `sh scripts/2.predict-abusive-en`: predict and evaluate pretrained language models trained on English data for the abusive language detection task;
- `sh scripts/2.predict-abusive-it`: predict and evaluate pretrained language models trained on Italian data for the abusive language detection task;
- `sh scripts/2.predict-religion-en`: predict and evaluate pretrained language models trained on English data for the religious hate speech detection task;
- `sh scripts/2.predict-religion-it`: predict and evaluate pretrained language models trained on Italian data for the religious hate speech detection task;
- `sh scripts/2.predict-abusive-cross-iten-to-en`: predict and evaluate cross-lingual pretrained language models trained on Italian and English data for the abusive language detection task, and test them on English data;
- `sh scripts/2.predict-abusive-cross-iten-to-it`: predict and evaluate cross-lingual pretrained language models trained on Italian and English data for the abusive language detection task, and test them on Italian data;
- `sh scripts/2.predict-abusive-zeroshot-en-to-it`: zero-shot prediction and evaluation of pretrained language models trained on English data for the abusive language detection task, and tested on Italian data;
- `sh scripts/2.predict-abusive-zeroshot-it-to-en`: zero-shot prediction and evaluation of pretrained language models trained on Italian data for the abusive language detection task, and tested on English data;
- `sh scripts/2.predict-religion-zeroshot-en-to-it`: zero-shot prediction and evaluation of pretrained language models trained on English data for the religious hate speech detection task, and tested on Italian data;
- `sh scripts/2.predict-religion-zeroshot-it-to-en`: zero-shot prediction and evaluation of pretrained language models trained on Italian data for the religious hate speech detection task, and tested on English data.