module load cray-hdf5-parallel

set -e

### Build adios
git clone https://github.com/ornladios/ADIOS2.git
mkdir adios2-build && cd adios2-build
cmake CXX=CC CC=cc FC=ftn -DADIOS2_USE_HDF5=TRUE  -DCMAKE_INSTALL_PREFIX=../adios2 ../ADIOS2/
make -j 8
make install 
cd ..

### Creates script to be sourced before using the library
cd adios2
echo "INSTALL_DIR=$(pwd)" > source.sh
echo 'export PATH=${INSTALL_DIR}/bin:${PATH}' >> source.sh
echo 'export LD_LIBRARY_PATH=${INSTALL_DIR}/lib64:${LD_LIBRARY_PATH}' >> source.sh
echo 'export LIBRARY_PATH=${INSTALL_DIR}/lib64:${LIBRARY_PATH}' >> source.sh
cd .. 

git clone https://github.com/davidhenty/benchio
cd benchio 
source ../adios2_24/source.sh
make
