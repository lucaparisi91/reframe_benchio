#!/bin/bash
#SBATCH --job-name=reframe_benchio
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=01-00:00:00
#SBATCH --partition=serial
#SBATCH --qos=serial
#SBATCH --account=z19
#SBATCH --hint=nomultithread
#SBATCH --distribution=block:block

module load reframe
module load epcc-reframe

unset SLURM_MEM_PER_NODE
unset SLURM_MEM_PER_CPU

filename_report=`date +%d-%m-%Y_%H.%M`.json
report_dir="/work/z19/z19/shared/benchio/reports/${filename_report}"

reframe -C /work/y07/shared/utils/core/epcc-reframe/configuration/archer2_settings.py -J"account=z19" --report-file ${report_dir} -c ../tests/ -R -r
chmod -R g+Xr ${report_dir}

sbatch  --begin=now+3600 submit_benchio.sh
