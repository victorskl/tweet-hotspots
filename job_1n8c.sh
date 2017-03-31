#!/bin/bash
#SBATCH --job-name=TweetHotspotsApp_1n8c
#SBATCH -p cloud
#SBATCH --time=00:15:59
#SBATCH --nodes=1
#SBATCH --ntasks=8

echo hostname
echo 'Number of cpu on node: ' $SLURM_CPUS_ON_NODE
echo ' '

echo 'Run: 1 node 8 cores'
echo ' '

module load Python/3.5.2-intel-2016.u3
mpirun -np 8 python app.py
