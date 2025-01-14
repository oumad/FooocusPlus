import os
import sys
import modules.config as config
from launch import ROOT

paths_checkpoints = config.paths_checkpoints
paths_loras = config.paths_loras
path_embeddings = config.path_embeddings
path_vae_approx = config.path_vae_approx
path_upscale_models = config.path_upscale_models
paths_inpaint = config.paths_inpaint
paths_controlnet = config.paths_controlnet
path_clip_vision = config.path_clip_vision
path_fooocus_expansion = config.path_fooocus_expansion
paths_llms = config.paths_llms
path_outputs = config.path_outputs
path_root = ROOT

def init_module(file_path):
    module_root = os.path.dirname(file_path)
    sys.path.append(module_root)
    module_name = os.path.relpath(module_root, os.path.dirname(os.path.abspath(__file__)))
    print(f'[{module_name}] The customized module:{module_name} is initializing...')
    return module_name, module_root

