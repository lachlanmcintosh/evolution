#!/bin/bash

# specify the name of the job
#SBATCH --job-name=pyclone-vi-test

# specify the number of cpus needed for this job
#SBATCH --ntasks=1

# specify the amount of memory needed (e.g. 2G)
#SBATCH --mem=2G

# specify how long the job should run hh:mm:ss (e.g. 01:30:00 = 1 hour 30 minutes)
#SBATCH --time=01:30:00

# specify the output file. %j will be replaced with the job ID
#SBATCH --output=pyclone-vi-test-output-%j.txt

# specify the error file. %j will be replaced with the job ID
#SBATCH --error=pyclone-vi-test-error-%j.txt

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=your-email@your-domain.com

# activate conda environment
source /stornext/Bioinf/data/bioinf-data/Papenfuss_lab/projects/evolution/environments/pyclone-vi/etc/profile.d/conda.sh
conda activate pyclone-vi

# run the application
python /home/users/allstaff/lmcintosh/evolution/pyclone-vi/test_pyclone.py

