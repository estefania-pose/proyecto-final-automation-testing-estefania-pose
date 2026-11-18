# tests_behave/test_behave_suite.py
import sys
import subprocess
import pytest

@pytest.mark.bdd
def test_ejecutar_suite_bdd():
    """Wrapper para ejecutar Behave integrado dentro de Pytest usando el python actual."""
    result = subprocess.run(
        [sys.executable, "-m", "behave", "-f", "json", "-o", "reports/behave.json", "-f", "pretty"],
        capture_output=False
    )
    assert result.returncode == 0, "Uno o más escenarios BDD de Behave fallaron."