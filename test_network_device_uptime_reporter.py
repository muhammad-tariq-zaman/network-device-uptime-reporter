import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import report

def row(d, days):
    return {"device": d, "uptime_days": str(days)}

class TestDeviceUptime(unittest.TestCase):
    def test_long_uptime(self):
        self.assertEqual(report([row("SW1", 400)])[0][2], "LONG UPTIME")
    def test_ok(self):
        self.assertEqual(report([row("SW1", 90)])[0][2], "OK")
    def test_longest_first(self):
        r = report([row("A", 10), row("B", 500)])
        self.assertEqual(r[0][0], "B")
    def test_boundary_ok(self):
        self.assertEqual(report([row("SW1", 365)])[0][2], "OK")
