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
        # "dataframe": df.to_json(orient='records'),
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

if __name__ == "__main__":
    run("", "")

