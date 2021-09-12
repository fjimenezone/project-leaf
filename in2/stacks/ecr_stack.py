from aws_cdk import (
    core,
    aws_ecr as ecr
)

class EcrStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        registry = ecr.Repository(
            self,
            "Repository",
            repository_name="fastapi",
            removal_policy=core.RemovalPolicy.DESTROY
        )
