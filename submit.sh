#!/bin/bash

set -e

TOP_DIR=`dirname $0`
export TOP_DIR=`cd $TOP_DIR && pwd`
export RUN_ID=`date --iso-8601='seconds' | sed 's/://g'`
export WORK_DIR=$WORK/$RUN_ID

export PEGASUS_HOME=/home/00384/rynge/software/pegasus/4.9.0dev
export PATH=$PEGASUS_HOME/bin:$PATH

echo
echo "Work dir is $WORK_DIR"
echo

mkdir -p $WORK_DIR

# create a site and transformation catalogs from the templates
envsubst < sites.template.xml > $WORK_DIR/sites.xml
envsubst < transformations.template.txt > $WORK_DIR/transformations.txt

# generate the dax
export PYTHONPATH=`pegasus-config --python`
./dax-generator.py $PEGASUS_HOME > $WORK_DIR/black-diamond.dax

# plan and submit the  workflow
cd $WORK_DIR
pegasus-plan \
    --conf $TOP_DIR/pegasus.conf \
    --sites tacc_wrangler \
    --output-site local \
    --dir work \
    --dax black-diamond.dax \
    --submit | tee plan.out


