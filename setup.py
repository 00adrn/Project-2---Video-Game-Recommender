#just an optional setup script, generated using GenAI
import os
import sys
import subprocess

venv_name = "venv"
requirements_file = "requirements.txt"

# Check if venv already exists
if os.path.exists(venv_name):
    print(f"Virtual environment '{venv_name}' already exists.")
else:
    print(f"Creating virtual environment '{venv_name}'...")
    subprocess.run([sys.executable, "-m", "venv", venv_name])
    print("Created.")

# Path to pip inside the venv
pip_path = os.path.join(venv_name, "Scripts" if os.name == "nt" else "bin", "pip")

# Install requirements if file exists
if os.path.exists(requirements_file):
    print(f"Installing packages from '{requirements_file}'...")
    subprocess.run([pip_path, "install", "-r", requirements_file])
    print("Packages installed.")
else:
    print("No requirements.txt found. Skipping package installation.")

# Show activation instructions
if os.name == "nt":
    activate_cmd = f"{venv_name}\\Scripts\\activate.bat"
else:
    activate_cmd = f"source {venv_name}/bin/activate"

print(f"\nTo activate your environment, run:\n\n    {activate_cmd}\n")