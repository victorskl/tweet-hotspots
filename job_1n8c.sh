#!/bin/bash
#SBATCH --job-name=TweetHotspotsApp_1n8c
#SBATCH -p cloud
#SBATCH --time=00:15:59
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1

echo $HOSTNAME
echo 'Number of cpu on node: ' $SLURM_CPUS_ON_NODE
echo 'TweetHotspotsApp_1n8c'
echo 'Running: 1 node 8 cores'
echo ' '

module load OpenMPI
module load Python
mpirun -np 8 python app.py
