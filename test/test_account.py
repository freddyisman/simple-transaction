from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_account():
    # Create new account balance
    body = {
        "name": "John Doe",
        "number": "1234567890",
        "balance": 100000,
    }

    response = client.post(
        "/account",
        json=body,
    )

    content = response.json()
    assert content["data"]["name"] == body["name"]
    assert content["data"]["number"] == body["number"]
    assert content["data"]["balance"] == body["balance"]
    assert content["status"] == 201
    assert content["message"] == "Account created successfully"

    # Get account by number
    account_number = content["data"]["number"]
    response = client.get(
        f"/account/{account_number}",
    )

    content = response.json()
    assert content["data"]["name"] == body["name"]
    assert content["data"]["number"] == body["number"]
    assert content["data"]["balance"] == body["balance"]
    assert content["status"] == 200
    assert content["message"] == "Account retrieved successfully"

    # List all accounts
    response = client.get(
        "/account",
    )

    content = response.json()
    for account in content["data"]:
        if account["number"] == account_number:
            assert account["name"] == body["name"]
            assert account["number"] == body["number"]
            assert account["balance"] == body["balance"]
            break
    assert content["status"] == 200
    assert content["message"] == "List of accounts retrieved successfully"
