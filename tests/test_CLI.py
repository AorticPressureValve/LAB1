import subprocess

class test_CLI:
    def test_cli_calc(self):
        result = subprocess.run(["python", "-m", "toolkit", "calc", "2+2"], capture_output = True, text = True, cwd = "src")

        assert result.returncode == 0


    def test_cli_convert_error(self):
        result = subprocess.run(["python", "-m", "toolkit", "convert", "1.5", "--from", "km", "--to", "kg"],capture_output=True,text=True,cwd="src")

        assert result.returncode == 2