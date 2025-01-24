import os
import sys
from common import ROOT

sys.path.append(ROOT)
os.chdir(ROOT)

print('Loading FooocusPlus without updating...')

#if __name__ == '__main__':
#    import multiprocessing as mp
#    mp.set_start_method('spawn')

from launch import *
