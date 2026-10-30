#!/bin/bash

# Check input parameters from user, accepting only a filepath under ~/csce465-agentsec/hw3/inbox/
if [[ "$1" != /home/anna_s/csce465-agentsec/hw3/inbox/* && "$1" != "hw3/inbox/" ]]; then
    echo "Error: Input file must be under ~/csce465-agentsec/hw3/inbox/"
    exit 1
fi

# Run the legacy log parser on the provided file
./src/legacy_log_parser "$1"

# Report the output or any errors encountered during execution
if [[ $? -ne 0 ]]; then
    echo "Error: Legacy log parser failed."
fi