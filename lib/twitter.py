import re

import requests


class twitter_home:
    TWITTER_HOME = "https://x.com/home"
    CLIENT = "responsive-web"
    LATEST_USER_AGENT = "https://raw.githubusercontent.com/fa0311/latest-user-agent/main/output.json"
    TWITTER_FRONTEND_FLOW = False
    TIMEOUT = 30

    def __init__(self):
        self.session = requests.session()
        self.user_agent = self.session.get(self.LATEST_USER_AGENT, timeout=self.TIMEOUT).json()["chrome"]

    def login(self, userid: str, password: str):
        flow = TwitterFrontendFlow() # type: ignore
        flow.session = self.session
        flow.login_flow()
        flow.LoginJsInstrumentationSubtask()
        flow.LoginEnterUserIdentifierSSO(userid)
        flow.LoginEnterPassword(password)
        flow.AccountDuplicationCheck()
        if "LoginSuccessSubtask" not in flow.get_subtask_ids():
            raise Exception("login error")

    def load(self, file_path: str):
        flow = TwitterFrontendFlow() # type: ignore
        flow.session = self.session
        flow.LoadCookies(file_path)

    def get_home(self):
        legacy = self.session.get(self.TWITTER_HOME, headers=self.get_header(), timeout=self.TIMEOUT)
        migrate_script = self.get_script(legacy.text)

        if re.search(r'document\.location = "(.*?)"', migrate_script[0]):
            migrate_url = re.search(r'document\.location = "(.*?)"', migrate_script[0]).group(1)
            redirect = self.session.get(migrate_url, headers=self.get_header(), timeout=self.TIMEOUT)
            
            migrate_url = re.search(r'<form action="(.*?)"', redirect.text).group(1)
            params = dict(re.findall(r'<input type="hidden" name="(.*?)" value="(.*?)" />', redirect.text))
            self.response = self.session.post(migrate_url, headers=self.get_header(), json=params, timeout=self.TIMEOUT)
        else:
            self.response = legacy


    def get_header(self):
        return {
            "User-Agent": self.user_agent,
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "ja,en;q=0.9",
            "cache-control": "no-cache",
            "origin": "https://x.com",
            "pragma": "no-cache",
            "referer": "https://x.com/",
            "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
        }
            
            
                

    def get_script_url(self) -> list[str]:
        src = "(https://abs\.twimg\.com\/{0}\/client-web\/[a-zA-Z0-9\.]*?\.js)".format(
            re.escape(self.CLIENT)
        )
        reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}" crossorigin="anonymous" src="{src}"></script>'.format(
            nonce="([a-zA-Z0-9]{48})",
            src=src,
        )
        return [url[1] for url in re.findall(reg_script, self.response.text)]
    


    def get_script(self,response:str) -> list[str]:
        reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}">{any}</script>'.format(
            nonce="([a-zA-Z0-9]{48})",
            any="([\s\S]*?)",
        )
        return [script[1] for script in re.findall(reg_script, response)]
    
    def get_script_res(self) -> list[str]:
        return self.get_script(self.response.text)



class twitter_deck(twitter_home):
    TWITTER_HOME = "https://pro.x.com"
    CLIENT = "gryphon-client"


try:
    from TwitterFrontendFlow.TwitterFrontendFlow.TwitterFrontendFlow import *  # type: ignore

    twitter_home.TWITTER_FRONTEND_FLOW = True
except:
    pass
