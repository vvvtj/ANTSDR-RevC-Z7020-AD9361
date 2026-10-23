#!/usr/bin/env python3
"""Convert the detailed STEP to binary STL and reproducible ZIP, using OpenCascade."""
from pathlib import Path
from OCP.STEPControl import STEPControl_Reader
from OCP.IFSelect import IFSelect_RetDone
from OCP.BRepMesh import BRepMesh_IncrementalMesh
from OCP.StlAPI import StlAPI_Writer
import struct, zipfile, hashlib

folder=Path(__file__).resolve().parent
step=folder/"ANTSDR_E310_photo_corrected_v30.step"
stl=folder/"ANTSDR_E310_photo_corrected_v30.stl"
zip_path=folder/"ANTSDR_E310_v30_CAD_bundle.zip"
reader=STEPControl_Reader()
assert reader.ReadFile(str(step)) == IFSelect_RetDone, "STEP read failed"
assert reader.TransferRoots() > 0, "STEP has no transferable roots"
shape=reader.OneShape()
assert not shape.IsNull(), "No shape"
BRepMesh_IncrementalMesh(shape, 0.15, False, 0.3, True)
writer=StlAPI_Writer()
writer.ASCIIMode=False
assert writer.Write(shape,str(stl)), "STL write failed"
raw=stl.read_bytes()
assert len(raw)>=84, "STL too short"
count=struct.unpack_from("<I",raw,80)[0]
assert count>0 and len(raw)==84+50*count, "Invalid binary STL"
with zipfile.ZipFile(zip_path,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for item in (step,stl,folder/"E310_RevC_photo_approx_v30.scad",folder/"README.md"):
        archive.write(item,arcname=item.name)
with zipfile.ZipFile(zip_path) as archive:
    assert archive.testzip() is None, "ZIP CRC failed"
for item in (step,stl,zip_path):
    print(item.name, item.stat().st_size, hashlib.sha256(item.read_bytes()).hexdigest())
print("STL triangles:",count)
