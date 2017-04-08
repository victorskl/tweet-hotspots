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

---
This assignment work is done for _COMP90024 Cluster and Cloud Computing_ assignment 1 assessment of 2017 SM1, The University of Melbourne. You can read [the report](SanKhoLin_829463_COMP90024_Project1_Report.pdf) for background context, though it discusses more on the data that I have worked with. You may also want to read the related tutorials [`mpi4py-tute`](https://github.com/victorskl/mpi4py-tute) and [`mpjexpress-tute`](https://github.com/victorskl/mpjexpress-tute). The implementation still has room for improvement. You may wish to cite this work as follow.

LaTeX/BibTeX:

    @misc{sanl1,
        author    = {Lin, San Kho},
        title     = {Tweet Hotspots - HPC Twitter GeoProcessing},
        year      = {2017},
        url       = {https://github.com/victorskl/tweet-hotspots},
        urldate   = {yyyy-mm-dd}
    }
