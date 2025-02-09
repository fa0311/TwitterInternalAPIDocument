import ast
import re


def get_i18n(i18n_response: str):
    reg_script = '{name}\("{id}",({fn}|"{any}")\)'.format(
        name="([a-z])",
        id="([a-z0-9]{8})",
        any="([\s\S]*?)",
        fn="\(function\(e\){return([\s\S]*?)}\)",
    )

    res_1 = {
        script[1]: (script[4] if script[3] == "" else i18n_format_1(script[3].strip()))
        for script in re.findall(reg_script, i18n_response)
    }

    reg_script = '{{key:"{id}",get:{fn}}}'.format(
        id="([a-z0-9]{8})",
        fn="function\(\){return([\s\S]*?)}",
    )

    res_2 = {
        script[0]: i18n_format_2(script[1])
        for script in re.findall(
            reg_script,
            i18n_response,
        )
    }

    return res_1 | res_2


def replace_ver(script):
    a = re.sub(
        "{name}\.createElement\({any}\)".format(
            name="([a-z])",
            any="([\s\S]*?)",
        ),
        "",
        script,
    )
    b = re.sub(
        "{reg}{join}{name}\({ins}\.{placeholder},{any},{any}\({any}\){any}\){join}{reg}".format(
            reg="(\"|')?",
            join="(\+)?",
            name="([a-z])",
            ins="(e|this\.props)",
            placeholder="([A-Za-z0-9_]+)",
            any="([\s\S]*?)",
        ),
        r"\1\2\4.\5+\6\10\11",
        a,
    )
    c = re.sub(
        "{reg}{join}{name}\({ins}\.{placeholder},{any},{any}\){join}{reg}".format(
            reg="(\"|')?",
            join="(\+)?",
            name="([a-z])",
            ins="(e|this\.props)",
            placeholder="([A-Za-z0-9_]+)",
            any="([\s\S]*?)",
        ),
        r"\1\2\4.\5+\6\8\9",
        b,
    )
    d = re.sub(
        "{reg}{join}{name}\({ins}\.{placeholder},{any}\){join}{reg}".format(
            reg="(\"|')?",
            join="(\+)?",
            name="([a-z])",
            ins="(e|this\.props)",
            placeholder="([A-Za-z0-9_]+)",
            any="([\s\S]*?)",
        ),
        r"\1\2\4.\5+\6\7\8",
        c,
    )

    e = re.sub(
        "{reg}{join}{ins}\.{placeholder}{join}{reg}".format(
            reg="(\"|')?",
            join="(\+)?",
            ins="(e|this\.props)",
            placeholder="([A-Za-z0-9_]+)",
        ),
        r"\1\2{double_quotation}{\4}{double_quotation}\5\6",
        d,
    ).replace("{double_quotation}", '"')
    output = e.replace("+", ",")
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


def i18n_format_1(script):
    return "".join(replace_ver(script))


def i18n_format_2(script):
    data = [""]
    quote = []
    before = ""
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
        elif d in ["("]:
            quote.append(d.replace("(", ")"))
        data[-1] += d

    t = ""
    for i in range(len(data)):
        text = "".join(replace_ver(data[i]))
        t += f"{{{i - 1}}}{text}"
    return t[4:]
