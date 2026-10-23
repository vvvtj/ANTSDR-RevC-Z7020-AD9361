# ANTSDR E310 Rev.C — enclosure clearance CAD

Board: **MicroPhase ANTSDR E310**, photo marking `23-E310B25-20`, AD9361, Zynq-7020. This is an approximate **board assembly model** for enclosure prototyping. The user's board has **exactly two USB Type-C sockets**, one Ethernet, four SMA and a microSD on the opposite face.

## Files
- `E310_RevC_photo_approx_v30.scad` — parametric OpenSCAD model, independent of proprietary parts.
- The higher-detail STEP/STL models were generated locally from the official MicroPhase E310 ES2 DXF and the six user photos. **Do not manufacture close-tolerance connector cutouts from the approximations until measured.**

Coordinates in mm: X=0 USB/Ethernet end; X=100 SMA end; board 100×60×1.6 mm assumed. Components are photo-positioned, some heights allowed ±2 mm. The connector bodies have approximate dimensions; SMA, USB and RJ45 positions should be validated with calipers or manufacturer drawings. Mounting holes in SCAD are provisional.

Official source drawing: https://github.com/MicroPhase/antsdr_doc_en/blob/master/mechanical/ANT_E310_ES2_Mechanical.dxf

To export mesh: `openscad -o E310_RevC_photo_approx_v30.stl E310_RevC_photo_approx_v30.scad`
