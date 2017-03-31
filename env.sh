#!/usr/bin/env bash

ln -s /data/projects/COMP90024/ ./data
ls -l .

module load Python/3.4.3-goolf-2015a
python -V
which python
python -c "import mpi4py"