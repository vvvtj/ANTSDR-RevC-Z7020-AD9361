# ANTSDR E310 Rev.C — CAD v30

Model for board marked `23-E310B25-20`. All files are for enclosure prototyping, NOT final machining tolerances.

- `ANTSDR_E310_photo_corrected_v30.step` — native STEP geometry, existing exact blob copied into this folder without text re-encoding.
- `E310_RevC_photo_approx_v30.scad` — simplified parametric OpenSCAD alternative; different detail level from STEP.
- `build_e310_photo_revision_v30.py` — Python generator source for detailed model.

STL v30 was produced in ChatGPT, but has not been uploaded to GitHub because available integration cannot read its binary bytes as a blob. Original downloadable STL is available from the conversation attachment. To regenerate locally, run the generator or export the STEP in FreeCAD (File > Export > STL).

## Geometry and caveats

PCB approximately 100 × 60 × 1.6 mm. Four SMA, RJ45, two USB Type-C (no micro-USB), microSD on reverse, shield and heatsink. Connector cutout dimensions and mounting hole centres need verification against the physical board before manufacturing. The official mechanical DXF is for E310 ES2, which may differ from this board revision.

Official DXF: https://github.com/MicroPhase/antsdr_doc_en/blob/master/mechanical/ANT_E310_ES2_Mechanical.dxf
