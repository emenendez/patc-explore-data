PATC GPS Rangers Data Notes
===========================

General
-------

Some of the data appears to have been generated by DeLorme Topo. This data includes elevation information; did it come from the GPS or from the software?

Top-level metadata
------------------

No pertinent info here
Geometry sub-elements: trk, wpt

one `<bin>` element with base64-encoded binary data

Track metadata
--------------

Relevant fields: name, desc
Time comes from individual points
desc is sometimes date, sometimes a useful description

Waypoint metadata
-----------------

Relevant attributes: lat, lon
Relevant fields: name, time, ele, desc, cmt
desc is sometimes date, sometimes a useful description
cmt appears to match desc
One waypoint links to a picture

extensions/gpxx:WaypointExtension/gpxx:Categories/gpxx:Category sometimes has interesting information
extensions/gpxx:WaypointExtension/wptx1:Samples sometimes has number of samples
