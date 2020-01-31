# aws-cdk-playground
A collection of CDK examples used to build various cloud resources in AWS

# hello world - cdk

Set up credentials

`export AWS_DEFAULT_REGION=us-east-2`

`export AWS_ACCESS_KEY_ID=xxxxxxxxxxx`

`export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxx`

`mkdir hello-cdk`

`cd hello-cdk`

`cdk init app --language=python`

activate the virtual environment

`source .env/bin/activate`

`pip install -r requirements.txt`

change the instantiation in app.py to
`HelloCdkStack(app, "HelloCdkStack")`

add the resources required in place of the comment

`cdk synth`

`cdk deploy`

make some changes - and show the changes using diff

`cdk diff`

`cdk deploy`

get rid of the app resources

`cdk destroy`
