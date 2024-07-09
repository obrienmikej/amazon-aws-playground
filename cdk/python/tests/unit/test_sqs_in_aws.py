import unittest
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class TestSQSQueue(unittest.TestCase):

    def setUp(self):
        # Initialize boto3 client for SQS
        self.sqs_client = boto3.client('sqs')

    def test_sqs_queue_exists(self):
        queue_name = "MyQueue"
        try:
            # Get the list of queues
            response = self.sqs_client.list_queues()

            # Check if the queue exists in the list of queues
            queue_urls = response.get('QueueUrls', [])
            queue_exists = any(queue_name in url for url in queue_urls)

            self.assertTrue(queue_exists, f"SQS Queue '{queue_name}' does not exist.")
        
        except NoCredentialsError:
            self.fail("AWS credentials not found.")
        except PartialCredentialsError:
            self.fail("Incomplete AWS credentials.")
        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == '__main__':
    unittest.main()
