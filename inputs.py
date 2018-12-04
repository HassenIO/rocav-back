import json
import sys
import os

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

    return {
        "statusCode": 200,
        "headers": {
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(body)
    }


if __name__ == "__main__":
    run("", "")

