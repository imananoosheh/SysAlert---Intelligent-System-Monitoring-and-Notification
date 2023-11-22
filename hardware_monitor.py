import time
import psutil
import subprocess

NTFY_TOPIC_URL="ntfy.sh/<your-topic-name>"

# Function to calculate average usage for a given window
def calculate_average_usage(window_data):
    total_cpu = sum(window_data['cpu'])
    total_ram = sum(window_data['ram'])
    total_network = sum(window_data['network'])
    total_disk = sum(window_data['disk'])
    num_samples = len(window_data['cpu'])
    
    avg_cpu = total_cpu / num_samples
    avg_ram = total_ram / num_samples
    avg_network = total_network / num_samples
    avg_disk = total_disk / num_samples
    
    return avg_cpu, avg_ram, avg_network, avg_disk

# Function to send notification using nfty
def send_notification(avg_cpu, avg_ram, avg_network, avg_disk):
    message = f"Average Usage:\nCPU: {avg_cpu:.2f}%\nRAM: {avg_ram:.2f}%\nNetwork: {avg_network:.2f} MB\nDISK: {avg_disk:.2f}MB"
    # POSTing the message via curl commnad
    subprocess.run(["curl", "-d", message, NTFY_TOPIC_URL])

# Main function for monitoring and notification
def monitor_hardware(window_size, window_interval):
    window_data = {'cpu': [], 'ram': [], 'network': [], 'disk': []}
    
    try:
        while True:
            # Collect hardware usage data
            cpu_percent = psutil.cpu_percent()
            ram_percent = psutil.virtual_memory().percent
            network_traffic = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            total_byte_read_and_write = psutil.disk_io_counters().read_bytes + psutil.disk_io_counters().write_bytes

            # Append data to the current window
            window_data['cpu'].append(cpu_percent)
            window_data['ram'].append(ram_percent)
            window_data['network'].append(network_traffic / (1024 * 1024))  # Convert to MB
            window_data['disk'].append(total_byte_read_and_write / (1024 * 1024)) # Convert to MB

            # Check if the window has reached its duration
            if len(window_data['cpu']) == window_size:
                # Calculate average usage
                avg_cpu, avg_ram, avg_network, avg_disk = calculate_average_usage(window_data)
                
                # Send notification
                send_notification(avg_cpu, avg_ram, avg_network, avg_disk)

                # Reset window data
                window_data = {'cpu': [], 'ram': [], 'network': [], 'disk': []}

            time.sleep(window_interval)
    
    except KeyboardInterrupt:
        subprocess.run(["curl", "-d", "Monitoring stopped by admin.", NTFY_TOPIC_URL])
        print("Monitoring stopped by admin.")

if __name__ == "__main__":
    # Set the window size and interval (in seconds)
    # 30 times of 1 second sleep sends average of 30 records every 30 seconds
    window_size = 30  # You can adjust this based on your preference
    window_interval = 1  # Adjust as needed

    monitor_hardware(window_size, window_interval)
