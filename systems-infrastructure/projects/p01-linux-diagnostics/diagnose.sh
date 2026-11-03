#!/usr/bin/env bash
# P01 — intentionally read-only Linux diagnostics starter.
# Run on an isolated, personally owned or authorized Linux VM only.
# Does not persist output, mutate system settings, or invoke network clients.
set -u
export LC_ALL=C

usage() {
  printf '%s\n' 'Usage: bash diagnose.sh [--help]'
  printf '%s\n' 'Read-only local Linux diagnostic summary. No files are written.'
  printf '%s\n' 'Redact command output before publishing; process names can be sensitive.'
}

if [[ "${1:-}" == "--help" && $# -eq 1 ]]; then
  usage
  exit 0
fi
if (( $# > 0 )); then
  usage >&2
  exit 2
fi

if [[ "$(uname -s 2>/dev/null)" != "Linux" ]]; then
  printf '%s\n' 'ERROR: This starter supports Linux only.' >&2
  exit 2
fi

failures=0

section() {
  local label="$1"; shift
  local program="$1"; shift
  printf '\n=== %s ===\n' "$label"
  if ! command -v "$program" >/dev/null 2>&1; then
    printf 'WARN: command unavailable: %s\n' "$program" >&2
    failures=$((failures + 1))
    return
  fi
  if "$program" "$@"; then
    :
  else
    local status=$?
    printf 'WARN: %s exited with code %s\n' "$program" "$status" >&2
    failures=$((failures + 1))
  fi
}

printf '%s\n' 'P01 Linux System Diagnostics — read-only snapshot'
section 'UTC observation time' date -u '+%Y-%m-%dT%H:%M:%SZ'
section 'Kernel and machine' uname -srmo
section 'Uptime and load' uptime
section 'Memory allocation' free -h
section 'Filesystem capacity' df -hP
section 'Top processes by CPU (names may be sensitive)' ps -eo pid,comm,%cpu,%mem --sort=-%cpu
section 'Network socket summary (no remote connections)' ss -s

printf '\nCompleted with %s section warning(s).\n' "$failures"
if (( failures > 0 )); then
  exit 1
fi
exit 0
