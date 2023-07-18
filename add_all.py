import subprocess
import os

def git_add_files():
    # Get the current working directory
    cwd = os.getcwd()

    # Get a list of all directories in the current directory
    directories = [dir for dir in os.listdir(cwd)
                   if os.path.isdir(os.path.join(cwd, dir)) and
                   not os.path.islink(os.path.join(cwd, dir)) and
                   dir not in ['temp_nix_store', 'environments']]

    # Add directories to the list
    directories.append(cwd)  # add the current directory to the list

    for directory in directories:
        # Get a list of all files in the current directory
        files_in_dir = [os.path.join(cwd, directory, f) for f in os.listdir(os.path.join(cwd, directory)) if os.path.isfile(os.path.join(cwd, directory, f))]

        # Add each file to the Git repository
        for file_name in files_in_dir:
            subprocess.run(["git", "add", file_name])

    # Commit the changes
    subprocess.run(["git", "commit", "-m", "Added files"])

# Run the function
git_add_files()

