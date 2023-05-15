import reqeusts,re,telegram
url = "https://5dang.ebs.co.kr/auschool/detail?courseId=BK0KAKC0000000014"
page_source = requests.get(url).text
url = "https://wstrotu.ebs.co.kr" + re.split('wstrotu.ebs.co.kr',page_source,re.S)[1].replace(";"," ").split("?")[0]
token = os.environ.get('BOT_TELEGRAM_TOKEN')
bot = telegram.Bot(token=token)
bot.send_audio(chat_id = '-1001442562593', audio=url)
