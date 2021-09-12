from aws_cdk import core
from stacks.ecr_stack import EcrStack

app = core.App()

ecr_registry = EcrStack(app, "Repository")
app.synth()
