import os
import subprocess

def run_lichee_cmd(lichee_path, input_file_path, output_file_path, options):
    cmd = [
        lichee_path,  # we're calling the lichee shell script directly
        "-build",
        "-i",
        input_file_path,
        "-o",
        output_file_path,
    ]
    cmd += options

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("LICHeE test passed.")
    else:
        print("LICHeE test failed.")
        print("Error message:")
        print(result.stderr)

    return result.returncode == 0

def test_lichee():
    lichee_path = "/home/users/allstaff/lmcintosh/evolution/lichee/lichee/LICHeE/release/lichee"  # updated path
    input_file_path = "/home/users/allstaff/lmcintosh/evolution/lichee/lichee/LICHeE/release/data/test.txt"  # replace 'test.txt' with your test data file
    output_file_path = "/home/users/allstaff/lmcintosh/evolution/lichee/lichee/LICHeE/release/data/test_output.txt"  # the output file will be created here
    options = ["-maxVAFAbsent", "0.005", "-minVAFPresent", "0.005", "-n", "0", "-showTree", "1"]

    # Test 1: Does the LICHeE command complete successfully?
    success = run_lichee_cmd(lichee_path, input_file_path, output_file_path, options)
    if not success:
        return  # if the command didn't run successfully, there's no point continuing with the tests

    # Test 2: Does the output file exist?
    if os.path.exists(output_file_path):
        print("Output file test passed.")
    else:
        print("Output file test failed: file does not exist.")

    # More tests can be added here as needed...

# run the tests
test_lichee()

