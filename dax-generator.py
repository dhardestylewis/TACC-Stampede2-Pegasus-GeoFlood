#!/usr/bin/env python

from Pegasus.DAX3 import *
import sys
import os

if len(sys.argv) != 2:
        print("Usage: %s PEGASUS_HOME" % (sys.argv[0]))
        sys.exit(1)

geoflood_dir = "/scratch/04950/dhlGeoFlood.sablake.git/"

# Create a abstract dag
geoflood = ADAG("geoflood")

# Add input file to the DAX-level replica catalog
sablake = File("ins/GIS/sablake/sablake_r2f.tif")
sablake.addPFN(PFN("file://" + geoflood_dir + "ins/GIS/sablake/sablake_r2f.tif", "local"))
geoflood.addFile(sablake)

# Add input file to the DAX-level replica catalog
flowline = File("ins/GIS/sablake/Flowline.shp")
flowline.addPFN(PFN("file://" + geoflood_dir + "ins/GIS/sablake/Flowline.shp", "local"))
geoflood.addFile(flowline)

# Add input file to the DAX-level replica catalog
catchment = File("ins/GIS/sablake/Catchment.shp")
catchment.addPFN(PFN("file://" + geoflood_dir + "ins/GIS/sablake/Catchment.shp", "local"))
geoflood.addFile(catchment)

# Add input file to the DAX-level replica catalog
comid_roughness = File("ins/Hydraulics/sablake/COMID_Roughness.csv")
comid_roughness.addPFN(PFN("file://" + geoflood_dir + "ins/Hydraulics/sablake/COMID_Roughness.csv", "local"))
geoflood.addFile(comid_roughness)

# Add input file to the DAX-level replica catalog
stage = File("ins/Hydraulics/sablake/stage.txt")
stage.addPFN(PFN("file://" + geoflood_dir + "ins/Hydraulics/sablake/stage.txt", "local"))
geoflood.addFile(stage)

# Add input file to the DAX-level replica catalog
nwm_forecast = File("ins/Hydraulics/sablake/stage.txt")
nwm_forecast.addPFN(PFN("file://" + geoflood_dir + "ins/NWM/sablake/imelda20190918_12pm.nc", "local"))
geoflood.addFile(nwm_forecast)

# Add executables to the DAX-level replica catalog
# In this case the binary is pegasus-keg, which is shipped with Pegasus, so we use
# the remote PEGASUS_HOME to build the path.
e_pitremove = Executable(namespace="geoflood", name="pitremove", version="Develop", installed=True)
e_pitremove.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_pitremove)

e_pygeonet_nonlinear_filter = Executable(namespace="geoflood", name="pygeonet_nonlinear_filter", version="main", installed=True)
e_pygeonet_nonlinear_filter.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_pygeonet_nonlinear_filter)

e_dinfflowdir = Executable(namespace="geoflood", name="dinfflowdir", version="Develop", installed=True)
e_dinfflowdir.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_dinfflowdir)

e_pygeonet_slope_curvature = Executable(namespace="geoflood", name="pygeonet_slope_curvature", version="main", installed=True)
e_pygeonet_slope_curvature.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_pygeonet_slope_curvature)

e_pygeonet_grass_py3 = Executable(namespace="geoflood", name="pygeonet_grass_py3", version="main", installed=True)
e_pygeonet_grass_py3.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_pygeonet_grass_py3)

#e_pygeonet_skeleton_definition = Executable(namespace="geoflood", name="pygeonet_skeleton_definition", version="main", installed=True)
#e_pygeonet_skeleton_definition.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
#geoflood.addExecutable(e_pygeonet_skeleton_definition)

#e_Network_Node_Reading = Executable(namespace="geoflood", name="Network_Node_Reading", version="main", installed=True)
#e_Network_Node_Reading.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
#geoflood.addExecutable(e_Network_Node_Reading)

e_Relative_Height_Estimation = Executable(namespace="geoflood", name="Relative_Height_Estimation", version="main", installed=True)
e_Relative_Height_Estimation.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_Relative_Height_Estimation)

#e_network_extraction = Executable(namespace="geoflood", name="Network_Extraction", version="main", installed=True)
#e_network_extraction.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
#geoflood.addExecutable(e_network_extraction)

e_Streamline_Segmentation = Executable(namespace="geoflood", name="Streamline_Segmentation", version="main", installed=True)
e_Streamline_Segmentation.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_Streamline_Segmentation)

e_dinfdistdown = Executable(namespace="geoflood", name="dinfdistdown", version="Develop", installed=True)
e_dinfdistdown.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_dinfdistdown)

e_grass_delineation_py3 = Executable(namespace="geoflood", name="Grass_Delineation_py3", version="main", installed=True)
e_grass_delineation_py3.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_grass_delineation_py3)

e_River_Attribute_Estimation = Executable(namespace="geoflood", name="River_Attribute_Estimation", version="main", installed=True)
e_River_Attribute_Estimation.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_River_Attribute_Estimation)

e_Network_Mapping = Executable(namespace="geoflood", name="Network_Mapping", version="main", installed=True)
e_Network_Mapping.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_Network_Mapping)

e_catchhydrogeo = Executable(namespace="geoflood", name="catchhydrogeo", version="Develop", installed=True)
e_catchhydrogeo.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_catchhydrogeo)

e_Hydraulic_Property_Postprocess = Executable(namespace="geoflood", name="Hydraulic_Property_Postprocess", version="main", installed=True)
e_Hydraulic_Property_Postprocess.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_Hydraulic_Property_Postprocess)

e_Forecast_Table = Executable(namespace="geoflood", name="Forecast_Table", version="main", installed=True)
e_Forecast_Table.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_Forecast_Table)

e_inunmap = Executable(namespace="geoflood", name="inunmap", version="Develop", installed=True)
e_inunmap.addPFN(PFN("file://" + sys.argv[1] + "pegasus_wrapper.sh", "local"))
geoflood.addExecutable(e_inunmap)

# Add job
pitremove = Job(namespace="geoflood", name="pitremove", version="Develop")
fel = File("ins/GIS/sablake/sablake_fel.tif")
pitremove.addArguments("-e taudem","'pitremove -z",sablake,"-fel",fel+"'")
pitremove.uses(sablake, link=Link.INPUT)
pitremove.uses(fel, link=Link.OUTPUT)
# required resources for the job
pitremove.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
pitremove.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(pitremove)

# Add job
pygeonet_nonlinear_filter = Job(namespace="geoflood", name="pygeonet_nonlinear_filter", version="main")
filtered = File("outs/GIS/sablake/PM_filtered_grassgis.tif")
pygeonet_nonlinear_filter.addArguments("-e geoflood","'python3",geoflood_dir+"GeoNet/pygeonet_nonlinear_filter.py'")
pygeonet_nonlinear_filter.uses(sablake, link=Link.INPUT)
pygeonet_nonlinear_filter.uses(filtered, link=Link.OUTPUT)
# required resources for the job
pygeonet_nonlinear_filter.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
pygeonet_nonlinear_filter.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(pygeonet_nonlinear_filter)

# Add job
pygeonet_grass_py3 = Job(namespace="geoflood", name="pygeonet_grass_py3", version="main")
fac = File("outs/GIS/sablake/sablake_fac.tif")
outlets = File("outs/GIS/sablake/sablake_outlets.tif")
basins = File("outs/GIS/sablake/sablake_basins.tif")
fdr = File("outs/GIS/sablake/sablake_fdr.tif")
pygeonet_grass_py3.addArguments("-e grass","-s",geoflood_dir+"/geoflood.sif","'python3",geoflood_dir+"GeoNet/pygeonet_grass_py3'")
pygeonet_grass_py3.uses(filtered, link=Link.INPUT)
pygeonet_grass_py3.uses(fac, link=Link.OUTPUT)
pygeonet_grass_py3.uses(outlets, link=Link.OUTPUT)
pygeonet_grass_py3.uses(basins, link=Link.OUTPUT)
pygeonet_grass_py3.uses(fdr, link=Link.OUTPUT)
# required resources for the job
pygeonet_grass_py3.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
pygeonet_grass_py3.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(pygeonet_grass_py3)

# Add job
pygeonet_slope_curvature = Job(namespace="geoflood", name="pygeonet_slope_curvature", version="main")
slope = File("outs/GIS/sablake/sablake_slope.tif")
curvature = File("outs/GIS/sablake/sablake_curvature.tif")
pygeonet_slope_curvature.addArguments("-e geoflood","'python3",geoflood_dir+"GeoNet/pygeonet_slope_curvature.py'")
pygeonet_slope_curvature.uses(filtered, link=Link.INPUT)
pygeonet_slope_curvature.uses(slope, link=Link.OUTPUT)
pygeonet_slope_curvature.uses(curvature, link=Link.OUTPUT)
# required resources for the job
pygeonet_slope_curvature.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
pygeonet_slope_curvature.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(pygeonet_slope_curvature)

## Add job
#pygeonet_skeleton_definition = Job(namespace="geoflood", name="pygeonet_skeleton_definition", version="main")
#skeleton = File("outs/GIS/sablake/sablake_skeleton.tif")
#curvatureskeleton = File("outs/GIS/sablake/sablake_curvatureskeleton.tif")
#flowskeleton = File("outs/GIS/sablake/sablake_flowskeleton.tif")
#pygeonet_skeleton_definition.addArguments("-e geoflood","python3 pygeonet_skeleton_definition.py")
#pygeonet_skeleton_definition.uses(filtered, link=Link.INPUT)
#pygeonet_skeleton_definition.uses(curvature, link=Link.INPUT)
#pygeonet_skeleton_definition.uses(fac, link=Link.INPUT)
#pygeonet_skeleton_definition.uses(skeleton, link=Link.OUTPUT)
#pygeonet_skeleton_definition.uses(curvatureskeleton, link=Link.OUTPUT)
#pygeonet_skeleton_definition.uses(flowskeleton, link=Link.OUTPUT)
## required resources for the job
#pygeonet_skeleton_definition.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
#pygeonet_skeleton_definition.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
#geoflood.addJob(pygeonet_skeleton_definition)

## Add job
#network_node_reading = Job(namespace="geoflood", name="Network_Node_Reading", version="main")
#endpoints = File("outs/GIS/sablake/sablake_endPoints.csv")
#network_node_reading.addArguments("-e geoflood","python3 Network_Node_Reading.py")
#network_node_reading.uses(flowline, link=Link.INPUT)
#network_node_reading.uses(endpoints, link=Link.OUTPUT)
## required resources for the job
#network_node_reading.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
#network_node_reading.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
#geoflood.addJob(network_node_reading)

# Add job
relative_height_estimation = Job(namespace="geoflood", name="Relative_Height_Estimation", version="main")
negahand = File("outs/GIS/sablake/sablake_NegaHand.tif")
nhdflowline = File("outs/GIS/sablake/sablake_nhdflowline.tif")
allocation = File("outs/GIS/sablake/sablake_Allocation.tif")
relative_height_estimation.addArguments("-e geoflood","'python3",geoflood_dir+"GeoFlood/Relative_Height_Estimation.py'")
relative_height_estimation.uses(flowline, link=Link.INPUT)
relative_height_estimation.uses(negahand, link=Link.OUTPUT)
relative_height_estimation.uses(nhdflowline, link=Link.OUTPUT)
relative_height_estimation.uses(allocation, link=Link.OUTPUT)
# required resources for the job
relative_height_estimation.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
relative_height_estimation.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(relative_height_estimation)

## Add job
#network_extraction = Job(namespace="geoflood", name="Network_Extraction", version="main")
#channelnetwork = File("outs/GIS/sablake/sablake_channelNetwork.shp")
#cost = File("outs/GIS/sablake/sablake_cost.tif")
#path = File("outs/GIS/sablake/sablake_path.tif")
#network_extraction.addArguments("-e geoflood","python3 Network_Extraction.py")
#network_extraction.uses(skeleton, link=Link.INPUT)
#network_extraction.uses(curvature, link=Link.INPUT)
#network_extraction.uses(fac, link=Link.INPUT)
#network_extraction.uses(endpoints, link=Link.INPUT)
#network_extraction.uses(negahand, link=Link.INPUT)
#network_extraction.uses(channelnetwork, link=Link.OUTPUT)
#network_extraction.uses(cost, link=Link.OUTPUT)
#network_extraction.uses(path, link=Link.OUTPUT)
## required resources for the job
#network_extraction.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
#network_extraction.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
#geoflood.addJob(network_extraction)

# Add job
dinfflowdir = Job(namespace="geoflood", name="dinfflowdir", version="Develop")
slp = File("outs/GIS/sablake/sablake_slp.tif")
ang = File("outs/GIS/sablake/sablake_ang.tif")
dinfflowdir.addArguments("-e taudem","'dinfflowdir -fel",fel,"-slp",slp,"-ang",ang+"'")
dinfflowdir.uses(fel, link=Link.INPUT)
dinfflowdir.uses(slp, link=Link.OUTPUT)
dinfflowdir.uses(ang, link=Link.OUTPUT)
# required resources for the job
dinfflowdir.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
dinfflowdir.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(dinfflowdir)

# Add job
dinfdistdown = Job(namespace="geoflood", name="dinfdistdown", version="Develop")
hand = File("outs/GIS/sablake/sablake_hand.tif")
dinfdistdown.addArguments("-e taudem","'dinfdistdown -src",nhdflowline,"-fel",fel,"-slp",slp,"-ang",ang,"-dd",hand,"-m ave v'")
dinfdistdown.uses(nhdflowline, link=Link.INPUT)
dinfdistdown.uses(fel, link=Link.INPUT)
dinfdistdown.uses(slp, link=Link.INPUT)
dinfdistdown.uses(ang, link=Link.INPUT)
dinfdistdown.uses(hand, link=Link.OUTPUT)
# required resources for the job
dinfdistdown.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
dinfdistdown.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(dinfdistdown)

# Add job
streamline_segmentation = Job(namespace="geoflood", name="Streamline_Segmentation", version="main")
channelsegment = File("outs/GIS/sablake/sablake_channelSegment.shp")
streamline_segmentation.addArguments("-e geoflood","'python3",geoflood_dir+"GeoFlood/Streamline_Segmentation.py -nhd'")
streamline_segmentation.uses(channelnetwork, link=Link.INPUT)
streamline_segmentation.uses(channelsegment, link=Link.OUTPUT)
# required resources for the job
streamline_segmentation.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
streamline_segmentation.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(streamline_segmentation)

# Add job
grass_delineation_py3 = Job(namespace="geoflood", name="Grass_Delineation_py3", version="main")
segmentcatchmenttif = File("outs/GIS/sablake/sablake_segmentCatchment.tif")
grass_delineation_py3.addArguments("-e grass","-s",geoflood_dir+"/geoflood.sif","'python3",geoflood_dir+"GeoFlood/Grass_Delineation_py3.py'")
grass_delineation_py3.uses(channelsegment, link=Link.INPUT)
grass_delineation_py3.uses(fdr, link=Link.INPUT)
grass_delineation_py3.uses(segmentcatchmenttif, link=Link.OUTPUT)
# required resources for the job
grass_delineation_py3.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
grass_delineation_py3.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(grass_delineation_py3)

# Add job
river_attribute_estimation = Job(namespace="geoflood", name="River_Attribute_Estimation", version="main")
river_attribute = File("outs/Hydraulics/sablake/sablake_River_Attribute.txt")
segmentcatchmentshp = File("outs/GIS/sablake/sablake_segmentCatchment.shp")
river_attribute_estimation.addArguments("-e geoflood","'python3",geoflood_dir+"GeoFlood/River_Attribute_Estimation.py'")
river_attribute_estimation.uses(channelsegment, link=Link.INPUT)
river_attribute_estimation.uses(segmentcatchmenttif, link=Link.INPUT)
river_attribute_estimation.uses(river_attribute, link=Link.OUTPUT)
river_attribute_estimation.uses(segmentcatchmentshp, link=Link.OUTPUT)
# required resources for the job
river_attribute_estimation.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
river_attribute_estimation.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(river_attribute_estimation)

# Add job
catchhydrogeo = Job(namespace="geoflood", name="catchhydrogeo", version="Develop")
hydroprop_basetable = File("outs/Hydraulics/sablake/hydroprop-basetable.csv")
catchhydrogeo.addArguments("-e taudem","'catchhydrogeo -catchlist",river_attribute,"-h",stage,"-slp",slp,"-catch",segmentcatchmenttif,"-hand",hand,"-table",hydroprop_basetable+"'")
catchhydrogeo.uses(river_attribute, link=Link.INPUT)
catchhydrogeo.uses(stage, link=Link.INPUT)
catchhydrogeo.uses(slp, link=Link.INPUT)
catchhydrogeo.uses(segmentcatchmenttif, link=Link.INPUT)
catchhydrogeo.uses(hand, link=Link.INPUT)
catchhydrogeo.uses(hydroprop_basetable, link=Link.OUTPUT)
# required resources for the job
catchhydrogeo.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
catchhydrogeo.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(catchhydrogeo)

# Add job
network_mapping = Job(namespace="geoflood", name="Network_Mapping", version="main")
networkmapping = File("outs/Hydraulics/sablake/sablake_networkMapping.csv")
network_mapping.addArguments("-e geoflood","'python3",geoflood_dir+"GeoFlood/Network_Mapping.py'")
network_mapping.uses(catchment, link=Link.INPUT)
network_mapping.uses(segmentcatchmentshp, link=Link.INPUT)
network_mapping.uses(networkmapping, link=Link.OUTPUT)
# required resources for the job
network_mapping.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
network_mapping.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(network_mapping)

# Add job
hydraulic_property_postprocess = Job(namespace="geoflood", name="Hydraulic_Property_Postprocess", version="main")
hydroprop_fulltable = File("outs/Hydraulics/sablake/hydroprop-fulltable.csv")
hydraulic_property_postprocess.addArguments("-e geoflood","'python3",geoflood_dir+"GeoFlood/Hydraulic_Property_Postprocess.py'")
hydraulic_property_postprocess.uses(networkmapping, link=Link.INPUT)
hydraulic_property_postprocess.uses(comid_roughness, link=Link.INPUT)
hydraulic_property_postprocess.uses(hydroprop_basetable, link=Link.INPUT)
hydraulic_property_postprocess.uses(hydroprop_fulltable, link=Link.OUTPUT)
# required resources for the job
hydraulic_property_postprocess.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
hydraulic_property_postprocess.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(hydraulic_property_postprocess)

# Add job
forecast_table = Job(namespace="geoflood", name="Forecast_Table", version="main")
nwm_conusnc = File("outs/NWM/sablake/imelda20190918_12pm.nc")
nwm_conuscsv = File("outs/NWM/sablake/imelda20190918_12pm.csv")
forecast_table.addArguments("-e geoflood","'python3",geoflood_dir+"GeoFlood/Forecast_Table.py",nwm_forecast+"'")
forecast_table.uses(nwm_forecast, link=Link.INPUT)
forecast_table.uses(networkmapping, link=Link.INPUT)
forecast_table.uses(hydroprop_fulltable, link=Link.INPUT)
forecast_table.uses(nwm_conusnc, link=Link.OUTPUT)
forecast_table.uses(nwm_conuscsv, link=Link.OUTPUT)
# required resources for the job
forecast_table.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
forecast_table.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(forecast_table)

# Add job
inunmap = Job(namespace="geoflood", name="inunmap", version="Develop")
nwm_inunmap = File("outs/Inundation/sablake/sablake_NWM_inunmap.tif")
inunmap.addArguments("-e taudem","'inunmap -forecast",nwm_conusnc,"-catch",segmentcatchmenttif,"-hand",hand,"-mapfile",nwm_inunmap+"'")
inunmap.uses(nwm_conusnc, link=Link.INPUT)
inunmap.uses(segmentcatchmenttif, link=Link.INPUT)
inunmap.uses(hand, link=Link.INPUT)
inunmap.uses(nwm_inunmap, link=Link.OUTPUT)
# required resources for the job
inunmap.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
inunmap.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(inunmap)

# Add control-flow dependencies
geoflood.addDependency(Dependency(parent=pitremove, child=pygeonet_nonlinear_filter))
geoflood.addDependency(Dependency(parent=pitremove, child=dinfflowdir))
geoflood.addDependency(Dependency(parent=pygeonet_nonlinear_filter, child=pygeonet_grass_py3))
geoflood.addDependency(Dependency(parent=pygeonet_nonlinear_filter, child=pygeonet_slope_curvature))
geoflood.addDependency(Dependency(parent=pygeonet_grass_py3, child=grass_delineation_py3))
#geoflood.addDependency(Dependency(parent=pygeonet_grass_py3, child=pygeonet_skeleton_definition))
#geoflood.addDependency(Dependency(parent=pygeonet_grass_py3, child=network_extraction))
#geoflood.addDependency(Dependency(parent=pygeonet_slope_curvature, child=pygeonet_skeleton_definition))
#geoflood.addDependency(Dependency(parent=pygeonet_slope_curvature, child=network_extraction))
#geoflood.addDependency(Dependency(parent=pygeonet_skeleton_definition, child=network_extraction))
#geoflood.addDependency(Dependency(parent=network_node_reading, child=network_extraction))
#geoflood.addDependency(Dependency(parent=relative_height_estimation, child=network_extraction))
#geoflood.addDependency(Dependency(parent=network_extraction, child=streamline_segmentation))
#geoflood.addDependency(Dependency(parent=network_extraction, child=dinfdistdown))
geoflood.addDependency(Dependency(parent=dinfflowdir, child=dinfdistdown))
geoflood.addDependency(Dependency(parent=streamline_segmentation, child=grass_delineation_py3))
geoflood.addDependency(Dependency(parent=streamline_segmentation, child=network_mapping))
geoflood.addDependency(Dependency(parent=dinfdistdown, child=inunmap))
geoflood.addDependency(Dependency(parent=grass_delineation_py3, child=river_attribute_estimation))
geoflood.addDependency(Dependency(parent=river_attribute_estimation, child=catchhydrogeo))
geoflood.addDependency(Dependency(parent=network_mapping, child=forecast_table))
geoflood.addDependency(Dependency(parent=network_mapping, child=hydraulic_property_postprocess))
geoflood.addDependency(Dependency(parent=catchhydrogeo, child=hydraulic_property_postprocess))
geoflood.addDependency(Dependency(parent=hydraulic_property_postprocess, child=forecast_table))
geoflood.addDependency(Dependency(parent=forecast_table, child=inunmap))

# Write the DAX to stdout
geoflood.writeXML(sys.stdout)


