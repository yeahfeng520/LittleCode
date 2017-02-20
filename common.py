# coding=utf-8

import sys
import numpy as np

def read_sparse_data(fp_data):
	X, Y = list(), list()

	for line in fp_data:
		line_arr = line.strip().split()
		Y.append(line_arr[0])
		x = list()
		for kv in line_arr[1 : ]:
			k, v = kv.split(':')
			x.append([k, float(v)])
		X.append(x)

	return X, Y