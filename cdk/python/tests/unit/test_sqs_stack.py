import unittest
from aws_cdk import (
    Stack,
    App,
    assertions,
    aws_sqs as sqs,
    Duration
)
from constructs import Construct

class SqsStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the SQS queue
        queue = sqs.Queue(
            self, "MyQueue",
            queue_name="MyQueue",
            visibility_timeout=Duration.seconds(30),
            retention_period=Duration.days(4)
        )

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        SqsStack(self, "SqsStack")

class TestSqsStack(unittest.TestCase):

    def setUp(self):
        self.app = App()
        self.stack = SqsStack(self.app, "SqsStack")

    def test_queue_created(self):
        template = assertions.Template.from_stack(self.stack)

        # Check if the SQS Queue resource is present
        template.resource_count_is("AWS::SQS::Queue", 1)

        # Verify the properties of the SQS Queue
        template.has_resource_properties("AWS::SQS::Queue", {
            "QueueName": "MyQueue",
            "VisibilityTimeout": 30,
            "MessageRetentionPeriod": 345600  # 4 days in seconds
        })

if __name__ == '__main__':
    unittest.main()
