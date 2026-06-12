import subprocess
import sys

def test_app_runs():
    result = subprocess.run([sys.executable, "app.py"], capture_output=True, text=True)
    assert result.returncode == 0, "App did not run successfully"
    assert "Cloud CI Pipeline Running" in result.stdout, "Wrong output"

if __name__ == "__main__":
    test_app_runs()
    print("Test passed!")