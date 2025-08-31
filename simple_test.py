import requests
import json

# Test the root endpoint first
try:
    response = requests.get("http://localhost:8000/")
    print("Root endpoint:")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
except Exception as e:
    print(f"Error testing root: {e}")

# Test our specific endpoints
endpoints = [
    "http://localhost:8000/api/methods",
    "http://localhost:8000/api/execute"
]

for endpoint in endpoints:
    try:
        if "methods" in endpoint:
            response = requests.get(endpoint)
        else:
            # Test execute endpoint
            test_data = {
                "method": "create_from_list",
                "params": {"data": [1, 2, 3]}
            }
            response = requests.post(endpoint, json=test_data)
        
        print(f"Endpoint: {endpoint}")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"Error Response: {response.text}")
        print("-" * 50)
    except Exception as e:
        print(f"Error testing {endpoint}: {e}")
        print("-" * 50)