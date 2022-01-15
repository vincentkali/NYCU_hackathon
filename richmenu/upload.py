import sys
from linebot import LineBotApi
from NYCU_hackathon.config import *

if CHANNEL_TOKEN is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(CHANNEL_TOKEN)

# Example: https://github.com/line/line-bot-sdk-python#set_rich_menu_imageself-rich_menu_id-content_type-content-timeoutnone
# Document https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image

content_type = 'image/png'  # Just support JPEG or PNG, check your image type

try:
    with open('./NYCU_hackathon/richmenu/default.png', 'rb') as f:
        line_bot_api.set_rich_menu_image('richmenu-4cf0175cb2fb38e008d79387d26eefbe', content_type, f)
except Exception as e:
    print(e)

print('Set default success.')
