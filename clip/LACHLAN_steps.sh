# The installation steps that were in the github repo didn't work for me 
# These are the steps that I used to sucessfully install it:

conda create -n clip python=3.7
conda activate clip
pip install numpy scipy pandas
conda install -c r r-base=3.6.1
git clone https://github.com/wwylab/CliP.git
cd CliP
python setup.py build
python setup.py install

R
install.packages("stringi")
quit()

sbatch LACHLAN_steps.slurm
