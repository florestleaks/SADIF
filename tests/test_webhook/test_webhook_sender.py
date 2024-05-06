import unittest
from unittest.mock import Mock, patch

import requests

from sadif.frameworks_drivers.notification.webhook import WebhookSender


class TestWebhookSender(unittest.TestCase):
    def setUp(self):
        self.valid_url = "https://dsa.requestcatcher.com/test"
        self.invalid_url = "invalid://url"
        self.timeout = 10
        self.max_retries = 3
        self.proxies = None
        self.success_callback = Mock()
        self.failure_callback = Mock()

    def test_valid_url_initialization(self):
        sender = WebhookSender(self.valid_url)
        self.assertEqual(sender.url, self.valid_url)

    def test_invalid_url_initialization(self):
        sender = WebhookSender(self.invalid_url)
        self.assertTrue(sender.validate_url())

    @patch("requests.request")
    def test_send_success(self, mock_request):
        mock_request.return_value.status_code = 200
        sender = WebhookSender(self.valid_url, success_callback=self.success_callback)
        sender.send({})
        self.success_callback.assert_called_once()

    @patch("requests.request")
    def test_send_failure_then_success(self, mock_request):
        # First two calls to request will raise an exception, third call will be successful
        mock_request.side_effect = [
            requests.exceptions.RequestException(),
            requests.exceptions.RequestException(),
            Mock(status_code=200),
        ]

        sender = WebhookSender(
            self.valid_url, max_retries=3, failure_callback=self.failure_callback
        )
        sender.send({})
        self.assertEqual(self.failure_callback.call_count, 2)
        self.success_callback.assert_not_called()

    @patch("requests.request")
    def test_send_failure_all_retries(self, mock_request):
        mock_request.side_effect = requests.exceptions.RequestException()

        sender = WebhookSender(
            self.valid_url, max_retries=3, failure_callback=self.failure_callback
        )
        with self.assertRaises(requests.exceptions.RequestException):
            sender.send({})
        self.assertEqual(self.failure_callback.call_count, 3)
        self.success_callback.assert_not_called()
