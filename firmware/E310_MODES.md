# Official E310 firmware and execution modes

Source: https://antsdr-docs.microphase.cn/en/latest/device_and_usage_manual/ANTSDR_E_Series_Module/ANTSDR_E_Series_Module.html

The official E310 documentation lists these **additional modes**. They are not necessarily unique flash images or independent source repositories:

1. **Standalone (no-OS)** — bare-metal FPGA/Zynq application workflow. Locate project files through E310 official Standalone guide before building.
2. **FMCOMMS** — Analog Devices FMCOMMS2/3/4 compatible bitstream/boot arrangements (historical E310 v1.0 release mentions FMCOMMS2/3/4 boot files).
3. **GNU Radio**, **MATLAB**, **libiio** — host software/interface paths; do not treat each as a separate flash firmware.
4. **OpenWiFi** — separate FPGA + Linux application, see upstream OpenWiFi project.
5. **Pluto-compatible IIO** — legacy `antsdr-fw` and newer `antsdr-fw-patch`.
6. **UHD** — latest official UHD firmware documentation explicitly mentions E200/E310V2, so E310 Rev.C is UNVERIFIED.

For each experiment write down PCB revision, AD9361 type, firmware tag/commit, `TARGET`, Vivado version, boot method, SD partition layout, backup/recovery, and tests. Do not flash builds for `e310v2` to Rev.C without proven hardware equivalence.

No vendor binaries have been copied into this repository; use `download_official.py` to retrieve GitHub Release assets from MicroPhase.
