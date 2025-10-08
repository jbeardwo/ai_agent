import os
def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)

    abs_working_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        contents = os.listdir(abs_full_path)
        output = ''
        for item in contents:
            cur_path = os.path.join(abs_full_path, item)

            size = os.path.getsize(cur_path)
            is_dir = os.path.isdir(cur_path)

            output += f'- {item}: file_size={size} bytes, is_dir={is_dir}\n'

        return output
    except Exception as e:
        return f"Error:{str(e)}"
