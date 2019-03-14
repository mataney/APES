# APES

This repository is an implementation of the summaries evaluation metric presented in Question Answering as an Automatic Evaluation Metric for News Article Summarization [link](link)

## preprocessing

First, run:

`python create_questions_mapping.py --cnn_questions_path path/to/cnn.tgz --dm_questions_path path/to/cnn.tgz`

This script creates a a pickle with a mapping from an article hash to its respective entities mapping (entity name to entity number), and questions.

# run

Then run both APES and ROUGE on your generated summaries. An example of a small subset of the CNN\Daily Mail:

`python run.py --preds_file testdata/test.txt.pred --targets_file testdata/test.txt.tgt --questions_mapping_path ./questions_data.pkl --filenames_path ./filenames/filenames-test.txt`

Filenames hold the mapping from CNN\Dail Mail article id to its hash.