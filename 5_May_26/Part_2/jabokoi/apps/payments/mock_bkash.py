import random
import string

class MockBkashService:
    @staticmethod
    def initiate_payment(amount, callback_url):
        # Simulate bKash token generation and redirect URL
        payment_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        return {
            "status": "success",
            "paymentID": payment_id,
            "bkashURL": f"https://mock.bkash.com/checkout?paymentID={payment_id}",
        }

    @staticmethod
    def execute_payment(payment_id):
        # Simulate successful payment execution
        trx_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        return {
            "status": "success",
            "trxID": trx_id,
            "amount": random.randint(1000, 5000),
            "paymentTime": "2026-05-14T12:00:00.000 GMT+6"
        }
