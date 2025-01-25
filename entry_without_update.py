import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)
os.chdir(ROOT)

print('Loading FooocusPlus without updating...')

#if __name__ == '__main__':
#    import multiprocessing as mp
#    mp.set_start_method('spawn')

from launch import *
