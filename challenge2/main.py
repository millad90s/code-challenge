import subprocess
import sys

# Arguments give from command
args = sys.argv[1:]

# Create command for run to method1
command = ["python3", "seprated-odd-even-number.py"] + args

# Process to run command
result = subprocess.run(command, stdout=subprocess.PIPE)

# Show result
print(result.stdout.decode())
