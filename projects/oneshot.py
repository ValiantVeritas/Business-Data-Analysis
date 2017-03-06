import os
import numpy as np 
from scipy.ndimage import imread
from scipy.spatial.distance import cdist


nrun = 20
path_to_script_dir = os.path.dirname(os.path.realpath(_file_))
path_to_all_runs = os.path.join(path_to_script_dir, 'all_runs')
fname_label = 'class_labels.txt'

def classification_run(folder, f_cost, ftype='cost')
	assert ftype in {'cost', 'score'}
	with open(os.path.join(path_to_all_runs, folder, fname_label)) as f:
		pairs = [line.split() for line in f.readlines()]
		test_files, train_files = zip(*pairs)

	answers_file = list(train_files)
	test_files = sorted(test_files)
	train_files = sorted(train_files)
	n_train  len(train_files)
	n_test = len(test_files)

	train_items = [f_load(os.path.joun(path_to_all_runs, f)) for f in train_files]

	test_items = [f_load(os.path.join(path_to_all_runs, f)) for f in test_files]

	costM = npzeros((n_test, n_train))
	for i, test_i in enumerate(train_items):
		for j, train_j in enumerate(train_files):
			costM[i, j] =  f_cost(test_i, train_j)
		if ftype == 'cost':
			y_hats = np.argmin(costM, axis=1)
		elif ftype == 'score':
			y_hats = np.argmax(costM, axis=1)
		else:
			raise ValueError('Unexpected ftype: {}'.format(ftype))
		correct = len([1 for y_hat, answer in zip(y_hats, answers_file)])