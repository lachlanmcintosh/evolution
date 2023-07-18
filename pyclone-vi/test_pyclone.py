import subprocess

def run_pyclone_test():
    # set your working directory to the base directory of PyClone-VI git repo
    base_dir = "/home/users/allstaff/lmcintosh/evolution/pyclone-vi/pyclone-vi" 

    try:
        # Fit the model to the data
        print("Fitting model to the data...")
        subprocess.run(["pyclone-vi", "fit", "-i", f"{base_dir}/examples/tracerx.tsv", "-o", f"{base_dir}/tracerx.h5", "-c", "40", "-d", "beta-binomial", "-r", "10"], check=True)
        print("Model fitting completed.")

        # Output the final results from the best random restart
        print("Writing results...")
        subprocess.run(["pyclone-vi", "write-results-file", "-i", f"{base_dir}/tracerx.h5", "-o", f"{base_dir}/tracerx.tsv"], check=True)
        print("Results written.")

        print("Test completed successfully!")
    except subprocess.CalledProcessError as e:
        print("Test failed!")
        print(str(e))

if __name__ == "__main__":
    run_pyclone_test()

