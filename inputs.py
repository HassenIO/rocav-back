import json
import sys
import os

# pathToPackage = os.path.dirname(os.path.abspath(__file__)) + '/package'
# sys.path.append('./MyFunctionDependencies.zip')

import pandas as pd
from utils import *

def run(event, context):
    inputs = {
        "compTerit": list_CompTerit(),
        "specialite": list_Spe(),
        "domaine": list_domaines()
    }
    body = {
        "inputsFilter": inputs,
        "input": event
    }

    response = {
        "statusCode": 200,
        "headers": {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(body)
    }

    return response

if __name__ == "__main__":
    run("", "")

