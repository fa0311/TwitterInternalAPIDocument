import requests
import re


class twitter_home:
    TWITTER_HOME = "https://twitter.com/home"
    LATEST_USER_AGENT = "https://raw.githubusercontent.com/TechfaneTechnologies/latest-user-agent/main/user_agents.json"
    TWITTER_FRONTEND_FLOW = False

    def __init__(self):
        self.session = requests.session()
        self.user_agent_list = self.session.get(self.LATEST_USER_AGENT).json()

    def login(self, userid: str, password: str):
        flow = TwitterFrontendFlow()
        flow.session = self.session
        flow.login_flow()
        flow.LoginJsInstrumentationSubtask()
        flow.LoginEnterUserIdentifierSSO(userid)
        flow.LoginEnterPassword(password)
        flow.AccountDuplicationCheck()
        if "LoginSuccessSubtask" not in flow.get_subtask_ids():
            raise Exception("login error")

    def load(self, file_path: str):
        flow = TwitterFrontendFlow()
        flow.session = self.session
        flow.LoadCookies(file_path)

    def get_home(self):
        self.response = self.session.get(self.TWITTER_HOME, headers=self.get_header())

    def get_header(self):
        return {"User-Agent": self.user_agent_list[0]}

    def get_script_url(self) -> list[str]:
        reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}" crossorigin="anonymous" src="{src}"></script>'.format(
            nonce="([a-zA-Z0-9]{48})",
            src="(https://abs\.twimg\.com\/responsive\-web\/client\-web\/[a-zA-Z0-9\.]*?\.js)",
        )
        return [url[1] for url in re.findall(reg_script, self.response.text)]

    def get_script(self) -> list[str]:
        reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}">{any}</script>'.format(
            nonce="([a-zA-Z0-9]{48})",
            any="([\s\S]*?)",
        )
        return [script[1] for script in re.findall(reg_script, self.response.text)]


try:
    from TwitterFrontendFlow.TwitterFrontendFlow.TwitterFrontendFlow import *
    twitter_home.TWITTER_FRONTEND_FLOW = True
except:
    pass