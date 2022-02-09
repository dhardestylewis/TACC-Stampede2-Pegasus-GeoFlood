#!/usr/bin/env python

from Pegasus.DAX3 import *
import sys
import os

if len(sys.argv) != 2:
        print("Usage: %s PEGASUS_HOME" % (sys.argv[0]))
        sys.exit(1)

# Create a abstract dag
geoflood = ADAG("geoflood")

# Add input file to the DAX-level replica catalog
dem = File("GeoInputs/GIS/my_project/dem.tif")
dem.addPFN(PFN("file://" + os.getcwd() + "/GeoInputs/GIS/my_project/dem.tif", "local"))
geoflood.addFile(dem)

# Add input file to the DAX-level replica catalog
flowline = File("GeoInputs/GIS/my_project/Flowline.shp")
flowline.addPFN(PFN("file://" + os.getcwd() + "/GeoInputs/GIS/my_project/Flowline.shp", "local"))
geoflood.addFile(flowline)

# Add input file to the DAX-level replica catalog
catchment = File("GeoInputs/GIS/my_project/Catchment.shp")
catchment.addPFN(PFN("file://" + os.getcwd() + "/GeoInputs/GIS/my_project/Catchment.shp", "local"))
geoflood.addFile(catchment)

# Add input file to the DAX-level replica catalog
comid_roughness = File("GeoInputs/Hydraulics/my_project/COMID_Roughness.csv")
comid_roughness.addPFN(PFN("file://" + os.getcwd() + "/GeoInputs/Hydraulics/my_project/COMID_Roughness.csv", "local"))
geoflood.addFile(comid_roughness)

# Add input file to the DAX-level replica catalog
stage = File("GeoInputs/Hydraulics/my_project/stage.txt")
stage.addPFN(PFN("file://" + os.getcwd() + "/GeoInputs/Hydraulics/my_project/stage.txt", "local"))
geoflood.addFile(stage)

# Add executables to the DAX-level replica catalog
# In this case the binary is pegasus-keg, which is shipped with Pegasus, so we use
# the remote PEGASUS_HOME to build the path.
e_pitremove = Executable(namespace="geoflood", name="pitremove", version="Develop", installed=False)
e_pitremove.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_pitremove)

e_pygeonet_nonlinear_filter = Executable(namespace="geoflood", name="pygeonet_nonlinear_filter", version="main", installed=False)
e_pygeonet_nonlinear_filter.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_pygeonet_nonlinear_filter)

e_dinfflowdir = Executable(namespace="geoflood", name="dinfflowdir", version="Develop", installed=False)
e_dinfflowdir.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_dinfflowdir)

e_pygeonet_slope_curvature = Executable(namespace="geoflood", name="pygeonet_slope_curvature", version="main", installed=False)
e_pygeonet_slope_curvature.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_pygeonet_slope_curvature)

e_pygeonet_grass_py3 = Executable(namespace="geoflood", name="pygeonet_grass_py3", version="main", installed=False)
e_pygeonet_grass_py3.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_pygeonet_grass_py3)

e_pygeonet_skeleton_definition = Executable(namespace="geoflood", name="pygeonet_skeleton_definition", version="main", installed=False)
e_pygeonet_skeleton_definition.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_pygeonet_skeleton_definition)

e_Network_Node_Reading = Executable(namespace="geoflood", name="Network_Node_Reading", version="main", installed=False)
e_Network_Node_Reading.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_Network_Node_Reading)

e_Relative_Height_Estimation = Executable(namespace="geoflood", name="Relative_Height_Estimation", version="main", installed=False)
e_Relative_Height_Estimation.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_Relative_Height_Estimation)

e_network_extraction = Executable(namespace="geoflood", name="Network_Extraction", version="main", installed=False)
e_network_extraction.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_network_extraction)

e_Streamline_Segmentation = Executable(namespace="geoflood", name="Streamline_Segmentation", version="main", installed=False)
e_Streamline_Segmentation.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_Streamline_Segmentation)

e_dinfdistdown = Executable(namespace="geoflood", name="dinfdistdown", version="Develop", installed=False)
e_dinfdistdown.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_dinfdistdown)

e_grass_delineation_py3 = Executable(namespace="geoflood", name="Grass_Delineation_py3", version="main", installed=False)
e_grass_delineation_py3.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_grass_delineation_py3)

e_River_Attribute_Estimation = Executable(namespace="geoflood", name="River_Attribute_Estimation", version="main", installed=False)
e_River_Attribute_Estimation.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_River_Attribute_Estimation)

e_Network_Mapping = Executable(namespace="geoflood", name="Network_Mapping", version="main", installed=False)
e_Network_Mapping.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_Network_Mapping)

e_catchhydrogeo = Executable(namespace="geoflood", name="catchhydrogeo", version="Develop", installed=False)
e_catchhydrogeo.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_catchhydrogeo)

e_Hydraulic_Property_Postprocess = Executable(namespace="geoflood", name="Hydraulic_Property_Postprocess", version="main", installed=False)
e_Hydraulic_Property_Postprocess.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_Hydraulic_Property_Postprocess)

e_Forecast_Table = Executable(namespace="geoflood", name="Forecast_Table", version="main", installed=False)
e_Forecast_Table.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_Forecast_Table)

e_inunmap = Executable(namespace="geoflood", name="inunmap", version="Develop", installed=False)
e_inunmap.addPFN(PFN("file://" + sys.argv[1] + "/bin/pegasus-keg", "local"))
geoflood.addExecutable(e_inunmap)

# Add a preprocess job
pitremove = Job(namespace="geoflood", name="pitremove", version="Develop")
fel = File("GeoInputs/GIS/my_project/dem_fel.tif")
pitremove.addArguments("-a pitremove","-T5","-i",dem,"-o",fel)
pitremove.uses(dem, link=Link.INPUT)
pitremove.uses(fel, link=Link.OUTPUT)
# required resources for the job
pitremove.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
pitremove.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(pitremove)

# Add left Findrange job
pygeonet_nonlinear_filter = Job(namespace="geoflood", name="pygeonet_nonlinear_filter", version="main")
filtered = File("GeoOutputs/GIS/my_project/PM_filtered_grassgis.tif")
pygeonet_nonlinear_filter.addArguments("-a pygeonet_nonlinear_filter","-T5","-i",dem,"-o",filtered)
pygeonet_nonlinear_filter.uses(dem, link=Link.INPUT)
pygeonet_nonlinear_filter.uses(filtered, link=Link.OUTPUT)
# required resources for the job
pygeonet_nonlinear_filter.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
pygeonet_nonlinear_filter.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(pygeonet_nonlinear_filter)

# Add left Findrange job
pygeonet_grass_py3 = Job(namespace="geoflood", name="pygeonet_grass_py3", version="main")
fac = File("GeoOutputs/GIS/my_project/dem_fac.tif")
outlets = File("GeoOutputs/GIS/my_project/dem_outlets.tif")
basins = File("GeoOutputs/GIS/my_project/dem_basins.tif")
fdr = File("GeoOutputs/GIS/my_project/dem_fdr.tif")
pygeonet_grass_py3.addArguments("-a pygeonet_grass_py3","-T5","-i",filtered,"-o",fac,outlets,basins,fdr)
pygeonet_grass_py3.uses(filtered, link=Link.INPUT)
pygeonet_grass_py3.uses(fac, link=Link.OUTPUT)
pygeonet_grass_py3.uses(outlets, link=Link.OUTPUT)
pygeonet_grass_py3.uses(basins, link=Link.OUTPUT)
pygeonet_grass_py3.uses(fdr, link=Link.OUTPUT)
# required resources for the job
pygeonet_grass_py3.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
pygeonet_grass_py3.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(pygeonet_grass_py3)

# Add left Findrange job
pygeonet_slope_curvature = Job(namespace="geoflood", name="pygeonet_slope_curvature", version="main")
slope = File("GeoOutputs/GIS/my_project/dem_slope.tif")
curvature = File("GeoOutputs/GIS/my_project/dem_curvature.tif")
pygeonet_slope_curvature.addArguments("-a pygeonet_slope_curvature","-T5","-i",filtered,"-o",slope,curvature)
pygeonet_slope_curvature.uses(filtered, link=Link.INPUT)
pygeonet_slope_curvature.uses(slope, link=Link.OUTPUT)
pygeonet_slope_curvature.uses(curvature, link=Link.OUTPUT)
# required resources for the job
pygeonet_slope_curvature.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
pygeonet_slope_curvature.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(pygeonet_slope_curvature)

# Add left Findrange job
pygeonet_skeleton_definition = Job(namespace="geoflood", name="pygeonet_skeleton_definition", version="main")
skeleton = File("GeoOutputs/GIS/my_project/dem_skeleton.tif")
curvatureskeleton = File("GeoOutputs/GIS/my_project/dem_curvatureskeleton.tif")
flowskeleton = File("GeoOutputs/GIS/my_project/dem_flowskeleton.tif")
pygeonet_skeleton_definition.addArguments("-a pygeonet_skeleton_definition","-T5","-i",filtered,curvature,fac,"-o",skeleton,curvatureskeleton,flowskeleton)
pygeonet_skeleton_definition.uses(filtered, link=Link.INPUT)
pygeonet_skeleton_definition.uses(curvature, link=Link.INPUT)
pygeonet_skeleton_definition.uses(fac, link=Link.INPUT)
pygeonet_skeleton_definition.uses(skelton, link=Link.OUTPUT)
pygeonet_skeleton_definition.uses(curvatureskeleton, link=Link.OUTPUT)
pygeonet_skeleton_definition.uses(flowskeleton, link=Link.OUTPUT)
# required resources for the job
pygeonet_skeleton_definition.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
pygeonet_skeleton_definition.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(pygeonet_skeleton_definition)

# Add left Findrange job
network_node_reading = Job(namespace="geoflood", name="Network_Node_Reading", version="main")
endpoints = File("GeoOutputs/GIS/my_project/dem_endPoints.csv")
network_node_reading.addArguments("-a network_node_reading","-T5","-i",flowline,"-o",endpoints)
network_node_reading.uses(flowline, link=Link.INPUT)
network_node_reading.uses(endpoints, link=Link.OUTPUT)
# required resources for the job
network_node_reading.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
network_node_reading.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(network_node_reading)

# Add left Findrange job
relative_height_estimation = Job(namespace="geoflood", name="Relative_Height_Estimation", version="main")
negahand = File("GeoOutputs/GIS/my_project/dem_NegaHand.tif")
nhdflowline = File("GeoOutputs/GIS/my_project/dem_nhdflowline.tif")
allocation = File("GeoOutputs/GIS/my_project/dem_Allocation.tif")
relative_height_estimation.addArguments("-a relative_height_estimation","-T5","-i",flowline,"-o",negahand,nhdflowline,allocation)
relative_height_estimation.uses(flowline, link=Link.INPUT)
relative_height_estimation.uses(negahand, link=Link.OUTPUT)
relative_height_estimation.uses(nhdflowline, link=Link.OUTPUT)
relative_height_estimation.uses(allocation, link=Link.OUTPUT)
# required resources for the job
relative_height_estimation.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
relative_height_estimation.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(relative_height_estimation)

# Add left Findrange job
network_extraction = Job(namespace="geoflood", name="Network_Extraction", version="main")
channelnetwork = File("GeoOutputs/GIS/my_project/dem_channelNetwork.shp")
cost = File("GeoOutputs/GIS/my_project/dem_cost.tif")
path = File("GeoOutputs/GIS/my_project/dem_path.tif")
network_extraction.addArguments("-a network_extraction","-T5","-i",skeleton,curvature,fac,endpoints,negahand,"-o",channelnetwork,cost,path)
network_extraction.uses(skeleton, link=Link.INPUT)
network_extraction.uses(curvature, link=Link.INPUT)
network_extraction.uses(fac, link=Link.INPUT)
network_extraction.uses(endpoints, link=Link.INPUT)
network_extraction.uses(negahand, link=Link.INPUT)
network_extraction.uses(channelnetwork, link=Link.OUTPUT)
network_extraction.uses(cost, link=Link.OUTPUT)
network_extraction.uses(path, link=Link.OUTPUT)
# required resources for the job
network_extraction.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
network_extraction.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(network_extraction)

# Add right Findrange job
dinfflowdir = Job(namespace="geoflood", name="dinfflowdir", version="Develop")
slp = File("GeoOutputs/GIS/my_project/dem_slp.tif")
ang = File("GeoOutputs/GIS/my_project/dem_ang.tif")
dinfflowdir.addArguments("-a findrange","-T5","-i",fel,"-o",slp,ang)
dinfflowdir.uses(fel, link=Link.INPUT)
dinfflowdir.uses(slp, link=Link.OUTPUT)
dinfflowdir.uses(ang, link=Link.OUTPUT)
# required resources for the job
dinfflowdir.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
dinfflowdir.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(dinfflowdir)

# Add right Findrange job
dinfdistdown = Job(namespace="geoflood", name="dinfdistdown", version="Develop")
hand = File("GeoOutputs/GIS/my_project/dem_hand.tif")
dinfdistdown.addArguments("-a findrange","-T5","-i",path,fel,slp,ang,"-o",hand)
dinfdistdown.uses(path, link=Link.INPUT)
dinfdistdown.uses(fel, link=Link.INPUT)
dinfdistdown.uses(slp, link=Link.INPUT)
dinfdistdown.uses(ang, link=Link.INPUT)
dinfdistdown.uses(hand, link=Link.OUTPUT)
# required resources for the job
dinfdistdown.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
dinfdistdown.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(dinfdistdown)

# Add right Findrange job
streamline_segmentation = Job(namespace="geoflood", name="Streamline_Segmentation", version="main")
channelsegment = File("GeoOutputs/GIS/my_project/dem_channelSegment.shp")
streamline_segmentation.addArguments("-a streamline_segmentation","-T5","-i",channelnetwork,"-o",channgelsegment)
streamline_segmentation.uses(channelnetwork, link=Link.INPUT)
streamline_segmentation.uses(channelsegment, link=Link.OUTPUT)
# required resources for the job
streamline_segmentation.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
streamline_segmentation.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(streamline_segmentation)

# Add right Findrange job
grass_delineation_py3 = Job(namespace="geoflood", name="Grass_Delineation_py3", version="main")
segmentcatchmenttif = File("GeoOutputs/GIS/my_project/dem_segmentCatchment.tif")
grass_delineation_py3.addArguments("-a grass_delineation_py3","-T5","-i",channelsegment,fdr,"-o",segmentcatchmenttif)
grass_delineation_py3.uses(channelsegment, link=Link.INPUT)
grass_delineation_py3.uses(fdr, link=Link.INPUT)
grass_delineation_py3.uses(segmentcatchmenttif, link=Link.OUTPUT)
# required resources for the job
grass_delineation_py3.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
grass_delineation_py3.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(grass_delineation_py3)

# Add right Findrange job
river_attribute_estimation = Job(namespace="geoflood", name="River_Attribute_Estimation", version="main")
river_attribute = File("GeoOutputs/Hydraulics/my_project/dem_River_Attribute.txt")
segmentcatchmentshp = File("GeoOutputs/GIS/my_project/dem_segmentCatchment.shp")
river_attribute_estimation.addArguments("-a river_attribute_estimation","-T5","-i",channelsegment,segmentcatchmenttif,"-o",river_attribute,segmentcatchmentshp)
river_attribute_estimation.uses(channelsegment, link=Link.INPUT)
river_attribute_estimation.uses(segmentcatchmenttif, link=Link.INPUT)
river_attribute_estimation.uses(river_attribute, link=Link.OUTPUT)
river_attribute_estimation.uses(segmentcatchmentshp, link=Link.OUTPUT)
# required resources for the job
river_attribute_estimation.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
river_attribute_estimation.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(river_attribute_estimation)

# Add right Findrange job
catchhydrogeo = Job(namespace="geoflood", name="catchhydrogeo", version="Develop")
hydroprop_basetable = File("GeoOutputs/Hydraulics/my_project/hydroprop-basetable.csv")
catchhydrogeo.addArguments("-a catchhydrogeo","-T5","-i",river_attribute,stage,slp,segmentcatchmenttif,hand,"-o",hydroprop_basetable)
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

# Add right Findrange job
network_mapping = Job(namespace="geoflood", name="Network_Mapping", version="main")
networkmapping = File("GeoOutputs/Hydraulics/my_project/dem_networkMapping.csv")
network_mapping.addArguments("-a network_mapping","-T5","-i",catchment,"-o",networkmapping)
network_mapping.uses(catchment, link=Link.INPUT)
network_mapping.uses(networkmapping, link=Link.OUTPUT)
# required resources for the job
network_mapping.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
network_mapping.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(network_mapping)

# Add right Findrange job
hydraulic_property_postprocess = Job(namespace="geoflood", name="Hydraulic_Property_Postprocess", version="main")
hydroprop_fulltable = File("GeoOutputs/Hydraulics/my_project/hydroprop-fulltable.csv")
hydraulic_property_postprocess.addArguments("-a hydraulic_property_postprocess","-T5","-i",networkmapping,comid_roughness,hydroprop_basetable,"-o",hydroprop_fulltable)
hydraulic_property_postprocess.uses(networkmapping, link=Link.INPUT)
hydraulic_property_postprocess.uses(comid_roughness, link=Link.INPUT)
hydraulic_property_postprocess.uses(hydroprop_basetable, link=Link.INPUT)
hydraulic_property_postprocess.uses(hydroprop_fulltable, link=Link.OUTPUT)
# required resources for the job
hydraulic_property_postprocess.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
hydraulic_property_postprocess.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(hydraulic_property_postprocess)

# Add right Findrange job
forecast_table = Job(namespace="geoflood", name="Forecast_Table", version="main")
nwm_conusnc = File("GeoOutputs/NWM/my_project/nwm.....conus.nc")
forecast_table.addArguments("-a forecast_table","-T5","-i",networkmapping,comid_roughness,hydroprop_basetable,"-o",hydroprop_fulltable)
forecast_table.uses(networkmapping, link=Link.INPUT)
forecast_table.uses(comid_roughness, link=Link.INPUT)
forecast_table.uses(hydroprop_basetable, link=Link.INPUT)
forecast_table.uses(hydroprop_fulltable, link=Link.OUTPUT)
# required resources for the job
forecast_table.addProfile(Profile(Namespace.PEGASUS, key="nodes", value="1"))
forecast_table.addProfile(Profile(Namespace.PEGASUS, key="cores", value="47"))
geoflood.addJob(forecast_table)

# Add right Findrange job
inunmap = Job(namespace="geoflood", name="inunmap", version="Develop")
nwm_inunmap = File("GeoOutputs/Inundation/my_project/dem_NWM_inunmap.tif")
inunmap.addArguments("-a inunmap","-T5","-i",nwm_conusnc,segmentcatchmenttif,hand,"-o",nwm_inunmap)
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
geoflood.addDependency(Dependency(parent=pygeonet_grass_py3, child=pygeonet_skeleton_definition))
geoflood.addDependency(Dependency(parent=pygeonet_grass_py3, child=network_extraction))
geoflood.addDependency(Dependency(parent=pygeonet_slope_curvature, child=pygeonet_skeleton_definition))
geoflood.addDependency(Dependency(parent=pygeonet_slope_curvature, child=network_extraction))
geoflood.addDependency(Dependency(parent=pygeonet_skeleton_definition, child=network_extraction))
geoflood.addDependency(Dependency(parent=network_node_reading, child=network_extraction))
geoflood.addDependency(Dependency(parent=relative_height_estimation, child=network_extraction))
geoflood.addDependency(Dependency(parent=network_extraction, child=streamline_segmentation))
geoflood.addDependency(Dependency(parent=network_extraction, child=dinfdistdown))
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


