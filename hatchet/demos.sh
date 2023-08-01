#!/bin/bash

# Define path to the hatchet folder
HATCHET_DIR="/home/users/allstaff/lmcintosh/evolution/hatchet/hatchet"

# Define path to the tests folder
TESTS_DIR="$HATCHET_DIR/tests"

# Navigate to tests folder
cd "$TESTS_DIR"

# Find all Python test scripts in the current folder
TEST_SCRIPTS=$(find . -name 'test_*.py')

# Iterate through each found test script and execute
for TEST_SCRIPT in $TEST_SCRIPTS
do
    python $TEST_SCRIPT
done

# Define array of demo folders
declare -a DEMO_FOLDERS=("demo-complete" "demo-WES" "demo-WGS-cancer" "demo-WGS-sim")

# Iterate through the demos
for DEMO in "${DEMO_FOLDERS[@]}"
do
    # Navigate to demo folder
    cd "$HATCHET_DIR/examples/$DEMO"

    # Find all bash scripts in the current folder
    SCRIPTS=$(find . -name '*.sh')

    # Iterate through each found bash script and execute
    for SCRIPT in $SCRIPTS
    do
        bash $SCRIPT
    done
done
