import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk.python.src.sqs import SimpleQueueService

def test_sqs_queue_created():
    app = core.App()
    stack = MyStack(app, "MyTestStack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "QueueName": "MyTestQueue",
        "VisibilityTimeout": 300
    })

def test_sqs_queue_retention_period():
    app = core.App()
    stack = MyStack(app, "MyTestStack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "MessageRetentionPeriod": 345600  # 4 days in seconds
    })

def test_sqs_queue_max_message_size():
    app = core.App()
    stack = MyStack(app, "MyTestStack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "MaximumMessageSize": 1024
    })

def test_sqs_queue_encryption():
    app = core.App()
    stack = MyStack(app, "MyTestStack")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "KmsMasterKeyId": "alias/aws/sqs"  # KMS managed key alias
    })