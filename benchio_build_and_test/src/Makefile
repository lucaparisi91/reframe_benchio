
SHELL:= bash

all: setup

benchio_link:
	ln -s /work/z19/z19/lparisi/reframe/benchio/benchio .
	ln -s /work/z19/z19/lparisi/reframe/benchio/adios2 .

setup:	benchio_link
	$(SHELL) setup.sh

adios2:
	$(SHELL) build_adios.sh

$(OBJ):	$(MF)

benchio:	adios2
	$(SHELL) build_benchio.sh

clean:
	rm -rf adios2 benchio adios2-build benchio ADIOS2 striped unstriped fullstriped adios2.xml