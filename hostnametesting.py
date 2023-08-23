# test_switch.py
import pytest
from netmiko import ConnectHandler

# Replace these with your actual router credentials
RouterIP = "192.168.59.8"
Username = "cisco"
Password = "cisco123!"
Device_type = "cisco_xe"  # Adjust this based on your router's OS

def check_vlan_configuration(router_ip, username, password, expected_hostname):
    # Connect to the switch using Netmiko
    net_connect = ConnectHandler(
    device_type=Device_type,
    ip=RouterIP,
    username=Username,
    password=Password,
    )

    try:
        current_hostname = net_connect.find_prompt()

        # Close the SSH connection
        net_connect.disconnect()

        return expected_hostname in current_hostname

    except Exception as e:
        print(f"Error: {e}")
        return False

# Define the fixtures to provide the router's credentials
@pytest.fixture
def router_ip():
    #return "192.168.59.8" 
    return RouterIP

@pytest.fixture
def username():
    #return "cisco" 
    return Username

@pytest.fixture
def password():
    #return "cisco123!"
    return Password

@pytest.fixture
def device_type():
    #return "cisco_xe" 
    return Device_type

# The pytest test function
@pytest.mark.parametrize("hostname", ["CSRouter45"])
def test_vlan_configuration(router_ip, username, password, hostname):
    assert check_vlan_configuration(router_ip, username, password, hostname)
