#!/bin/bash
#SBATCH -J rae2822_0
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=susmitsj@vt.edu
#SBATCH -p normal_q
#SBATCH -N 1
#SBATCH --ntasks-per-node=128 
#SBATCH -t 10:00:00
#SBATCH -A adjfsi
#SBATCH --chdir=/home/susmitsj/training_data/rae2822/

#load modules
module reset
# module load GCC/8.3.0
# module load GCCcore/8.3.0
# module load Ninja/1.9.0-GCCcore-8.3.0
# module load OpenBLAS/0.3.7-GCC-8.3.0
# module load OpenMPI/3.1.4-GCC-8.3.0
# module load CMake/3.15.3-GCCcore-8.3.0
# module load Python/3.7.4-GCCcore-8.3.0
# module load SWIG/4.0.1-GCCcore-8.3.0
# module load mpi4py/3.0.2-iimpi-2019b-timed-pingpong
# module load iomkl/2019b
# module load intel/2019b
module load tinkercliffs-rome/SU2/8.0.0-foss-2022a-mpi

#run
mpirun -n 128 SU2_CFD ./con_rae2822_air_0.cfg > log_rae2822_air_0 

