from urllib import request
from urllib.request import Request
from http import cookiejar


class LikeFacebook(object):

    def __init__(self):

        # self.fblogin = fb.get_facebook_cookie()
        # self.paramsDict = self.fblogin.run()
        self.cookies = "c_user=100022481003233;datr=1nKsW370c4rVvNDfhxUsfjUO;fr=1ddI77NTmWxoCWfqS.AWW8We1SPq5vsBp3GlGM5PeSYVg.BbrHK2.pp.AAA.0.0.BbrHLG.AWVbFc_i;pl=n;sb=tnKsWwi8KpLzcPbkEM8BTbQb;spin=r.4357353_b.trunk_t.1538028231_s.1_v.2_;xs=24%3AtypxAXPVStwR_A%3A2%3A1538028230%3A-1%3A-1', 'composer_session_id': 'f67aa526-921d-bf76-f278-5c2fbca9ca3e', 'fb_dtsg': 'AQHP8vYquxsI:AQEwfqkVgRlL"
        self.cj = cookiejar.CookieJar()
        self.handler = request.HTTPCookieProcessor(self.cj)
        self.opener = request.build_opener(self.handler)
        self.headers1 = {
            "User-Agent": "Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) "
                          "Chrome / 69.0.3497.81Safari / 537.36"
        }

    def parse_cookies(self, cookies):

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

    def get_formdata_params(self):
        sent_url = 'https://www.facebook.com'
        request = Request(url=sent_url, headers=self.headers1)
        content = self.opener.open(request)
        with open("点赞获取的facebook的个人主页.html", "w+", encoding="utf-8") as fp:
            fp.write(content.read().decode("utf-8"))

    def fb_commment_like(self):
        url = "https://www.facebook.com/ufi/comment/reaction/?dpr=1"
        formdata = {
            "comment_id": "334546083971422_335535233872507",
            "legacy_id": "335535233872507",
            "reaction_type": 1,
            "ft_ent_identifier": "334546083971422",
            "source": 1,
            "instance_id": "u_ps_0_0_u",
            "client_id": "1537950232064:2032229500",
            "session_id": "54d161e9",
            "av": "100022481003233",
            "fb_dtsg": "AQGlvdLpSUeH:AQFeZ5tJzXF8",
            "jazoest": "26581711081181007611283851017258658170101905311674122887056"
        }

        params_data =  "comment_id=334546083971422_335535233872507&legacy_id=335535233872507&reaction_type=1&" \
                       "ft_ent_identifier=334546083971422&source=1&instance_id=u_ps_0_0_u&" \
                       "client_id=1537950232064:2032229500&session_id=54d161e9&av=100022481003233&" \
                       "fb_dtsg=AQGlvdLpSUeH:AQFeZ5tJzXF8&jazoest=265817110811810076112838510" \
                       "17258658170101905311674122887056"
        requ = Request(url=url, headers=self.headers1, data=params_data.encode("utf-8"))
        content = self.opener.open(requ)

    def run(self):
        # self.parse_cookies(self.cookies)
        self.fb_commment_like()


if __name__ == '__main__':
    fb = LikeFacebook()
    fb.run()