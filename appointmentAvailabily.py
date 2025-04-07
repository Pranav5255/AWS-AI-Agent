
import json

def lambda_handler(event, context):
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])

    print(parameters)

    paramDict = {item['name']: item['value'] for item in parameters}

    print(paramDict['date'])
    print(paramDict['location'])
    print(paramDict['time'])
    print(paramDict['providerName'])

    # Execute your business logic here. For more information, refer to: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
    if(paramDict['date'] == "31/12/2024"):
        print("Unavailable date")
        responseBody = {
            "TEXT": {
                "body": "The slot is not available"
            }
        }
    else:
        print("Available date")
        responseBody = {
            "TEXT": {
                "body": "The slot is available"
            }
        }

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }

    }

    dummy_function_response = {'response': action_response, 'messageVersion': event['messageVersion']}
    print("Response: {}".format(dummy_function_response))

    return dummy_function_response
