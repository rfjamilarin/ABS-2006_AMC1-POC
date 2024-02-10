import subprocess
import os

def run_main_script():
    # Get the directory where the main.py file is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Path to main.py
    main_script_path = os.path.join(script_dir, "main.py")
    
    # Execute main.py using subprocess
    subprocess.call(["python", main_script_path])

if __name__ == "__main__":
    run_main_script()