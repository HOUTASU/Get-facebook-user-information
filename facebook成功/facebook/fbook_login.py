from urllib import request
from urllib.request import Request,ProxyHandler
from time import sleep, time
import re
from http import cookiejar


class LoginFacebook(object):

    """
    模拟登录Facebook并且获取登录后的cookie
    """
    def __init__(self):
        self.get_proxy()
        self.login_post_values = None
        self.email = "MihalinaKonstantinova9818@mail.ru"
        self.password = "bkwgkk"
        self.cj = cookiejar.CookieJar()
        self.proxies = {
            "http": 'http://{}:{}@{}'.format('squid_user', 'Urun2017', '137.175.62.130:65432')
        }
        # self.proxy_support = ProxyHandler(self.proxies)
        self.handler = request.HTTPCookieProcessor(self.cj)
        auth_handler = request.HTTPBasicAuthHandler()
        auth_handler.add_password(realm=None,
                                  uri='http://137.175.62.130:65432',
                                  user='squid_user',
                                  passwd="Urun2017"
                                  )
        self.opener = request.build_opener(auth_handler, request.HTTPBasicAuthHandler)
        self.opener.add_handler(self.handler)
        self.headers1 = {
            "User-Agent": "Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) "
                          "Chrome / 69.0.3497.81Safari / 537.36"
        }
        self.post_data_params = None

    def login_first_step(self):
        print("第一步")
        """
        获取登录页面的源码，提取lsd，lgndim，lgnrnd，lgnjs等参数数值，拼接登录的post请求的参数
        :return:
        """
        # url = "https://www.facebook.com/"
        url = "http://icanhazip.com/"
        self.opener.addheaders = [("User-Agent","Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / "
                                                "537.36(KHTML, likeGecko)Chrome / 69.0.3497.81Safari / 537.36")]
        content = self.opener.open(url)
        print(content)
        with open("IP返回的页面.html", "w+", encoding="utf-8") as fp:
            fp.write(content.read().decode("utf-8"))
        html = content.read().decode("utf-8")
        print(request.getproxies())
        lsd_re = re.compile('<input type="hidden" name="lsd" value="(.+?)" autocomplete="off" />')
        lsd_result = lsd_re.findall(html)
        lsd = ''
        if len(lsd_result) != 0:
            lsd = lsd_result[0]

        lgndim_re = re.compile('<input type="hidden" autocomplete="off" name="lgndim" value="(.*?)" id="u_0_4" />')
        lgndim_result = lgndim_re.findall(html)
        lgndim = ''
        if len(lgndim_result) != 0:
            lgndim = lgndim_result[0]

        lgnrnd_re = re.compile('<input type="hidden" name="lgnrnd" value="(.+?)" />')
        lgnrnd_result = lgnrnd_re.findall(html)
        # lgnrnd = ''
        if len(lgnrnd_result) != 0:
            lgnrnd = lgnrnd_result[0]
        else:
            lgnrnd = ""

        lgnjs_re = re.compile('<input type="hidden" id="lgnjs" name="lgnjs" value="(.+?)" />')
        lgnjs_result = lgnjs_re.findall(html)
        lgnjs = ''
        if len(lgnjs_result) != 0:
            lgnjs=lgnjs_result[0]

        # 用上面抓取的值拼接post请求的data参数
        self.login_post_values = 'lsd=' + lsd + '&email=' + self.email + '&pass=' + self.password + \
                                 '&persistent=&default_persistent=1&timezone=&lgndim=&lgnrnd=' \
                                 + lgnrnd + '&lgnjs=' + lgnjs + '&locale=zh_CN'

    def login_second_step(self):
        print("第二步")
        """
        进行登录操作
        :return:
        """
        sent_url = 'https://www.facebook.com/login.php?login_attempt=1&lwv=110'
        request = Request(url=sent_url, headers=self.headers1, data=self.login_post_values.encode("utf-8"))
        content = self.opener.open(request).read().decode("utf-8")

    def login_third_step(self):
        print("第三步")
        """
        提取datr参数，添加到cookiejar
        :return:
        """
        sent_url = 'https://www.facebook.com'
        request = Request(url=sent_url, headers=self.headers1)
        content = self.opener.open(request)
        tmp_html = content.read().decode("utf-8")
        # 查找datr
        datr_re = re.compile('"_js_datr","(.+?)",')
        # m = re.compile(reg)
        datr_result = datr_re.findall(tmp_html)
        datr = ''
        if datr_result:
            datr = datr_result[0]
        self.cj.set_cookie(cookiejar.Cookie(
            version=0,
            name='datr',
            value=datr,
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

    def login_fourth_step(self):
        print("第四步")
        cookie_dict = {}
        sent_url = 'https://www.facebook.com'
        request = Request(url=sent_url, headers=self.headers1)
        content = self.opener.open(request).read().decode("utf-8")
        with open("Facebook登录后的个人主页.html", "w", encoding="utf-8") as fp:
            fp.write(content)
        print(content)
        cookieList = []
        for key in self.cj:
            cookie = str(key.name) + "=" + str(key.value)
            cookieList.append(cookie)
        cookies = ";".join(cookieList)
        cookie_dict["cookies"] = cookies

        composer_id_re = re.compile('<input type="hidden" autocomplete="off" name="composer_session_id" '
                                    'value="(.+?)" />')
        composer_id_result = composer_id_re.findall(content)
        if len(composer_id_result) != 0:
            composer_session_id = composer_id_result[0]
            cookie_dict["composer_session_id"] = composer_session_id

        fb_dtsg_re = re.compile('<input type="hidden" name="fb_dtsg" value="(.+?)" autocomplete="off" />')
        fb_dtsg_result = fb_dtsg_re.findall(content)
        # print(fb_dtsg_result)
        if len(fb_dtsg_result) != 0:
            fb_dtsg = fb_dtsg_result[0]
            # print(fb_dtsg)
            cookie_dict["fb_dtsg"] = fb_dtsg

        return cookie_dict

    def get_proxy(self):
        proxy = {'http': r'http://squid_user:Urun2017@137.175.62.130:65432'}
        proxy_support = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_support)
        request.install_opener(opener)

    def run(self):
        gfc = LoginFacebook()
        gfc.login_first_step()
        gfc.login_second_step()
        gfc.login_third_step()
        cookies = gfc.login_fourth_step()
        print(cookies)
        return cookies


if __name__ == '__main__':
    lgfb = LoginFacebook()
    lgfb.run()