#!/bin/sh

# creates a directory to use as test results
mkdir striped
mkdir unstriped
mkdir fullstriped

lfs setstripe -c 1 unstriped
lfs setstripe -c -1 fullstriped
lfs setstripe -c 4 striped
