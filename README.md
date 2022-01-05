# TACC Stampede2 Pegasus for GeoFlood

This is a comprehensive example of the GeoFlood workflow using the Pegasus workflow management system (WMS) for running on a login node on TACC's Stampede2 supercomputer. It is using a local HTCondor install for workflow/job management and Glite to transform HTCondor jobs into SLURM jobs. An overview of such a setup can be found in the [Pegasus Glite Documentation](https://pegasus.isi.edu/documentation/glite.php).

Currently, only one of the TACC Stampede2's submit nodes have the HTCondor/Glite stack (`login6.stampede2.tacc.utexas.edu`). *Please contact me if you need access to this node in order to use Pegasus on Stampede2.*

The workflow is the comprehensive GeoFlood workflow. Please note:

 * Queue configuration, walltime, and project name are defined in `sites.template.xml`. *If you do not use this workflow generator on Stampede2, you will need to update this file for it to run under your own set-up, user account, & allocation.*
 * Node/core requirements are set in `dax-generator.py`. This is to highlight that those requirements can change for the different jobs in the workflow. *You will need to modify the input/output filenames in this file in order to successfully run GeoFlood using Pegasus.*
 * `pegasus.conf` contains throttle settings for limiting the number of jobs going to SLURM
 
## Running the Example

Run `./submit.sh` do submit a new workflow run:

```
$ ./submit.sh

Work dir is /work/04950/dhl/stampede2/2021-11-08T155607-0500

2022.01.03 15:56:09.009 CDT:    
2022.01.03 15:56:09.014 CDT:   ----------------------------------------------------------------------- 
2022.01.03 15:56:09.020 CDT:   File for submitting this DAG to HTCondor           : geoflood-0.dag.condor.sub 
2022.01.03 15:56:09.025 CDT:   Log of DAGMan debugging messages                   : geoflood-0.dag.dagman.out 
2022.01.03 15:56:09.030 CDT:   Log of HTCondor library output                     : geoflood-0.dag.lib.out 
2022.01.03 15:56:09.035 CDT:   Log of HTCondor library error messages             : geoflood-0.dag.lib.err 
2022.01.03 15:56:09.041 CDT:   Log of the life of condor_dagman itself            : geoflood-0.dag.dagman.log 
2022.01.03 15:56:09.046 CDT:    
2022.01.03 15:56:09.051 CDT:   -no_submit given, not submitting DAG to HTCondor.  You can do this with: 
2022.01.03 15:56:09.062 CDT:   ----------------------------------------------------------------------- 
2022.01.03 15:56:09.795 CDT:   Your database is compatible with Pegasus version: 4.9.0dev 
2022.01.03 15:56:09.888 CDT:   Submitting to condor geoflood-0.dag.condor.sub 
2022.01.03 15:56:10.464 CDT:   Submitting job(s). 
2022.01.03 15:56:10.470 CDT:   1 job(s) submitted to cluster 96. 
2022.01.03 15:56:10.475 CDT:    
2022.01.03 15:56:10.480 CDT:   Your workflow has been started and is running in the base directory: 
2022.01.03 15:56:10.486 CDT:    
2022.01.03 15:56:10.491 CDT:     /work/04950/dhl/stampede2/2021-11-08T155607-0500/work/dhl/pegasus/geoflood/run0001 
2022.01.03 15:56:10.496 CDT:    
2022.01.03 15:56:10.501 CDT:   *** To monitor the workflow you can run *** 
2022.01.03 15:56:10.507 CDT:    
2022.01.03 15:56:10.512 CDT:     pegasus-status -l /work/04950/dhl/stampede2/2021-11-08T155607-0500/work/dhl/pegasus/geoflood/run0001 
2022.01.03 15:56:10.517 CDT:    
2022.01.03 15:56:10.522 CDT:   *** To remove your workflow run *** 
2022.01.03 15:56:10.528 CDT:    
2022.01.03 15:56:10.533 CDT:     pegasus-remove /work/04950/dhl/stampede2/2021-11-08T155607-0500/work/dhl/pegasus/geoflood/run0001 
2022.01.03 15:56:10.538 CDT:    
2022.01.03 15:56:11.329 CDT:   Time taken to execute is 2.378 seconds 
```

Monitor the workflow with the provided `pegasus-status ...` command.

Once the workfow is complete, you will find outputs under the work dir printed right after the `submit.sh` command.

## Modifications to the Stampede2 Setup

The following patch was applied to the HTCondor install on TACC Stampede2 to solve a few missing environment variables in the HTCondor/Glite SLURM submit environment:

```
--- /home/04950/dhl/slurm_submit.sh   2022-01-04 11:02:05.000000000 -0500
+++ /usr/libexec/condor/glite/bin/slurm_submit.sh       2022-01-04 13:10:02.827359647 -0500
@@ -78,6 +78,8 @@
 
 bls_add_job_wrapper
 
+export USER=`whoami`
+. /etc/profile.d/work_archive.sh
 
 ###############################################################
 # Submit the script
```

