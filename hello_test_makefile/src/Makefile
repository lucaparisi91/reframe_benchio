# You will need to load some modules:
 
# module load adios/2.8.3
# module load cray-hdf5-parallel
# module load cray-netcdf-hdf5parallel


CC=	CC

EXE=	hello

SRC= \
	hello.cpp


OBJ=	$(SRC:.cpp=.o)

.cpp.o:
	$(CC) $(FFLAGS) -c $<

all:	$(EXE)

$(EXE):	$(OBJ)
	$(CC) -o $@ $(OBJ)

$(OBJ):	$(MF)

clean:
	rm -f $(OBJ) $(EXE)
