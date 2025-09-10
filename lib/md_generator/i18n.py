import ast
import re


def get_i18n(i18n_response: str):
    reg_script = r'{name}\("{id}",({fn}|{quote}{any}{quote})\)[,;}}]'.format(
        quote=r"[\"']",
        name=r"([a-z])",
        id=r"([a-z0-9]{8})",
        any=r"([\s\S]*?)",
        fn=r"\(function\([aent]\){return([\s\S]*?)}\)",
    )

    res_1 = {
        script[1]: (script[4] if script[3] == "" else i18n_format_1(script[3].strip()))
        for script in re.findall(reg_script, i18n_response)
    }

    reg_script = r'{{key:"{id}",get:{fn}}}'.format(
        id=r"([a-z0-9]{8})",
        fn=r"function\(\){return([\s\S]*?)}",
    )

    res_2 = {
        script[0]: i18n_format_2(script[1])
        for script in re.findall(
            reg_script,
            i18n_response,
        )
    }

    return res_1 | res_2


def replace_ver(script: str):
    a = re.sub(
        r"{name}\.createElement\({any},([^,]*?)\)".format(
            name=r"([a-z])",
            any=r"([\s\S]*?)",
        ),
        r"\3",
        script,
    )
    b = re.sub(
        r"{reg}{join}{name}\({ins}\.{placeholder},{any}(({notname}\({any}\){any})+?)\){join}{reg}".format(
            reg=r"(\"|')?",
            join=r"(\+)?",
            name=r"([a-z])",
            ins=r"([aent]|this\.props)",
            placeholder=r"([A-Za-z0-9_]+)",
            any=r"([^\(\)]*?)",
            notname=r"([^\+,][\s\S]|[\+,]?[\"'])",
        ),
        r"\1\2'('+\4.\5,\6\7+')'\12\13",
        a,
    )
    c = re.sub(
        r"{reg}{join}{name}\({ins}\.{placeholder},{any}\){join}{reg}".format(
            reg=r"(\"|')?",
            join=r"(\+)?",
            name=r"([a-z])",
            ins=r"([aent]|this\.props)",
            placeholder=r"([A-Za-z0-9_]+)",
            any=r"([\s\S]*?)",
        ),
        r"\1\2'('+\4.\5,\6+')'\7\8",
        b,
    )

    e = re.sub(
        r"{reg}{join}{ins}\.{placeholder}(?={join}{reg})".format(
            reg=r"(\"|')?",
            join=r"(\+|^|$|,)",
            ins=r"([aent]|this\.props)",
            placeholder=r"([A-Za-z0-9_]+)",
        ),
        r"\1\2{double_quotation}{\4}{double_quotation}",
        c,
    ).replace("{double_quotation}", '"')
    d = re.sub(
        r"{reg},{reg}(?!$)".format(
            reg=r"(\"|')",
        ),
        r"\1+','+\2",
        e,
    )
    output = re.sub(
        r"('{any}'|\"{any}\")\+(?={reg})".format(
            reg=r"(\"|')",
            any=r"([\s\S]*?)",
        ),
        r"\1,",
        d,
    )
    output = output.replace("\"+','+\"", '","')
    output = f"[{output}]"
    try:
        return ast.literal_eval(output)
    except:
        sp = output.split(",")
        for i in range(len(sp) - 1, 0, -1):
            try:
                eval = ",".join(sp[:i]).rstrip('"') + '"]'
                return ast.literal_eval(eval)
            except:
                pass
    return [script]


def i18n_format_1(script: str):
    return "".join(replace_ver(script))


def i18n_format_2(script: str):
    data: list[str] = [""]
    quote: list[str] = []
    before: str = ""
    for d in script.lstrip("[").rstrip("]"):
        if d == "\\":
            before += "\\"
            continue
        else:
            d = before + d
            before = ""
        if len(quote) == 0:
            if d in [","]:
                data.append("")
                continue
            elif d in ["'", '"', "+"]:
                quote.append(d)
            else:
                quote.append("+")
        elif d == quote[-1]:
            quote.pop()
        elif d in ["("] and quote[-1] == "+":
            quote.append(d.replace("(", ")"))
        data[-1] += d

    t = ""
    for i in range(len(data)):
        text = "".join(replace_ver(data[i]))
        t += f"{{{i - 1}}}{text}"
    return t[4:]
