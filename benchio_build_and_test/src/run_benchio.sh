#!/bin/sh

module load cray-hdf5-parallel
module load cray-netcdf-hdf5parallel

# creates a directory to use as test results
mkdir striped
mkdir unstriped
mkdir fullstriped

lfs setstripe -c 1 unstriped
lfs setstripe -c -1 fullstriped
lfs setstripe -c 4 striped

# start the benchmark
srun ./benchio/benchio 512 512 512 global
