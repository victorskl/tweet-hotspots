#!/bin/bash
#SBATCH --job-name=TweetHotspotsApp_1n1c
#SBATCH -p physical
#SBATCH --time=00:30:59
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

# NOTE: echo-ing HOSTNAME and SLURM_CPUS_ON_NODE
# make sense on running in 1-node.
# If nodes > 1, better comment them out!
echo $HOSTNAME
echo 'Number of cpu on node: ' $SLURM_CPUS_ON_NODE

echo 'TweetHotspotsApp_1n1c'
echo 'Running: 1 node 1 core'
echo ' '

module load Python/3.4.3-goolf-2015a
#mpirun -np 1 python app.py   # we don't need -np flag, just config --nodes, --ntasks
mpirun python app.py
