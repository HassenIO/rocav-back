import json
import pandas as pd

from model import model

def run(event, context):
    body = event["queryStringParameters"]
    reco = model(body["compTerit"], body["specialite"], body["domaine"])

    return {
        "statusCode": 200,
        "headers": {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Credentials": True,
        },
        "body": reco.to_json(orient='records')
    }


if __name__ == "__main__":
    run("", "")

