from celery import shared_task
import slacky
from . import utils

@shared_task
def slack_message_task(message, channel_id =None, user_id =None, thread_ts= None):
    opeanai_msg = utils.chat_with_openai(message, raw=False)
    try:
        r =slacky.send_message(opeanai_msg, channel_id =channel_id, user_id =user_id, thread_ts= thread_ts)
    except:
        pass
    return r.status_code
