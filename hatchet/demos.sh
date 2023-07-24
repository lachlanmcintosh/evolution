#!/bin/bash

# define path to the hatchet folder
HATCHET_DIR="/home/users/allstaff/lmcintosh/evolution/hatchet/hatchet"

# define array of demo folders
declare -a DEMO_FOLDERS=("demo-complete" "demo-WES" "demo-WGS-cancer" "demo-WGS-sim")

# iterate through the demos
for DEMO in "${DEMO_FOLDERS[@]}"
do
    # navigate to demo folder
    cd "$HATCHET_DIR/examples/$DEMO"

    # find all bash scripts in the current folder
    SCRIPTS=$(find . -name '*.sh')

    # iterate through each found bash script
    for SCRIPT in $SCRIPTS
    do
        echo "Running script: $SCRIPT"
        bash "$SCRIPT"
    done
done

