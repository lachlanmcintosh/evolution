#!/bin/bash
#SBATCH --job-name=test_clip
#SBATCH --output=test_clip_%j.out
#SBATCH --error=test_clip_%j.err
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

# Source the necessary conda scripts
source /stornext/Home/data/allstaff/l/lmcintosh/mambaforge/etc/profile.d/conda.sh

# Activate the necessary conda environment
conda activate /stornext/Bioinf/data/bioinf-data/Papenfuss_lab/projects/evolution/environments/clip

# Call the Python script
python /home/users/allstaff/lmcintosh/evolution/clip/test_clip.py

