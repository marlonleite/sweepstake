from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class RaffleApiTest(APITestCase):
    """
    RaffleApiTest APITestCase
    """

    def setUp(self):
        self.data = {
            "items": [
                "maria socorro",
                "jose padilha",
                "pedro de lara",
                "simone turo",
                "fred cuma",
                "magno jose",
                "ryan pelo"
            ]
        }

        self.url = reverse('raffle')

    def test_raffle_items(self):
        """
        Ensure we can raffle items.
        """

        response = self.client.post(self.url, self.data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
