# Running the benchio test trough epcc-Reframe

You can launch the test using

```bash 
module load reframe
module load epcc-reframe
epcc-reframe -c ../tests -R -n  benchio -r -J "account=z19"
```
You need to be part of the z19 account in order to run these tests.
Temporary files are stored in `/work/z19/z19/shared/benchio` , on all filesystems being tested.

# Running the tests
The directory `scripts` contains a script to launch recursively the jobs.
The results are stored as timestamped json files in the directory `/work/z19/z19/shared/benchio/reports`.