#!/bin/bash

# Directory containing the generated job scripts
job_dir="/home/susmitsj/training_data/rae2822/"

# Check if the directory exists
if [ ! -d "$job_dir" ]; then
  echo "Error: Directory '$job_dir' does not exist."
  exit 1
fi

# Submit each job script in the directory
for job_script in "$job_dir"/*.sh; do
  if [ -f "$job_script" ]; then
    echo "Submitting job script: $job_script"
    sbatch "$job_script"
  else
    echo "No job scripts found in '$job_dir'."
  fi
done

echo "All job scripts in '$job_dir' have been submitted."
