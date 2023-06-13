# Copyright 2016-2022 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn
import os 
import re
import json

@rfm.simple_test
class benchio(rfm.RegressionTest):

    lang = parameter(['cpp'])
    valid_systems = ['archer2:compute']
    valid_prog_environs = ['PrgEnv-gnu']

    num_nodes = parameter( [1,2] )
    
    reference = {
        'archer2:compute': {
            'fullstriped_hdf5': ( 0.9, -0.3, 0.3 ,'GB/s'),
            'unstriped_hdf5': ( 0.7, -0.7, 0.7 ,'GB/s'),
            'fullstriped_mpiio': ( 1, -0.4, 0.4 ,'GB/s'),
            'unstriped_mpiio': ( 0.6, -0.5, 0.5 ,'GB/s')
        }
    }


    def __init__(self,**kwds):

        super().__init__()
        self.executable= "./src/benchio"
        self.executable_opts = ('1260 1260 1260 global mpiio hdf5').split()
        self.num_tasks = 128 * self.num_nodes
        self.num_tasks_per_node = 128
        self.num_cpus_per_task = 1

        self.env_vars = {"OMP_NUM_THREADS": str(self.num_cpus_per_task)}
        self.prerun_cmds  = ['source create_striped_dirs.sh']
        self.time_limit = '1h'
        self.build_system = 'CMake'
        self.build_system.ftn="ftn"
        self.modules = [ "cray-hdf5-parallel" ]

        self.perf_patterns = {
            'fullstriped_hdf5': sn.extractsingle(r'Writing to fullstriped/hdf5\.dat\W*\n\W*time\W*=\W*\d+.\d*\W*,\W*rate\W*=\W*(\d+.\d*)',
                                     self.stdout, 1, float),
            'unstriped_hdf5': sn.extractsingle(r'Writing to unstriped/hdf5\.dat\W*\n\W*time\W*=\W*\d+.\d*\W*,\W*rate\W*=\W*(\d+.\d*)',
                                     self.stdout, 1, float),
            'unstriped_mpiio': sn.extractsingle(r'Writing to unstriped/mpiio\.dat\W*\n\W*time\W*=\W*\d+.\d*\W*,\W*rate\W*=\W*(\d+.\d*)',
                                    self.stdout, 1, float),
            'fullstriped_mpiio': sn.extractsingle(r'Writing to fullstriped/mpiio\.dat\W*\n\W*time\W*=\W*\d+.\d*\W*,\W*rate\W*=\W*(\d+.\d*)',
                                    self.stdout, 1, float)
        }
    
    @run_before('compile')
    def set_compiler_flags(self):
        self.build_system.config_opts= ["-DUSE_HDF5=TRUE" ]
    
    @sanity_function
    def assert_benchio(self):
        return sn.assert_found(r'Finished', self.stdout)