# APES

This repository is an implementation of the summaries evaluation metric presented in [Question Answering as an Automatic Evaluation Metric for News Article Summarization](https://www.aclweb.org/anthology/N19-1395).
A Trained QA model on which we evaluate our generated summaries can be found in [here](https://github.com/mataney/rc-cnn-dailymail). (Notice these have different python versions so different environments are required) 

## preprocessing

First, run:

`python create_questions_mapping.py --cnn_questions_path path/to/cnn.tgz --dm_questions_path path/to/cnn.tgz`

This script creates a a pickle with a mapping from an article hash to its respective entities mapping (entity name to entity number), and questions.

# run

Then run both APES and ROUGE on your generated summaries. An example of a small subset of the CNN\Daily Mail:

`python run.py --preds_file testdata/test.txt.pred --targets_file testdata/test.txt.tgt --questions_mapping_path ./questions_data.pkl --filenames_path ./filenames/filenames-test.txt`

Filenames hold the mapping from CNN\Dail Mail article id to its hash.

# Citation

@inproceedings{eyal-etal-2019-question,
    title = "Question Answering as an Automatic Evaluation Metric for News Article Summarization",
    author = "Eyal, Matan  and
      Baumel, Tal  and
      Elhadad, Michael",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = jun,
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/N19-1395",
    pages = "3938--3948",
}
