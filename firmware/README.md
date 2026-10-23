# ANTSDR E310 Rev.C / AD9361 — firmware source catalog

Hardware in this project: **MicroPhase E310 Rev.C, PCB 23-E310B25-20**, AD9361, Zynq-7020.

## Official sources

| Family | Upstream | Role | Board target |
|---|---|---|---|
| Classic Pluto-compatible IIO | https://github.com/MicroPhase/antsdr-fw | Legacy Pluto/IIO images: SD, DFU | `ant` (verify Rev.C) |
| Current Pluto-compatible IIO | https://github.com/MicroPhase/antsdr-fw-patch | Updated firmware, release archives, Buildroot | `ant` (verify Rev.C) |
| UHD | https://github.com/MicroPhase/antsdr_uhd | UHD host and firmware; confirm actual hardware target | E200/E310V2 in latest docs; **not assumed compatible with Rev.C** |
| OpenWiFi | https://github.com/open-sdr/openwifi | Wi-Fi FPGA/Linux stack; official E310 documentation | `antsdr` (E310/ANT), verify bitstream/boot |
| Official user documentation | https://antsdr-docs.microphase.cn/en/latest/device_and_usage_manual/ANTSDR_E_Series_Module/ANTSDR_E_Series_Module.html | Device-specific guides | E310 section |

## Official release versions discovered
- Classic `antsdr-fw`: `e310_v1.0`, `e310_v1.1`, `e310_v1.1_rf_switch`, `e310_v1.2` (e310_v1.3 release title points to v1.2 tag; check API).
- Updated `antsdr-fw-patch`: `v0.34`, `v0.38`, `v0.39`, `antsdr_mesh`.
- Additional historical and future releases can be downloaded with `download_official.py` (discovers GitHub Releases API).

## Fetch (on Linux / WSL)
```sh
bash firmware/fetch_sources.sh
python3 firmware/download_official.py --list
python3 firmware/download_official.py --download
```
The scripts DO NOT build or flash hardware. Downloads go into `firmware/upstream/` and `firmware/releases/`; these directories are gitignored.
Downloads include all upstream release assets for the two official IIO firmware repositories (which may include binaries for other boards). Select the E310/ANT artifact only after inspection.

## Important
- **E310V2/E316 is not interchangeable with E310 Rev.C**. No flashing of E310V2 images to Rev.C unless verified.
- `DFU`, `SD`, `BOOT.BIN`, `bitstream`, `rootfs` describe image types, not necessarily distinct firmware families.
- Never update bootloader or FPGA bitstream without an independently tested recovery method.
- Check licenses of each upstream repo before redistribution.
- This project tracks official sources rather than committing huge binaries or cloning third-party histories into one repository.
- No firmware was compiled, validated on hardware, or flashed by this commit.

## Build pointers
Legacy `antsdr-fw` documents Vivado 2019.1 and `TARGET=ant`, then `make` and `make sdimg`. Updated `antsdr-fw-patch` documents Vivado 2023.2 for v0.39. UHD firmware directory documents 2019.1. Follow matching upstream instructions for each version.
