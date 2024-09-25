import boto3
import os

def delete_lambda_function(function_name):
    client = boto3.client('lambda', 
                          aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                          region_name=os.getenv('AWS_REGION', 'us-east-1'))

    # Delete the Lambda function
    try:
        response = client.delete_function(FunctionName=function_name)
        print(f"Successfully deleted Lambda function: {function_name}")
    except Exception as e:
        print(f"Error deleting Lambda function: {e}")

if __name__ == "__main__":
    lambda_function_name = os.getenv('LAMBDA_FUNCTION_NAME')
    if lambda_function_name:
        delete_lambda_function(lambda_function_name)
    else:
        print("Please set the LAMBDA_FUNCTION_NAME environment variable.")

if __name__ == "__main__":

    username = "leticiacb1"
    function_name = "wc_" + username

    delete_lambda_function(function_name)