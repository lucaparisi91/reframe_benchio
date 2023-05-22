# Copyright 2016-2022 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class benchioTest(rfm.RegressionTest):
    lang = parameter(['cpp'])

    valid_systems = ['archer2:login']
    valid_prog_environs = ['PrgEnv-cray']

    def __init__(self,**kwargs):
        self.executable= "./benchio/benchio"

    @sanity_function
    def assert_hello(self):
        return sn.assert_found(r'benchio', self.stdout)