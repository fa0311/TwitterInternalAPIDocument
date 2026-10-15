import json
import os
import random
import re
import socket
import urllib.parse

import requests


class TwitterHome:
    TWITTER_HOME = "https://x.com/home"
    CLIENT = "responsive-web"
    LATEST_HEADER = (
        "https://raw.githubusercontent.com/fa0311/latest-user-agent/main/header.json"
    )
    TIMEOUT = 30

    def __init__(self):
        self.session = requests.session()
        proxies = [x.strip() for x in os.environ.get("PROXY_LIST", "").splitlines() if x.strip()]
        if proxies:
            proxy = random.choice(proxies)
            if "://" not in proxy:  # legacy host:port:user:pass
                host, port, username, password = proxy.split(":")
                proxy = f"http://{username}:{password}@{host}:{port}"
            # PySocks and GitHub runners cannot reach IPv6 proxies; pin the IPv4 address
            parsed = urllib.parse.urlparse(proxy)
            proxy = parsed._replace(netloc=parsed.netloc.replace(parsed.hostname, socket.gethostbyname(parsed.hostname))).geturl()
            self.session.proxies = {"http": proxy, "https": proxy}
        header = self.session.get(self.LATEST_HEADER, timeout=self.TIMEOUT).json()
        self.chrome_header = {
            k: v for k, v in header["chrome"].items() if k not in ["host", "connection"]
        }

    def load(self, file_path: str):
        with open(file_path, mode="r", encoding="utf-8") as f:
            cookies = json.load(f)
        if isinstance(cookies, list):
            cookies = {c["name"]: c["value"] for c in cookies}
        self.session.cookies.update(cookies)

    def get_home(self):
        legacy = self.session.get(
            self.TWITTER_HOME, headers=self.get_header(), timeout=self.TIMEOUT
        )
        migrate_script = self.get_script(legacy.text)

        if re.search(r'document\.location = "(.*?)"', migrate_script[0]):
            migrate_url = re.search(
                r'document\.location = "(.*?)"', migrate_script[0]
            ).group(1)
            redirect = self.session.get(
                migrate_url, headers=self.get_header(), timeout=self.TIMEOUT
            )

            migrate_url = re.search(r'<form action="(.*?)"', redirect.text).group(1)
            params = dict(
                re.findall(
                    r'<input type="hidden" name="(.*?)" value="(.*?)" />', redirect.text
                )
            )
            self.response = self.session.post(
                migrate_url,
                headers=self.get_header(),
                json=params,
                timeout=self.TIMEOUT,
            )
        else:
            self.response = legacy

    def get_header(self):
        return {
            **self.chrome_header,
            "accept-language": "ja,en;q=0.9",
            "origin": "https://x.com",
            "referer": "https://x.com/",
            "sec-ch-ua-platform": '"Windows"',
        }

    def get_script_url(self) -> list[str]:
        src = r"(https://abs\.twimg\.com\/{0}\/client-web\/[a-zA-Z0-9\.]*?\.js)".format(
            re.escape(self.CLIENT)
        )
        reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}" crossorigin="anonymous" src="{src}"></script>'.format(
            nonce=r"([a-zA-Z0-9]{48})",
            src=src,
        )
        return [url[1] for url in re.findall(reg_script, self.response.text)]

    def get_script(self, response: str) -> list[str]:
        reg_script = '<script type="text/javascript" charset="utf-8" nonce="{nonce}">{any}</script>'.format(
            nonce=r"([a-zA-Z0-9]{48})",
            any=r"([\s\S]*?)",
        )
        return [script[1] for script in re.findall(reg_script, response)]

    def get_script_res(self) -> list[str]:
        return self.get_script(self.response.text)

    def get_script_res_url(self) -> dict[str, str]:
        reg_script = '<link nonce="{nonce}" rel="preload" as="script" crossorigin="anonymous" fetchpriority="high" href="{src}" />'.format(
            nonce=r"([a-zA-Z0-9]{48})",
            src=r"(https://[\s\S]*?\.js)",
        )
        return {
            re.sub(r"\.[0-9a-f]+a\.js$", "", "/".join(url[1].split("/")[5:])): url[1]
            for url in re.findall(reg_script, self.response.text)
        }


class TwitterDeck(TwitterHome):
    TWITTER_HOME = "https://pro.x.com"
    CLIENT = "gryphon-client"
