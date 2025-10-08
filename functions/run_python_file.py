import os
import subprocess

from pydantic_core.core_schema import arguments_parameter
def run_python_file(working_directory, file_path, args=[]):

    full_path = os.path.join(working_directory, file_path)

    abs_working_dir = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_full_path):
       return f'Error: File "{file_path}" not found.'
    if abs_full_path[-3:] != '.py':
       return f'Error: "{file_path}" is not a Python file.'


    try:
        arguments = [abs_full_path] + args
        completed_process = subprocess.run(arguments, timeout=30, capture_output=True) 
        print(completed_process)

    except Exception as e:
        return f"Error: executing Python file: {e}"
