import subprocess

# Install dependencies
def install_dependencies():
    subprocess.run(["pip3", "install", "psutil"])

# Run the hardware monitoring script
def run_monitor_script():
    subprocess.run(["python3", "hardware_monitor.py"])

# Main setup function
def setup_and_run():
    print("Installing dependencies...")
    install_dependencies()

    print("Dependencies installed. Running the hardware monitoring script...")
    run_monitor_script()

if __name__ == "__main__":
    setup_and_run()
