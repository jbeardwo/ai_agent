import os
import subprocess
from google.genai import types

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
        arguments = ['python', abs_full_path] + args
        completed_process = subprocess.run(arguments, timeout=30, capture_output=True, cwd=abs_working_dir, text=True) 

        if not completed_process.stdout and not completed_process.stderr:
            return "No output produced."

        result = ''
        if completed_process.stdout:
            result += f'\nSTDOUT: {completed_process.stdout}'
        if completed_process.stderr:
            result += f'\nSTDERR: {completed_process.stderr}'
        if completed_process.returncode != 0:
            result += f'\nProcess exited with code {completed_process.returncode}'

        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified python program with given arguments. Constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to be run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="The arguments to be passed to the python file being run.",
                items=types.Schema(
                    type=types.Type.STRING
                )
            ),
        },
    ),
)

