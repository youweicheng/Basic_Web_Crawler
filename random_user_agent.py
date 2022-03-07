import urllib.request
import random


def load_google():

    url = "https://www.google.com/"

    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
    ]
    # choose user-agent randomly
    random_user_agent = random.choice(user_agent_list)

    request = urllib.request.Request(url)
    # add header
    request.add_header("User-agent", random_user_agent)
    # get response
    response = urllib.request.urlopen(request)

    data = response.read().decode("utf-8")
    # get header
    print(request.get_header("User-agent"))
    # Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50

load_google()

