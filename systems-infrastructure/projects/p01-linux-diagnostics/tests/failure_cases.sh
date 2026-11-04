#!/usr/bin/env bash
# Non-destructive Bash dependency failure-path test (no test files created).
set -euo pipefail
cd -- "$(dirname -- "$0")/.."
# Intentional exported stub is called by the child Bash, not visibly in this file.
# shellcheck disable=SC2317
ss() { return 23; }
export -f ss
set +e
result="$(bash diagnose.sh 2>&1)"
status=$?
set -e
unset -f ss
if [[ "$status" != 1 ]] || ! grep -Fq 'WARN: ss exited with code 23' <<<"$result" || ! grep -Fq 'Completed with 1 section warning(s).' <<<"$result"; then
  printf 'FAIL: expected isolated failing-ss detection and nonzero diagnostic status\n' >&2
  exit 1
fi
printf '%s\n' 'PASS: intentionally failed ss is surfaced and produces diagnostic exit 1.'
