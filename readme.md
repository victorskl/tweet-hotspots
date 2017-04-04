## Tweet Hotspots

This application will search a large Geo-Coded Twitter dataset to identify tweet hotspots around Melbourne. The key purpose is to experiment and exercise the parallel programming on HPC environment and GeoProcessing big Twitter data.

It is using Python and `mpi4py` as a key module.

### Running Local

```batch
mpiexec -n 8 python app.py
```

### Running on [SPARTAN HPC](https://dashboard.hpc.unimelb.edu.au/)

```commandline
sbatch job_1n1c.sh
sbatch job_1n8c.sh
sbatch job_2n8c.sh
sbatch job_2n8c-sym.sh
```

NOTE: the different between `job_2n8c.sh` and `job_2n8c-sym.sh` is that, the latter `-sym` ensure 4 cores per node by using `--ntasks-per-node=4`, therefore symmetrical.

Utility scripts such as `env.sh` prepare input data and environmental setup on cluster and `clean.sh` clear outputs and log files for consecutive runs if desire.

### Slurm useful commands
 
```bash
squeue -u [ur_username]
scontrol show jobid -dd [ur_job_id]
scancel [ur_job_id]
```
