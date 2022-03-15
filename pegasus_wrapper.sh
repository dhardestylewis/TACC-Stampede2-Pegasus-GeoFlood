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
    *)
      POSITIONAL_ARGS+=("$1")
      shift
      ;;
  esac
done

set -- "${POSITIONAL_ARGS[@]}"


activate_environment()
{

  source pegasus.rc
  
  if [ ! -z ${ENVIRONMENT+x} ]; then
    eval "$(conda shell.bash hook)"
    export LD_LIBRARY_PATH="${work_dir}/miniconda3/envs/${ENVIRONMENT}/lib:${LD_LIBRARY_PATH}"
    conda activate ${ENVIRONMENT}
  fi
  
  eval "$1"
  
  if [ ! -z ${ENVIRONMENT+x} ]; then
    conda deactivate
    export LD_LIBRARY_PATH=$(echo "${LD_LIBRARY_PATH}" | sed -e "s/:$work_dir\/miniconda3\/envs\/${ENVIRONMENT}\/lib$//")
  fi

}

if [ -z ${SINGULARITY+x} ]; then
  activate_environment
else
  singularity exec ${SINGULARITY} activate_environment
fi
