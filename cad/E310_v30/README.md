# E310 Rev.C / AD9361 — CAD v30
Board photographed: `23-E310B25-20`, MicroPhase ANTSDR E310 Rev.C.

- `ANTSDR_E310_photo_corrected_v30.step`: detailed **approximate** 3D CAD assembly, original STEP binary.
- `ANTSDR_E310_photo_corrected_v30.stl`: generated binary STL **from the same detailed STEP**, when workflow completes.
- `ANTSDR_E310_v30_CAD_bundle.zip`: generated package containing STEP, STL, SCAD and this README, when workflow completes.
- `export_step_to_stl.py`: exact pipeline using OpenCascade and mesh validation.
- `build_e310_photo_revision_v30.py`: prior model generator.
- `E310_RevC_photo_approx_v30.scad`: **separate simplified model**, not the source of the detailed STL.

Use [GitHub Actions: Export detailed E310 STEP to binary STL and ZIP](../../../../actions/workflows/build-e310-stl.yml) and choose **Run workflow** if it does not run automatically. The workflow must complete successfully before STL and ZIP appear here.

Geometry reference: MicroPhase E310 ES2 DXF, physical photos, PCB 100×60 mm, approximate 1.6 mm thick. Four SMA, RJ45, exactly two USB Type-C, microSD on reverse. The mechanical DXF is for ES2 and may not match this particular Rev.C. Position and fit of connectors and mounting holes **are not certified**: check real device before machining.
