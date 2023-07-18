# This script will be used to check if CliP was installed correctly.

# 1. Importing the required packages
try:
    import numpy
    import scipy
    import pandas
    import subprocess
except ImportError:
    print("Error: NumPy, SciPy, or pandas is not installed.")

# 2. Testing CliP package
try:
    # Test data in the correct format for CliP
    snv_file = "/home/users/allstaff/lmcintosh/evolution/clip/CliP/sample/sample.snv.txt"
    cna_file = "/home/users/allstaff/lmcintosh/evolution/clip/CliP/sample/sample.cna.txt"
    purity_file = "/home/users/allstaff/lmcintosh/evolution/clip/CliP/sample/sample.purity.txt"

    # Optional parameters
    sample_id = 'sample_id'
    lam = 0.05  # choose an appropriate lambda value for your case
    preprocess = 'preprocess_result/'
    final = 'final_result/'

    # Create the command string
    cmd = f"python /home/users/allstaff/lmcintosh/evolution/clip/CliP/run_clip_main.py {snv_file} {cna_file} {purity_file} -i {sample_id} -l {lam} -p {preprocess} -f {final}"

    # Execute the command
    subprocess.check_call(cmd, shell=True)
    
    print("CliP package is working as expected.")
except subprocess.CalledProcessError:
    print("Error: CliP package did not run successfully.")
except Exception as e:
    print(f"Error: An error occurred while running CliP: {e}")

