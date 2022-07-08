import json

def lambda_handler(event, context):
  event_json = json.dumps(event)
  print(event_json)
  return "success"
