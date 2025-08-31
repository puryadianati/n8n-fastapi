import requests
import json

# Test the API endpoints
base_url = "http://localhost:8000"

# Test 1: Health check
print("=== Testing Health Check ===")
try:
    response = requests.get(f"{base_url}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")

print()

# Test 2: Get available methods
print("=== Testing Available Methods ===")
try:
    response = requests.get(f"{base_url}/api/methods")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

print()

# Test 3: Create from list
print("=== Testing create_from_list ===")
test_command_1 = {
    "method": "create_from_list",
    "params": {
        "data": [120, 155, 132, 180, 201]
    }
}

try:
    response = requests.post(f"{base_url}/api/execute", json=test_command_1)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

print()

# Test 4: Create zeros array
print("=== Testing zeros ===")
test_command_2 = {
    "method": "zeros",
    "params": {
        "shape": 12
    }
}

try:
    response = requests.post(f"{base_url}/api/execute", json=test_command_2)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")

print()

# Test 5: Invalid command
print("=== Testing Invalid Command ===")
test_command_3 = {
    "method": "invalid_method",
    "params": {}
}

try:
    response = requests.post(f"{base_url}/api/execute", json=test_command_3)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Error: {e}")