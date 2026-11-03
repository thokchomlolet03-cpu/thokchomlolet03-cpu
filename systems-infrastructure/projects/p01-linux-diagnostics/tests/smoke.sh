#!/usr/bin/env bash
# Minimal, local, no-network smoke tests. Not a substitute for VM validation.
set -euo pipefail
cd "$(dirname "$0")/.."

bash -n diagnose.sh
bash diagnose.sh --help | grep -q 'Read-only local Linux'

set +e
bash diagnose.sh --invalid >/dev/null 2>&1
status=$?
set -e
if [[ $status -ne 2 ]]; then
  printf 'Unexpected invalid-option status: %s\n' "$status" >&2
  exit 1
fi

# Do not echo outputs into CI logs; they can contain machine process info.
output_file="$(mktemp)"
trap 'rm -f "$output_file"' EXIT
set +e
bash diagnose.sh >"$output_file" 2>/dev/null
status=$?
set -e
if [[ $status -ne 0 && $status -ne 1 ]]; then
  printf 'Unexpected diagnostic exit status: %s\n' "$status" >&2
  exit 1
fi
grep -q '^P01 Linux System Diagnostics' "$output_file"
grep -q '^Completed with' "$output_file"
printf 'P01 smoke tests passed (diagnostic exit=%s; 1 means missing/failing sections).\n' "$status"
