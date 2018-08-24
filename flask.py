#from slackclient import SlackClient
from slacker import Slacker

slack_token = 'Some-Slack-Token'

sc = Slacker(slack_token)

# if sc.rtm_connect():
# 	events = sc.rtm_read()
# 	print(events)
# 	sc.api_call(
# 	  "chat.postEphemeral",
# 	  channel="#modules-exercise",
# 	  text="Hello from Python! :tada:",
# 	)
# else:
# 	print('could not connect')

sc.chat.post_message('#modules-exercise', 'Hello fellow slackers!')
