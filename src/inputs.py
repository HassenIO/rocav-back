import json
import sys
sys.path.append('./package')

from package import pandas

def run(event, context):
    df = pd.DataFrame([[1, 2], [3, 4]], columns=["a", "b"])
    body = {
        "message": "Serverless get inputs for front",
        "input": event
    }

    response = {
        "dataframe": df.to_json(orient='records'),
        "statusCode": 200,
        "body": json.dumps(body)
    }

    print(response)
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

if __name__ == "__main__":
    run("", "")

