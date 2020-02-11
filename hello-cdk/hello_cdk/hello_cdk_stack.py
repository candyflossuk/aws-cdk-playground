from aws_cdk import (
    aws_s3 as s3,
    aws_rds as rds,  # TODO build example based on https://gist.github.com/candyflossuk/b22e2eb407fb4e51524cf16e56b9da3c
    core
)


class HelloCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self,
                           "MyFirstBucket",
                           versioned=True,)
