'''
get cookies and add to headers

'''
import urllib.request

# 1. url
url = "https://www.yaozh.com/member/"
# 2. add headers
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Cookie":"PHPSESSID=b4v7t9l90fa9litmtb3e3ca250; _ga=GA1.2.949417196.1639060080; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1639060082; _gid=GA1.2.646039909.1639203413; acw_tc=781bad0b16392072905858806e3f6c37e763cc259e312b1ef4b1802a108992; yaozh_userId=1179956; yaozh_uidhas=1; yaozh_mylogin=1639207656; yaozh_logintime=1639208201; yaozh_user=1179956	yuweicheng; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyYnoaSaJxunpmbg26qb21rg66flM6bh5+scZJobIXe19jJzcSfyqPMhqDUbXBvWp3CrKWS1Z/SyVty1HJjk5+a09bC06fa7887Bc8773d2e38Efb57B01EkpqXmmmVbJuZl4Nuqm9sa4OtmqDGWKDXc2iUclSUm5WalpSZaZVnmZecg2605527f60ddf47044ea476398c41df5ea4; db_w_auth=952759	yuweicheng; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1639208987"
}
# 3. create request
request = urllib.request.Request(url, headers=headers)
# 4. send request and get response
response = urllib.request.urlopen(request)
# 5. read data
data = response.read()
# save data
with open("cookie2.html", "wb") as f:
    f.write(data)
