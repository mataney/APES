import os

from utils import summaries_to_rouge_format, delete_dir

def rouge(preds_file, targets_file):
	temp_targets_dir, temp_preds_dir = './temp_targets/', './temp_preds/'
	summaries_to_rouge_format(targets_file, temp_targets_dir, "targets")
	summaries_to_rouge_format(preds_file, temp_preds_dir, "preds")

	os.system("""python -m rouge.rouge \
	           --target_filepattern={}*.targets \
	           --prediction_filepattern={}*.preds \
	           --output_filename=rouge_scores.csv""".format(temp_targets_dir, temp_preds_dir))

	delete_dir(temp_targets_dir)
	delete_dir(temp_preds_dir)