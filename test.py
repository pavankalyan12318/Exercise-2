import requests

url = "https://reqres.in/api/users?page=2"  # You can change the endpoint if needed

response = requests.get(url)

def test_status_code():
    assert response.status_code == 200, f"Test Failed: Expected 200, but got {response.status_code}"
    print("Test Passed: Status code is 200")

if __name__ == "__main__":
    test_status_code()
