# Builds the benchio benchmark from David Henty
module load cray-hdf5-parallel
module load cray-netcdf-hdf5parallel

set -e 


git clone https://github.com/davidhenty/benchio
cd benchio 
cp Makefile-archer2 Makefile

source ../adios2/source.sh
make CXX=CC CC=cc FC=ftn