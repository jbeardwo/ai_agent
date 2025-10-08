import os
def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)

    abs_working_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    directory = os.path.dirname(abs_full_path)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        with open(abs_full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'         

    except Exception as e:
        return f"Error: {str(e)}"

