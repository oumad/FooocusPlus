from modules.util import get_output_folder
from modules.auth import get_current_user
from gradio import Error
from modules.path import get_user_output_path, get_output_directory
import json
import os

def auth_required(fn):
    def wrapper(*args, **kwargs):
        if not get_current_user():
            raise Error("Authentication required")
        return fn(*args, **kwargs)
    return wrapper

@auth_required
def save_image(image, metadata):
    output_dir = get_output_directory()
    filename = generate_unique_filename()
    full_path = os.path.join(output_dir, filename)
    
    # Sauvegarde de l'image
    image.save(full_path)
    
    # Sauvegarde des métadonnées
    with open(os.path.join(output_dir, "metadata.json"), "a") as f:
        json.dump(metadata, f)
    
    return full_path