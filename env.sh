#!/usr/bin/env bash

ln -s /data/projects/COMP90024/ ./data
ls -l .

module load Python/3.5.2-intel-2016.u3
python -V
which python
python -c "import mpi4py"