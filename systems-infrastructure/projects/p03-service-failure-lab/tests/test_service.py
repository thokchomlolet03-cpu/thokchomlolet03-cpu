"""Offline tests with synthetic data and loopback traffic only."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "service.py"
CONFIG = ROOT / "config.json"


class ServiceTests(unittest.TestCase):
    def test_missing_configuration(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "missing.json"
            result = subprocess.run([sys.executable, str(SCRIPT), "--config", str(target)],
                                    capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 2)
            self.assertIn("CONFIG_ERROR", result.stderr)

    def test_invalid_json(self):
        with tempfile.TemporaryDirectory() as folder:
            invalid = Path(folder) / "bad.json"
            invalid.write_text("not-json", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), "--config", str(invalid)],
                                    capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 2)

    def test_port_conflict(self):
        primary = subprocess.Popen([sys.executable, str(SCRIPT), "--config", str(CONFIG),
                                    "--port", "0"], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)
        try:
            ready = primary.stdout.readline().strip()
            self.assertTrue(ready.startswith("READY http://127.0.0.1:"), ready)
            port = ready.split(":")[-1].split("/")[0]
            secondary = subprocess.run([sys.executable, str(SCRIPT), "--config", str(CONFIG),
                                        "--port", port], capture_output=True, text=True, timeout=5)
            self.assertEqual(secondary.returncode, 3)
            self.assertIn("BIND_ERROR", secondary.stderr)
        finally:
            primary.terminate()
            primary.communicate(timeout=5)

    def test_local_health_response(self):
        primary = subprocess.Popen([sys.executable, str(SCRIPT), "--config", str(CONFIG),
                                    "--port", "0"], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, text=True)
        try:
            ready = primary.stdout.readline().strip()
            self.assertTrue(ready.startswith("READY http://127.0.0.1:"), ready)
            with urlopen(ready.removeprefix("READY "), timeout=3) as response:
                self.assertEqual(response.status, 200)
                self.assertEqual(json.loads(response.read())["message"], "synthetic-lab-ok")
        finally:
            primary.terminate()
            primary.communicate(timeout=5)


if __name__ == "__main__":
    unittest.main()
