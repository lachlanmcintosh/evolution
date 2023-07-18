import subprocess

# Define the commands to execute Machina
commands = [
    "pmh_sankoff -p LOv,ROv -c machina/data/mcpherson_2016/coloring.txt machina/data/mcpherson_2016/patient1.tree machina/data/mcpherson_2016/patient1.labeling -o patient1/",
    "pmh_sankoff -p LOv,ROv -c machina/data/mcpherson_2016/coloring.txt machina/data/mcpherson_2016/patient2.tree machina/data/mcpherson_2016/patient2.labeling -o patient2/",
    # Add more commands for different test cases here...
]

for i, command in enumerate(commands, start=1):
    try:
        # Execute the command
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)

        # Print the output
        print("Output for command {}:\n{}".format(i, output.decode('utf-8')))

        # Machina executed successfully
        print("Machina test script for command {} executed successfully.".format(i))
    except subprocess.CalledProcessError as e:
        # Machina execution failed
        print("Machina test script for command {} failed. Error:\n{}".format(i, e.output.decode('utf-8')))

