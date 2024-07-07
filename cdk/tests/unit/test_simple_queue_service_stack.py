import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk.python.src.sqs import SimpleQueueService

 def test_sqs_queue_created():
    app = cdk.App()
    stack = SimpleQueueServiceStack(app, "SimpleQueueServiceStack")
    template = assertions.Template.from_stack(stack)

    # Check if an SQS queue is created
    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })

    # Optionally check the queue name
    template.has_resource_properties("AWS::SQS::Queue", {
        "QueueName": "MySimpleQueue"
    })   
