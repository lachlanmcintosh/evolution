#!/bin/bash

#SBATCH --job-name=medicc2_test
#SBATCH --output=medicc2_test_%j.out
#SBATCH --error=medicc2_test_%j.err
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G

source activate /stornext/Bioinf/data/bioinf-data/Papenfuss_lab/projects/evolution/environments/medicc2

# Define paths
input_file="~/evolution/medicc2/medicc2/examples/simple_example/simple_example.tsv"
output_folder="~/evolution/medicc2/medicc2/examples/output"

# Run MEDICC2
medicc2 $input_file $output_folder

