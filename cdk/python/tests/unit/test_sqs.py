import aws_cdk as cdk
import aws_cdk.assertions as assertions

from cdk.python.src.sqs.app import SimpleQueueServiceStack

def test_sqs_queue_created():
    app = cdk.App()
    stack = SimpleQueueServiceStack(app, "TestStack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "QueueName": "MySimpleQueue",
        "VisibilityTimeout": 300
    })
