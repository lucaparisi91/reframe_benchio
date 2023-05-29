# Copyright 2016-2022 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn
import os 
import re

# TEST STEUP
# modify testConditionsobject to change the thresold on interval of memory bandwith for the test to fail ( or pass )


testConditions = {
        "hdf5" :
            {
                "fullstriped" :
                {
                    "min_bandwidth" : 0.9,
                    "max_bandwidth" : 1.5
                }
            }
        }



def extract_timing( out ):
    pattern=r"Writing to (striped|unstriped|fullstriped)\/([a-z0-9]+)\.dat\W*\n time\W=\W+(\d.\d*)\W,\Wrate\W=\W+(\d.\d*)"
        
    prog = re.compile(pattern, re.IGNORECASE | re.MULTILINE )
    matches= prog.findall(out)

    result={}

    for match in matches:
        test=match[1]
        stripe=match[0]
        time=match[2]
        bandwidth=match[3]

        if not test in result:
            result[test]={}

        if not stripe in result[test]:
            result[test][stripe]={}
        
        result[test][stripe]["time"]=float(time)
        result[test][stripe]["bandwidth"]=float(bandwidth)

        #result[ test ]={ stripe :  { "time" : float(time), "bandwidh" : float(bandwidh) } }
    
    return(result)

def check_timing( outputResult, testConditions ):
    
    result=True 

    for test in testConditions:
        for stripe in testConditions[test]:
            min_bandwith=testConditions[test][stripe]["min_bandwidth"]
            max_bandwidth=testConditions[test][stripe]["max_bandwidth"]

            bandwidth = outputResult[test][stripe]["bandwidth"]


            result = result and (bandwidth>= min_bandwith) and (bandwidth <= max_bandwidth) 
    return result






@rfm.simple_test
class benchioTest(rfm.RegressionTest):
    lang = parameter(['cpp'])

    valid_systems = ['archer2:compute']
    valid_prog_environs = ['PrgEnv-cray']

    def __init__(self,**kwargs):

        super().__init__()
        self.executable= "./benchio/benchio"
        self.executable_opts = ('512 512 512 global').split()
        self.num_tasks = 128
        self.num_tasks_per_node = 128
        self.num_cpus_per_task = 1
        
        self.env_vars = {"OMP_NUM_THREADS": str(self.num_cpus_per_task)}
        self.prerun_cmds  = ['source source.sh']

    @sanity_function
    def assert_benchio(self):
        #Writing to (striped|unstriped|fullstriped)\/([a-z0-9]+)\.dat\W*\n time\W=\W+(\d.\d*)\W,\Wrate\W=\W+(\d.\d*)
        #return sn.assert_found(r'Finished', self.stdout)

        with open( str(self.stdout)) as f:
            out=f.read()
        timePerfOut=extract_timing( str(out) )


        return check_timing(timePerfOut, testConditions) 


