from slackclient import SlackClient

slack_token = os.environ['xoxp-403424165366-403181525847-421195613985-7594c85ab117e23784fdff76fe3120d0']
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="#modules-exercise",
  text="Hello from Python! :tada:"
)