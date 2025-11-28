import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from patient import Patient

class TestPatient(unittest.TestCase):
    def test_admit_discharge(self):
        p = Patient("John", 30, "Flu")
        self.assertTrue(p.is_admitted())
        p.discharge()
        self.assertFalse(p.is_admitted())

if __name__ == "__main__":
    unittest.main()
