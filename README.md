# Hardware Monitoring and Notification

This Python script provides a hardware monitoring solution that calculates the average usage of CPU, RAM, network, and disk over a specified window of time. It sends notifications using the ntfy service, allowing you to stay informed about your system's performance.

## Prerequisites

1. **Python 3:**
   - If you don't have Python 3 installed, follow the steps at [python.org](https://www.python.org/downloads/) to install Python 3.

2. **ntfy Application:**
   - Install the ntfy application on your Android or iOS device. [ntfy App Website](https://ntfy.sh/)

   - Create a new topic in the ntfy app by clicking on the "+" button and setting a name for your topic.

## Configuration

1. Open the `hardware_monitor.py` file.
2. Locate the line:

    ```python
    NTFY_TOPIC_URL = "ntfy.sh/<your-topic-name>"
    ```

3. Replace `<your-topic-name>` with the name of the topic you created in the ntfy app.

## Usage

1. Run the setup script:

    ```bash
    python3 setup_and_run.py
    ```

   This script installs the required dependencies and starts the hardware monitoring script.

2. The hardware monitoring script will run continuously, collecting data and sending notifications at the end of each specified window.

## Stopping the Monitoring

- To stop the monitoring script, use "Ctrl + C" in the terminal where the script is running.
