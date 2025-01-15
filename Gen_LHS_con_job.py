import os
import csv

# Dynamically get the current working directory
current_dir = os.getcwd()

# Construct the file paths using the current working directory
lhs_file = os.path.join(current_dir, "lhs_samples.csv")
template_file = os.path.join(current_dir, "con_rae2822_air_0.cfg")
job_template_file = os.path.join(current_dir, "job_rae2822_air_0.sh")
output_dir = os.path.join(current_dir, "generated_configs")
output_job_dir = os.path.join(current_dir, "generated_jobs")

# Ensure output directories exist
os.makedirs(output_dir, exist_ok=True)
os.makedirs(output_job_dir, exist_ok=True)

# Read LHS samples
with open(lhs_file, "r") as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Loop through rows 2 to 101 (index 1 to 100 in 0-based indexing)
for idx in range(102, 1251):  # Starting from the 2nd row
    # Extract sample values for the row
    row = data[idx]
    alpha, mach, z, pressure, temperature, reynolds = row[:6]  # Adjust indices if needed

    # Read the template file
    with open(template_file, "r") as file:
        content = file.readlines()

    # Update lines as per requirements
    for i, line in enumerate(content):
        if "MACH_NUMBER=" in line:
            content[i] = f"MACH_NUMBER= {mach}\n"
        elif "AOA=" in line:
            content[i] = f"AOA= {alpha}\n"
        elif "FREESTREAM_PRESSURE=" in line:
            content[i] = f"FREESTREAM_PRESSURE= {pressure}\n"
        elif "FREESTREAM_TEMPERATURE=" in line:
            content[i] = f"FREESTREAM_TEMPERATURE= {temperature}\n"
        elif "REYNOLDS_NUMBER=" in line:
            content[i] = f"REYNOLDS_NUMBER= {reynolds}\n"
        elif "SOLUTION_FILENAME=" in line:
            content[i] = f"SOLUTION_FILENAME= sol_rae2822_air_{idx}.csv\n"
        elif "CONV_FILENAME=" in line:
            content[i] = f"CONV_FILENAME= hist_rae2822_air_{idx}\n"
        elif "RESTART_FILENAME=" in line:
            content[i] = f"RESTART_FILENAME= rest_rae2822_air_{idx}.csv\n"
        elif "VOLUME_FILENAME=" in line:
            content[i] = f"VOLUME_FILENAME= vol_rae2822_air_{idx}\n"
        elif "SURFACE_FILENAME=" in line:
            content[i] = f"SURFACE_FILENAME= sur_rae2822_air_{idx}\n"

    # Write updated content to a new .cfg file
    output_file = os.path.join(output_dir, f"con_rae2822_air_{idx}.cfg")
    with open(output_file, "w") as file:
        file.writelines(content)

    # Read the template job script
    with open(job_template_file, "r") as file:
        job_content = file.readlines()

    # Update lines as per requirements
    for i, line in enumerate(job_content):
        if "#SBATCH -J rae2822_0" in line:
            job_content[i] = f"#SBATCH -J rae2822_{idx}\n"
        elif "mpirun -n 128 SU2_CFD ./con_rae2822_air_0.cfg > log_rae2822_air_0" in line:
            job_content[i] = f"mpirun -n 128 SU2_CFD ./con_rae2822_air_{idx}.cfg > log_rae2822_air_{idx}\n"

    # Write updated content to a new job file
    output_job_file = os.path.join(output_job_dir, f"job_rae2822_air_{idx}.sh")
    with open(output_job_file, "w") as file:
        file.writelines(job_content)

print(f"Configuration files generated in: {output_dir}")
print(f"Job scripts generated in: {output_job_dir}")