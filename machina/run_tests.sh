#!/bin/bash
#SBATCH --job-name=machina_test_job
#SBATCH --output=machina_test_job.out
#SBATCH --error=machina_test_job.err
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

source /stornext/Home/data/allstaff/l/lmcintosh/mambaforge/etc/profile.d/conda.sh
conda activate /stornext/Bioinf/data/bioinf-data/Papenfuss_lab/projects/evolution/environments/machina

python machina_tests.py

