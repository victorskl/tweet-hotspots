#!/bin/bash
#SBATCH --job-name=TweetHotspotsApp_2n8c
#SBATCH -p physical
#SBATCH --time=00:15:59
#SBATCH --nodes=2
#SBATCH --ntasks=4

echo hostname
echo 'Number of cpu on node: ' $SLURM_CPUS_ON_NODE
echo ' '

echo 'Run: 2 node 8 cores'
echo ' '

module load Python/3.5.2-intel-2016.u3
mpirun -np 4 python app.py
