# TACC Stampede2 Pegasus Example

This is an example Pegasus workflow for running on the login node on TACC Stampede2. It is using a local HTCondor install for workflow/job management and Glite to transform HTCondor jobs into SLURM jobs. An overview of such setups can be found in the [Pegasus Glite Documentation](https://pegasus.isi.edu/documentation/glite.php). Currently, only one of the TACC Stampede2's submit nodes have the HTCondor/Glite stack (`login6.stampede2.tacc.utexas.edu`)

The workflow is the typical Black Diamond example used in the Pegasus tutorial. Please note:

 * Queue configuration, walltime, and project name are defined in `sites.template.xml`. At the minimum, you need to update the project for the example to run under your own user account/allocation.
 * Node/core requirements are set in `dax-generator.py`. This is to highlight that those requirements can change for the different jobs in the workflow.
 * `pegasus.conf` contains throttle settings for limiting the number of jobs going to SLURM
 
## Running the Example

After updating the project setting in `sites.template.xml`, run `./submit.sh` do submit a new workflow run:

```
$ ./submit.sh

Work dir is /work/04950/dhl/stampede2/2021-11-08T155607-0500

2018.08.13 15:56:09.009 CDT:    
2018.08.13 15:56:09.014 CDT:   ----------------------------------------------------------------------- 
2018.08.13 15:56:09.020 CDT:   File for submitting this DAG to HTCondor           : diamond-0.dag.condor.sub 
2018.08.13 15:56:09.025 CDT:   Log of DAGMan debugging messages                   : diamond-0.dag.dagman.out 
2018.08.13 15:56:09.030 CDT:   Log of HTCondor library output                     : diamond-0.dag.lib.out 
2018.08.13 15:56:09.035 CDT:   Log of HTCondor library error messages             : diamond-0.dag.lib.err 
2018.08.13 15:56:09.041 CDT:   Log of the life of condor_dagman itself            : diamond-0.dag.dagman.log 
2018.08.13 15:56:09.046 CDT:    
2018.08.13 15:56:09.051 CDT:   -no_submit given, not submitting DAG to HTCondor.  You can do this with: 
2018.08.13 15:56:09.062 CDT:   ----------------------------------------------------------------------- 
2018.08.13 15:56:09.795 CDT:   Your database is compatible with Pegasus version: 4.9.0dev 
2018.08.13 15:56:09.888 CDT:   Submitting to condor diamond-0.dag.condor.sub 
2018.08.13 15:56:10.464 CDT:   Submitting job(s). 
2018.08.13 15:56:10.470 CDT:   1 job(s) submitted to cluster 96. 
2018.08.13 15:56:10.475 CDT:    
2018.08.13 15:56:10.480 CDT:   Your workflow has been started and is running in the base directory: 
2018.08.13 15:56:10.486 CDT:    
2018.08.13 15:56:10.491 CDT:     /work/04950/dhl/stampede2/2021-11-08T155607-0500/work/dhl/pegasus/diamond/run0001 
2018.08.13 15:56:10.496 CDT:    
2018.08.13 15:56:10.501 CDT:   *** To monitor the workflow you can run *** 
2018.08.13 15:56:10.507 CDT:    
2018.08.13 15:56:10.512 CDT:     pegasus-status -l /work/04950/dhl/stampede2/2021-11-08T155607-0500/work/dhl/pegasus/diamond/run0001 
2018.08.13 15:56:10.517 CDT:    
2018.08.13 15:56:10.522 CDT:   *** To remove your workflow run *** 
2018.08.13 15:56:10.528 CDT:    
2018.08.13 15:56:10.533 CDT:     pegasus-remove /work/04950/dhl/stampede2/2021-11-08T155607-0500/work/dhl/pegasus/diamond/run0001 
2018.08.13 15:56:10.538 CDT:    
2018.08.13 15:56:11.329 CDT:   Time taken to execute is 2.378 seconds 
```

Monitor the workflow with the provided `pegasus-status ...` command.

Once the workfow is complete, you will find outputs under the work dir printed right after the `submit.sh` command.

## Modifications to the Stampede2 Setup

The following patch was applied to the HTCondor install on TACC Stampede2 to solve a few missing environment variables in the HTCondor/Glite SLURM submit environment:

```
--- /home/04950/dhl/slurm_submit.sh   2021-11-08 11:02:05.000000000 -0500
+++ /usr/libexec/condor/glite/bin/slurm_submit.sh       2021-11-08 13:10:02.827359647 -0500
@@ -78,6 +78,8 @@
 
 bls_add_job_wrapper
 
+export USER=`whoami`
+. /etc/profile.d/work_archive.sh
 
 ###############################################################
 # Submit the script
```

