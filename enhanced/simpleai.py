import os
import sys
import gradio as gr
import args_manager
from simpleai_base import simpleai_base, utils, comfyd, torch_version, xformers_version, cuda_version, comfyclient_pipeline
from simpleai_base.params_mapper import ComfyTaskParams
from simpleai_base.models_info import ModelsInfo, sync_model_info
from launch import MODELSINFO
from build_launcher import is_win32_standalone_build

args_comfyd = [[]]
modelsinfo_filename = 'models_info.json'

def init_modelsinfo(models_root, path_map):
    global modelsinfo_filename
    global MODELSINFO
    models_info_path = os.path.abspath(os.path.join(models_root, modelsinfo_filename))
    if not MODELSINFO:
        MODELSINFO = ModelsInfo(models_info_path, path_map)
    return MODELSINFO

