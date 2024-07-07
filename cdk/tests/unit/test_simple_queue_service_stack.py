import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk.python.src.sqs import SimpleQueueService

def test_queue_created():
    app = core.App()
    stack = SimpleQueueService(app, "TestStack")
    template = assertions.Template.from_stack(stack)

    # Check if the queue is created
    template.has_resource_properties("AWS::SQS::Queue", {
        "QueueName": "TestQueue"
    })  
