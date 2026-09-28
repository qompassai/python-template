"""Smoke test for the hello-world example."""

import subprocess
import sys


def test_hello_runs():
    r = subprocess.run([sys.executable, "src/00_hello.py"],
                       capture_output=True, text=True)
    assert r.returncode == 0
    assert "Hello" in r.stdout
