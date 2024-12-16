from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_transaction():
    # Create two different accounts
    body_list = [
        {
            "name": "Mary Jane",
            "number": "0987654321",
            "balance": 200000,
        },
        {
            "name": "Angela Doe",
            "number": "1357911131",
            "balance": 300000,
        },
    ]

    for body in body_list:
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

    # Transfer money from one account to another
    transaction_body = {
        "sender_number": body_list[0]["number"],
        "receiver_number": body_list[1]["number"],
        "amount": 50000,
    }

    response = client.post(
        "/transaction",
        json=transaction_body,
    )

    content = response.json()
    transaction_id = content["data"]["id"]
    assert transaction_id is not None
    assert content["data"]["sender_number"] == transaction_body["sender_number"]
    assert content["data"]["receiver_number"] == transaction_body["receiver_number"]
    assert content["data"]["amount"] == transaction_body["amount"]
    assert content["status"] == 201
    assert content["message"] == "Transaction created successfully"

    # Check sender account
    response = client.get(
        f"/account/{body_list[0]['number']}",
    )

    content = response.json()
    assert content["data"]["name"] == body_list[0]["name"]
    assert content["data"]["number"] == body_list[0]["number"]
    assert (
        content["data"]["balance"]
        == body_list[0]["balance"] - transaction_body["amount"]
    )

    # Check receiver account
    response = client.get(
        f"/account/{transaction_body['receiver_number']}",
    )

    content = response.json()
    assert content["data"]["name"] == body_list[1]["name"]
    assert content["data"]["number"] == body_list[1]["number"]
    assert (
        content["data"]["balance"]
        == body_list[1]["balance"] + transaction_body["amount"]
    )

    # Get transaction by id
    response = client.get(
        f"/transaction/{transaction_id}",
    )

    content = response.json()
    assert content["data"]["id"] == transaction_id
    assert content["data"]["sender_number"] == transaction_body["sender_number"]
    assert content["data"]["receiver_number"] == transaction_body["receiver_number"]
    assert content["data"]["amount"] == transaction_body["amount"]
    assert content["status"] == 200
    assert content["message"] == "Transaction retrieved successfully"

    # List all transactions
    response = client.get(
        "/transaction",
    )

    content = response.json()

    for transaction in content["data"]:
        if transaction["id"] == transaction_id:
            assert transaction["sender_number"] == transaction_body["sender_number"]
            assert transaction["receiver_number"] == transaction_body["receiver_number"]
            assert transaction["amount"] == transaction_body["amount"]
            break
    assert content["status"] == 200
    assert content["message"] == "List of transactions retrieved successfully"
