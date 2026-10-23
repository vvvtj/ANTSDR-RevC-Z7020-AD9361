#!/usr/bin/env bash
set -euo pipefail
base="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$base/upstream"
cd "$base/upstream"
clone() {
  local folder="$1" url="$2"
  if [[ -d "$folder/.git" ]]; then echo "Existing $folder — skipping"; return; fi
  git clone --recursive "$url" "$folder"
}
clone antsdr-fw https://github.com/MicroPhase/antsdr-fw.git
clone antsdr-fw-patch https://github.com/MicroPhase/antsdr-fw-patch.git
clone antsdr_uhd https://github.com/MicroPhase/antsdr_uhd.git
clone openwifi https://github.com/open-sdr/openwifi.git
echo 'Source checkouts fetched. Read firmware/README.md before choosing a target.'
