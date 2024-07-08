import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    Duration
)
from constructs import Construct

class SimpleQueueServiceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the SQS queue
        queue = sqs.Queue(
            self, "MyQueue",
            visibility_timeout=Duration.seconds(300),
            queue_name="MySimpleQueue"
        )

app = cdk.App()
SimpleQueueServiceStack(app, "SimpleQueueServiceStack")
app.synth()
