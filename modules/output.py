from modules.util import get_output_folder
from modules.auth import get_current_user

def save_image(image, filename):
    output_path = get_output_folder()
    image.save(os.path.join(output_path, filename))