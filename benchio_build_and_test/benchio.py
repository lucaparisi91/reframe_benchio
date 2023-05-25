# Copyright 2016-2022 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn
import os

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
        return sn.assert_found(r'Finished', self.stdout)