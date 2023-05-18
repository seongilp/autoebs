import requests,re,telegram,os
url = "https://5dang.ebs.co.kr/auschool/detail?courseId=BK0KAKC0000000014"
page_source = requests.get(url).text
url = "https://wstrotu.ebs.co.kr" + re.split('wstrotu.ebs.co.kr',page_source,re.S)[1].replace(";"," ").split("?")[0]
token = os.environ.get('BOT_TELEGRAM_TOKEN')
chatno = os.environ.get('CHAT_ID')
bot = telegram.Bot(token=token)
bot.send_audio(chat_id=chatno, audio=url)
