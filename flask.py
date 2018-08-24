#from slackclient import SlackClient
from slacker import Slacker

slack_token = 'xoxb-403424165366-422783206135-0snejtYO4C5wojyDtye8TrMg'
#slack_token = 'xoxp-403424165366-403181525847-421195613985-7594c85ab117e23784fdff76fe3120d0'
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
