import requests,wget,re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import telegram
import asyncio
import warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
warnings.filterwarnings('ignore', 'Unverified HTTPS request')
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

params = {
    'returnUrl': 'https://5dang.ebs.co.kr',
    'login_uri': 'https://5dang.ebs.co.kr/sso/login',
    'i': '##ID##',
    'c': '##PWD##'
}

header = {
    'Referer':'https://5dang.ebs.co.kr/login',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

token = '##TOKEN##'
chat_id = '##ID##'
bot = telegram.Bot(token=token)

login_url = 'https://5dang.ebs.co.kr/login'

url_list = [
    'https://5dang.ebs.co.kr/auschool/sub/replay?prodId=235&lectId=60359619&pageNum=8&orderby=NEW&situ=&startDate=&endDate=&pdfOnly=',
]

#rec_url = 'https://5dang.ebs.co.kr/auschool/sub/replay?prodId=235&lectId=60344311&pageNum=9&orderby=NEW&situ=&startDate=&endDate=&pdfOnly='


filename = ''

with requests.Session() as s:
    for url in url_list:
        res = s.post(login_url,headers=header,data=params,verify=False)
        res = s.get(url,headers=header,verify=False)
        url = "https://wstrotu.ebs.co.kr" + re.split('wstrotu.ebs.co.kr',res.text,re.S)[1]+ "wstrotu.ebs.co.kr"
        wget.download(url)
        filename = url.split('?')[0].split('/')[-1]

async def main():
    await bot.send_audio(chat_id=chat_id, audio=open(filename,'rb'))

asyncio.run(main())
# if __name__ == '__main__':
#     print_hi('PyCharm')±±
