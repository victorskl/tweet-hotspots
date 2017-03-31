#!/bin/bash
#SBATCH --job-name=TweetHotspotsApp_1n1c
#SBATCH -p cloud
#SBATCH --time=00:30:59
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

echo $HOSTNAME
echo 'Number of cpu on node: ' $SLURM_CPUS_ON_NODE
echo 'TweetHotspotsApp_1n1c'
echo 'Running: 1 node 1 core'
echo ' '

module load Python/3.4.3-goolf-2015a
mpirun -np 1 python app.py
