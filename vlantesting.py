# test_switch.py
import pytest
from netmiko import ConnectHandler

# Replace these with your actual switch credentials
switch_ip = "192.168.56.9"
username = "admin"
password = "Bryton123"
device_type = "cisco_nxos_ssh"  # Adjust this based on your switch's OS

def check_vlan_configuration(switch_ip, username, password, vlan_id):
    # Connect to the switch using Netmiko
    net_connect = ConnectHandler(
    device_type="cisco_nxos",
    ip="192.168.56.9",
    username="admin",
    password="Bryton123",
    )

    try:
        # net_connect = ConnectHandler(**switch)
        # Send the command to retrieve VLAN information
        output = net_connect.send_command("show vlan")

        # Check if VLAN ID is in the output
        vlan_found = f"{vlan_id} " in output

        # Close the SSH connection
        net_connect.disconnect()

        print(vlan_found)

        return vlan_found

    except Exception as e:
        print(f"Error: {e}")
        return False

# Define the 'switch_ip' fixture to provide the switch IP address
@pytest.fixture
def switch_ip():
    return "192.168.56.9" 

@pytest.fixture
def username():
    return "admin" 

@pytest.fixture
def password():
    return "Bryton123"

@pytest.fixture
def device_type():
    return "cisco_nxos" 


# The pytest test function
@pytest.mark.parametrize("vlan_id", [100])  # Add more VLAN IDs if needed
def test_vlan_configuration(switch_ip, username, password, vlan_id):
    assert check_vlan_configuration(switch_ip, username, password, vlan_id)
