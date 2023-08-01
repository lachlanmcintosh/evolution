import os
import subprocess

# Define path to the hatchet folder
HATCHET_DIR = "/home/users/allstaff/lmcintosh/evolution/hatchet/hatchet"

# Define path to the tests folder
TESTS_DIR = os.path.join(HATCHET_DIR, "tests")

# Directory to store SBATCH scripts, logs, and error files
TEMP_DIR = os.path.join(HATCHET_DIR, "temp")
os.makedirs(TEMP_DIR, exist_ok=True)

CONDA_PATH = "/stornext/Home/data/allstaff/l/lmcintosh/mambaforge/etc/profile.d/conda.sh"

# Function to create and submit an SBATCH script
def submit_sbatch_script(command, job_name):
    sbatch_file = os.path.join(TEMP_DIR, f"{job_name}.sbatch")
    log_file = os.path.join(TEMP_DIR, f"{job_name}.log")
    error_file = os.path.join(TEMP_DIR, f"{job_name}.err")

    sbatch_script = f"""#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --output={log_file}
#SBATCH --error={error_file}
#SBATCH --mem=10GB

# Source conda
source "{CONDA_PATH}"

# Activate the hatchet conda environment
conda activate /home/users/allstaff/l/lmcintosh/evolution/environments/hatchet

{command}
"""

    # Write the SBATCH script to a file
    with open(sbatch_file, "w") as file:
        file.write(sbatch_script)

    # Submit the SBATCH script using the "sbatch" command
    subprocess.run(["sbatch", sbatch_file])

# Function to handle test scripts
def handle_tests():
    test_scripts = [os.path.join(TESTS_DIR, f) for f in os.listdir(TESTS_DIR) if f.startswith("test_") and f.endswith(".py")]
    for test_script in test_scripts:
        script_name = os.path.basename(test_script)[:-3] # Removing .py extension
        job_name = f"test_{script_name}"
        command = f"python {test_script}"
        submit_sbatch_script(command, job_name)

# Function to handle demo scripts
def handle_demos():
    demo_folders = ["demo-complete", "demo-WES", "demo-WGS-cancer", "demo-WGS-sim"]
    for demo_folder in demo_folders:
        demo_path = os.path.join(HATCHET_DIR, "examples", demo_folder)
        demo_scripts = [os.path.join(demo_path, f) for f in os.listdir(demo_path) if f.endswith('.sh')]
        for demo_script in demo_scripts:
            script_name = os.path.basename(demo_script)[:-3] # Removing .sh extension
            job_name = f"demo_{script_name}"
            command = f"bash {demo_script}"
            submit_sbatch_script(command, job_name)

# Handle test and demo scripts
handle_tests()
handle_demos()

# Note: Please run this code on your local system with Slurm installed.

