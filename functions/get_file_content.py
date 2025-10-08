import os
from .config import MAX_FILE_CHARS
def get_file_content(working_directory, file_path):

    full_path = os.path.join(working_directory, file_path)

    abs_working_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_full_path, "r") as f:
            file_content_string = f.read(MAX_FILE_CHARS + 1)
        if len(file_content_string) > MAX_FILE_CHARS:
            file_content_string = f'{file_content_string[:MAX_FILE_CHARS]} [...File "{file_path}" truncated at {MAX_FILE_CHARS} characters]'

        return file_content_string

    except Exception as e:
        return f"Error: {str(e)}"


