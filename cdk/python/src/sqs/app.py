import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_sqs as sqs,
)
from constructs import Construct

class SqsStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the SQS queue
        queue = sqs.Queue(
            self, "MyQueue",
            queue_name="MyQueue",
            visibility_timeout=cdk.Duration.seconds(30),
            retention_period=cdk.Duration.days(4)
        )

class MyApp(cdk.App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        SqsStack(self, "SqsStack")

app = MyApp()
app.synth()
