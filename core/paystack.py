from django.conf import settings
import requests


class PayStack:
    # PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
    PAYSTACK_SECRET_KEY = "pk_test_db7eb580c0015ee09205de7791906de5b11d108d"
    base_url = "https://api.paystack.co"


    def verify_payment(self, ref, *args, **kwargs):
        path = f"/transaction/verify/{ref}"

        headers = {
            "Authorization": "Bearer sk_test_1ffdac633a99e7eb980b1a681a60f106f8c3d555",
            "Content-Type": 'application/json',

        }
        url = self.base_url + path
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return response_data["status"], response_data['data']
        response_data = response.json()
        return response_data["status"], response_data["message"]

