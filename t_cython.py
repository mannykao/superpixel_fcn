#from third_party.cython.build.libwin-amd64-3.8 import connectivity

#import sys
#sys.path.append('./third_party/cython/build/lib.win-amd64-3.8')

# cd third_party/cython
# instead of 'python setup.py install --user'
#   pip install .
#
import argparse, pprint

from train_util import *
import models

def ourArgs():
	parser = argparse.ArgumentParser(description='PyTorch SPixelNet inference on a folder of imgs',
	                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('--data_dir', metavar='DIR', default='./demo/inputs', help='path to images folder')
	parser.add_argument('--data_suffix',  default='jpg', help='suffix of the testing image')
	parser.add_argument('--pretrained', metavar='PTH', help='path to pre-trained model',
	                                    default= './pretrain_ckpt/SpixelNet_bsd_ckpt.tar')
	parser.add_argument('--output', metavar='DIR', default= './demo' , help='path to output folder')

	parser.add_argument('--downsize', default=16, type=float,help='superpixel grid cell, must be same as training setting')

	parser.add_argument('-nw', '--num_threads', default=1, type=int,  help='num_threads')
	parser.add_argument('-b', '--batch-size', default=1, type=int, metavar='N', help='mini-batch size')

	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = ourArgs()
	pp = pprint.PrettyPrinter(indent=1, width=120)
	#pp.pprint(models.__dict__)

	print(models.__dict__.keys())

	print(f"{args.pretrained=}")
	pretrained = args.pretrained

	network_data = torch.load(pretrained)

	modelname = network_data['arch']	#'SpixelNet1l_bn'
	print(f"{network_data['arch']=}")	#'SpixelNet1l_bn'
	print(f"=> using pre-trained model '{modelname}'")
