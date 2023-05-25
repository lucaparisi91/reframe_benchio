mkdir striped
mkdir unstriped
mkdir fullstriped

lfs setstripe -c 1 unstriped
lfs setstripe -c -1 fullstriped
lfs setstripe -c 4 striped

ln -s benchio/adios2.xml adios2.xml