import pandas as pd


class MdGenerator:
    def __init__(self):
        self.output = ""

    def h1(self, text: str, end: str = "<br>\n"):
        self.output += f"# {text}{end}"

    def h2(self, text: str, end: str = "<br>\n"):
        self.output += f"## {text}{end}"

    def h3(self, text: str, end: str = "<br>\n"):
        self.output += f"### {text}{end}"

    def h4(self, text: str, end: str = "<br>\n"):
        self.output += f"#### {text}{end}"

    def p(self, text: str, end: str = "<br>\n"):
        self.output += f"{text}{end}"

    def inline(self, text: str, end: str = "<br>\n"):
        self.output += f"`{text}`{end}"

    def code(self, text: str, title: str = "", end: str = "\n"):
        self.output += f"```{title}\n{text}\n```{end}"

    def li(self, text: str, end: str = "<br>\n"):
        self.output += f"- {text}{end}"

    def table(self, data: dict, end: str = "\n\n"):
        datafram = pd.DataFrame(data)
        self.output += f"{datafram.to_markdown(index=False)}{end}"

    def table_escape(self, text: str):
        if type(text) is str:
            return text.replace("|", "\|")
        else:
            return text

    def print(self):
        print(self.output)
