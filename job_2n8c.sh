#!/bin/bash
#SBATCH --job-name=TweetHotspotsApp_2n8c
#SBATCH -p physical
#SBATCH --time=00:15:59
#SBATCH --nodes=2
#SBATCH --ntasks=4

echo $HOSTNAME
echo 'Number of cpu on node: ' $SLURM_CPUS_ON_NODE
echo 'TweetHotspotsApp_2n8c'
echo 'Running: 2 node 8 cores'
echo ' '

module load Python/3.5.2-intel-2016.u3
mpirun -np 8 python app.py
