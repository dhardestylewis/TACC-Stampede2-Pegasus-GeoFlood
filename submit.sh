#!/bin/bash

set -e

TOP_DIR=`dirname $0`
export TOP_DIR=`cd $TOP_DIR && pwd`
export RUN_ID=`date --iso-8601='seconds' | sed 's/://g'`
export WORK_DIR=$WORK/$RUN_ID

export PEGASUS_HOME=/home1/00384/rynge/software/pegasus-4.9.3
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
export PEGASUS_TACC=/work2/04950/dhl/stampede2/TACC-Stampede2-Pegasus-GeoFlood
./dax-generator.py $PEGASUS_TACC > $WORK_DIR/geoflood.dax

# plan and submit the  workflow
cd $WORK_DIR
pegasus-plan \
    --conf $TOP_DIR/pegasus.conf \
    --sites tacc_wrangler \
    --output-site local \
    --dir work \
    --dax geoflood.dax \
    --submit | tee plan.out


