import requests
import re


class twitter_home:
    def __init__(self):
        self.TWITTER_HOME = "https://twitter.com/home"
        self.LATEST_USER_AGENT = "https://raw.githubusercontent.com/TechfaneTechnologies/latest-user-agent/main/user_agents.json"

        self.user_agent_list = requests.get(self.LATEST_USER_AGENT).json()
        self.headers = {"User-Agent": self.user_agent_list[0]}

        self.response = requests.get(self.TWITTER_HOME, headers=self.headers)

    def get_main_script_url(self) -> str:
        reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}" crossorigin="anonymous" src="{src}"></script>'.format(
            nonce="([a-zA-Z0-9]{48})",
            src="(https://abs\.twimg\.com\/responsive\-web\/client\-web\/main\.[a-z0-9]{9}\.js)",
        )
        return re.findall(reg_script, self.response.text)[0][1]