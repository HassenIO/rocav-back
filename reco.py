import json

from model import model

def run(event, context):
    response = {
        "statusCode": 200,
        "result": model(event["compTerit"], event["specialite"], event["domaine"]).to_json(orient='records')
    }

    return response


if __name__ == "__main__":
    run("", "")

