# Reframe 

Instructions for installing are found at https://reframe-hpc.readthedocs.io . It can be done trough GitHub .

`--report-file` flag can be used to control where the test report is saved.

`RFM_CONFIG_PATH` environment variables contain the path of the configuration files

`"system_name:parition_name"` can be used to filter the partitions where to run a test .

This repository contains the tests:

- hello_test : basic hello world test case
- hello-test_makefile : basic hellow world test case with a Makefile build ( no option )
- benchio_build_and_test: builds adios2, benchio and launches a test
- exp1/test.sh : template script to launch a specific test

Configuration in `configuration` folder ( currently archer2 configuration for the tds )

# Running the test trough epcc-Reframe

You can launch the test using

```bash 
module load reframe
module load epcc-reframe
epcc-reframe -c ../tests -R -n  benchio -r -J "account=z19"
```