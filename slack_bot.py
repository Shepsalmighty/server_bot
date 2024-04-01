
# https://slack.dev/python-slack-sdk/installation/index.html#access-tokens

import os
import logging
from slack_sdk import WebClient
from PRIVATE_bot_token import SLACK_BOT_TOKEN

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])


# res = client.api_test()


