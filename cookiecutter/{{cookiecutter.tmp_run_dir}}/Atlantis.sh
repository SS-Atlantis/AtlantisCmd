#!/bin/bash

set -e  # abort on first error
set -u  # abort if undefined variable is encountered

RUN_ID="{{ cookiecutter.run_id }}"
RUN_DESC="{{ cookiecutter.run_desc_yaml }}"
WORK_DIR="{{ cookiecutter.tmp_run_dir }}"
RESULTS_DIR="{{ cookiecutter.results_dir }}"
GATHER="{{ cookiecutter.atlantis_cmd }} gather"

mkdir -p ${RESULTS_DIR}

cd ${WORK_DIR}
echo "working dir: $(pwd)" >${RESULTS_DIR}/stdout

echo "Starting run at $(date)" >>${RESULTS_DIR}/stdout
./{{ cookiecutter.atlantis_executable_name }} \
  -i init_conditions.nc 0 -o {{ cookiecutter.output_filename_base }}.nc \
  -r run.prm -f forcing.prm -p physics.prm -b biology.prm -s groups.csv -m migrations.csv \
  -d ${RESULTS_DIR} &>>${RESULTS_DIR}/stdout
ATLANTIS_EXIT_CODE=$?
echo "Ended run at $(date)" >>${RESULTS_DIR}/stdout

echo "Results gathering started at $(date)" >>${RESULTS_DIR}/stdout
${GATHER} ${RESULTS_DIR} --debug &>>${RESULTS_DIR}/stdout
echo "Results gathering ended at $(date)" >>${RESULTS_DIR}/stdout

chmod -v go+rx ${RESULTS_DIR} &>>${RESULTS_DIR}/stdout
chmod -v g+rw ${RESULTS_DIR}/* &>>${RESULTS_DIR}/stdout
chmod -v o+r ${RESULTS_DIR}/* &>>${RESULTS_DIR}/stdout

echo "Deleting run directory" >>${RESULTS_DIR}/stdout
rmdir -v $(pwd) &>>${RESULTS_DIR}/stdout
echo "Finished at $(date)" >>${RESULTS_DIR}/stdout
exit ${ATLANTIS_EXIT_CODE}
