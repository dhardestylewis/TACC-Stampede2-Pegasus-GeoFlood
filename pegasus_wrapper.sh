#!/bin/bash


POSITIONAL_ARGS=()

while [[ $# -gt 0 ]]; do
  case $1 in
    -e|--environment)
      ENVIRONMENT="$2"
      shift ## past argument
      shift ## past value
      ;;
    -s|--singularity)
      SINGULARITY="$2"
      shift ## past argument
      shift ## past value
      ;;
    -m|--mpi)
      MPI="$2"
      shift ## past argument
      shift ## past value
      ;;
    *)
      POSITIONAL_ARGS+=("$1")
      shift
      ;;
  esac
done

set -- "${POSITIONAL_ARGS[@]}"


function activate_environment {

  source pegasus.rc
  
  if [ ! -z ${ENVIRONMENT+x} ]; then
    eval "$(conda shell.bash hook)"
    export LD_LIBRARY_PATH="${work_dir}/miniconda3/envs/${ENVIRONMENT}/lib:${LD_LIBRARY_PATH}"
    conda activate ${ENVIRONMENT}
  fi
  
  eval "${POSITIONAL_ARGS}"
  
  if [ ! -z ${ENVIRONMENT+x} ]; then
    conda deactivate
#    export LD_LIBRARY_PATH=$(echo "${LD_LIBRARY_PATH}" | sed -e "s/:$work_dir\/miniconda3\/envs\/${ENVIRONMENT}\/lib$//")
  fi

}

function singularity_command {
  if [ -z ${SINGULARITY+x} ]; then
    activate_environment
  else
    source pegasus.rc
    export ENVIRONMENT
    export POSITIONAL_ARGS
    module load tacc-singularity
    singularity exec --env APPEND_PATH="${ACTIVATE_ENV_PATH}" ${SINGULARITY} conda info --envs
  fi
}

function mpi_command {
  if [ -z ${MPI+x} ] || (( ${MPI} == 1 )); then
    singularity_command
  else
    ibrun -n ${MPI} singularity_command
  fi
}

mpi_command
