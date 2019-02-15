import requests
import re
from urllib import request
from urllib.request import Request,ProxyHandler
from http import cookiejar


class CommentFacebook(object):

    def __init__(self):

        # self.fblogin = fb.get_facebook_cookie()
        # self.paramsDict = self.fblogin.run()
        self.cj = cookiejar.CookieJar()
        self.handler = request.HTTPCookieProcessor(self.cj)
        self.opener = request.build_opener(self.handler)
        self.cookies = "c_user=100022481003233;datr=1nKsW370c4rVvNDfhxUsfjUO;fr=1ddI77NTmWxoCWfqS.AWW8We1SPq5vs" \
                       "Bp3GlGM5PeSYVg.BbrHK2.pp.AAA.0.0.BbrHLG.AWVbFc_i;pl=n;sb=tnKsWwi8KpLzcPbkEM8BTbQb;spin=" \
                       "r.4357353_b.trunk_t.1538028231_s.1_v.2_;xs=24%3AtypxAXPVStwR_A%3A2%3A1538028230%3A-1%3A-1'" \
                       ", 'composer_session_id': 'f67aa526-921d-bf76-f278-5c2fbca9ca3e', 'fb_dtsg': 'AQHP8vYquxsI:" \
                       "AQEwfqkVgRlL"
        self.session = requests.session()
        self.headers1 = {
            "User-Agent": "Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) "
                          "Chrome / 69.0.3497.81Safari / 537.36"
        }

    def parse_cookies(self, cookies):

        cookie = [cookie for cookie in cookies.split(";")]
        for cooks in cookie:
            cook = cooks.split("=")
            self.session.cookies.set(cook[0], cookie[1])
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

    def fb_commment(self):
        url = "https://www.facebook.com/ufi/add/comment/?dpr=1"
        # formdata = {
        #     "ft_ent_identifier": "334546083971422",
        #     "comment_text": "不可能是真的，刘欢政不帅，长得一般",
        #     "source": 1,
        #     "client_id": "1537951308186:2931486606",
        #     "session_id": "73d73505",
        #     "rootid": "u_ps_0_0_v",
        #     "attached_sticker_fbid": 0,
        #     "attached_photo_fbid": 0,
        #     "attached_video_fbid": 0,
        #     "attached_file_fbid": 0,
        #     "ft[qid]": "6605451417388423722",
        #     "ft[mf_story_key]": "3683855138787087532",
        #     "ft[top_level_post_id]": "334668957292468",
        #     "ft[src]": "10",
        #     "ft[fbfeed_location]": 1,
        #     "av": "100022481003233",
        #     "fb_dtsg": "AQF3rj3O7cxO:AQHHEJzjDS7e",
        #     "jazoest": "265817051114106517955991207958658172726974122106688355101"
        # }
        comments = "中文输入法"
        params = "ft_ent_identifier=334546083971422&comment_text=中文输入法&source=1" \
                 "&client_id=1537951308186:2931486606&rootid=u_ps_0_0_v" \
                 "&attached_sticker_fbid=0&attached_photo_fbid=0&attached_video_fbid=0&attached_file_fbid=0" \
                 "&ft[qid]=6605451417388423722&ft[mf_story_key]=3683855138787087532&ft[top_level_post_id]" \
                 "=334668957292468&ft[src]=10&ft[fbfeed_location]=1&av=100022481003233&fb_dtsg=AQF3rj3O7cxO:AQH" \
                 "HEJzjDS7e&jazoest=265817051114106517955991207958658172726974122106688355101"
        # param = urllib.parse.urlencode()
        requ = Request(url=url, headers=self.headers1, data=params.encode("utf-8"))
        content = self.opener.open(requ)
        comment_status = {}

        if content.status == 200:
            comment_status["status"] = "发表评论成功"

            resour = 'body:{text:"' + comments + '".+?,id:"(.+?)",fbid:'
            regn = re.compile(resour)
            req = Request(url="https://www.facebook.com", headers=self.headers1)
            response = self.opener.open(req)
            result = regn.findall(response.read().decode("utf-8"))
            # print(result[-1])
            comment_status["comment_id"] = result[-1]
            comment_status["url"] = None
            return comment_status

        else:
            if (content.status >= 400 and content.status < 500):
                comment_status["status"] = "发表评论失败，请检查链接"
            elif content.status < 600:
                comment_status["status"] = "发表评论，服务器错误"
            else:
                comment_status["status"] = "发表评论失败，未知错误原因"
            comment_status["comment_id"] = None
            comment_status["url"] = None
            return comment_status

    def run(self):
        self.parse_cookies(self.cookies)
        # self.parse_cookies()
        return self.fb_commment()


if __name__ == '__main__':
    fb = CommentFacebook()
    print(fb.run())