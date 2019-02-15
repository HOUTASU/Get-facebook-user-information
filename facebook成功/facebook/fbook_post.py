from urllib import request
from urllib.request import Request
from time import time
from http import cookiejar
import re


class FaceBook_Post(object):

    def __init__(self):

        # self.fblogin = fb.LoginFacebook()
        # self.paramsDict = self.fblogin.run()
        # self.cookies = "c_user=100022481003233;datr=ZJatW-SveH5Lm_mxhZEpzp1m;fr=1NbTUWRrz70CK4YYE." \
        #                "AWW5VKtMV_t0h4pNks7DCfmR-sw.BbrZZQ.nK.AAA.0.0.BbrZZV.AWUk0a0c;pl=n;sb=UJatW3KZx" \
        #                "xhurZ7dBXWI970Q;spin=r.4360835_b.trunk_t.1538102880_s.1_v.2_;xs=17%3AG7pp1JRhO789cQ%3A" \
        #                "2%3A1538102869%3A-1%3A-1"
        self.cookies = "fr=1NbTUWRrz70CK4YYE.AWW5VKtMV_t0h4pNks7DCfmR-sw.BbrZZQ.nK.AAA.0.0.BbrZZV.AWUk0a0c;pl=n;" \
                       "sb=UJatW3KZxxhurZ7dBXWI970Q;spin=r.4360835_b.trunk_t.1538102880_s.1_v.2_;xs=17%3AG7pp1JR" \
                       "hO789cQ%3A2%3A1538102869%3A-1%3A-1"

        self.cj = cookiejar.CookieJar()
        self.content = "克服自己的不足，成就自己"
        self.handler = request.HTTPCookieProcessor(self.cj)
        self.opener = request.build_opener(self.handler)
        self.headers1 = {
            "User-Agent": "Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) "
                          "Chrome / 69.0.3497.81Safari / 537.36"
        }
        self.post_data_params = None

    def parse_cookies(self, cookies):
        # pass
        cookie = [cookie for cookie in cookies.split(";")]
        for cooks in cookie:
            cook = cooks.split("=")
            self.cj.set_cookie(cookiejar.Cookie(
                version=0,
                name=cook[0],
                value=cook[1],
                port=None,
                port_specified=False,
                domain=".facebook.com",
                domain_specified=True,
                domain_initial_dot=False,
                path="/",
                path_specified=True,
                secure=False,
                expires=None,
                discard=False,
                comment=None,
                comment_url=None,
                rest=None
            ))

    def parse_post_data(self):
        # composer_session_id = paramdict["composer_session_id"]
        # fb_dtsg = paramdict["fb_dtsg"]
        composer_session_id = "9e8964a3 - 3bf1 - 50cf - d1b2 - 778b356ce456"
        fb_dtsg = 'AQFldDfgU8DK:AQGTrY7tTugY'
        gmt = str(time()).split('.')[0]
        self.post_data_params = "composer_session_id=" + composer_session_id + "&fb_dtsg=" + fb_dtsg + \
                                "&xhpc_context=home&xhpc_ismeta=1&xhpc_composerid=u_jsonp_2_3&xhpc_litestand=1" \
                                "&xhpc_targetid=&clp=%7B%22cl_impid%22%3A%223aa270dd%22%2C%22clearcounter%22%3A1%" \
                                "2C%22elementid%22%3A%22u_jsonp_2_a%22%2C%22version%22%3A%22x%22%2C%22parent_fbid%" \
                                "22%3A100007514494913%7D&xhpc_message_text=" + self.content + "&xhpc_message=" +\
                                self.content + "&tagger_session_id=" + gmt + \
                                "&hide_object_attachment=0&disable_location_sharing=false&composer_predicted_city" \
                                "=113317605345751&audience[0][value]=80&nctr[_mod]=pagelet_composer&__user=&__a=1" \
                                "&__dyn=7n8a9EAMHmqDxl2u5Fa8HzCq74qbx2mbAKGiyGGE&__eq=j&ttstamp=265816611211255" \
                                "8649&__rev=1081653"

    def post_data(self):
        sent_url = 'https://www.facebook.com/ajax/updatestatus.php'
        request = Request(url=sent_url, headers=self.headers1, data=self.post_data_params.encode("utf-8"))
        response = self.opener.open(request)
        content = response.read().decode("utf-8")
        status_post = {}
        with open("Facebook发帖后返回的内容.html", "w+", encoding="utf-8") as fp:
            fp.write(content)
        if response.status == 200:
            regn = re.compile('"permalink":"(.+?)",')
            result = regn.findall(content)
            # url = "https://www.facebook.com" + "".join(result[0].split("\\"))
            status_post["state"] = 0
            status_post["status"] = "成功"
            # status_post["url"] = url
        # else:

    def run(self):
        # print(self.paramsDict)
        self.parse_cookies(self.cookies)
        self.parse_post_data()
        self.post_data()


if __name__ == '__main__':
    haha = FaceBook_Post()
    haha.run()