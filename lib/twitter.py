import requests
import re


class twitter_home:
    TWITTER_HOME = "https://twitter.com/home"
    LATEST_USER_AGENT = "https://raw.githubusercontent.com/TechfaneTechnologies/latest-user-agent/main/user_agents.json"

    def __init__(self):
        self.user_agent_list = requests.get(self.LATEST_USER_AGENT).json()

    def get_header(self):
        return {"User-Agent": self.user_agent_list[0]}

    def get_i18n_url(self) -> list[str]:
        locales = ["en", "ja"]
        reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}" crossorigin="anonymous" src="{src}"></script>'.format(
            nonce="([a-zA-Z0-9]{48})",
            src="(https://abs\.twimg\.com\/responsive\-web\/client\-web\/i18n\/[a-zA-Z0-9\.]*?\.js)",
        )
        i18n = {}
        for locale in locales:
            response = requests.get(
                self.TWITTER_HOME,
                headers=dict(self.get_header(), **{"accept-language": locale}),
            )
            i18n[locale] = re.findall(reg_script, response.text)[0][1]
        return i18n

    def get_script_url(self) -> list[str]:
        reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}" crossorigin="anonymous" src="{src}"></script>'.format(
            nonce="([a-zA-Z0-9]{48})",
            src="(https://abs\.twimg\.com\/responsive\-web\/client\-web\/[a-zA-Z0-9\.]*?\.js)",
        )
        response = requests.get(self.TWITTER_HOME, headers=self.get_header())
        return [url[1] for url in re.findall(reg_script, response.text)]
