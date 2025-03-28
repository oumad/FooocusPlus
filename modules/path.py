import os
from modules.auth import get_current_user  # Importe la fonction qui donne l'utilisateur connecté

def get_output_path():
    user = get_current_user()
    return os.path.join("Outputs", user)
