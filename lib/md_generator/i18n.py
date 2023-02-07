import re


def get_i18n(i18n_response: str):
    reg_script = '{name}\("{id}",({fn}|"{any}")\)'.format(
        name="([a-z])",
        id="([a-z0-9]{8})",
        any="([\s\S]*?)",
        fn="\(function\(e\){return([\s\S]*?)}\)",
    )

    return {
        script[1]: script[4]
        if script[3] == ""
        else i18n_format(script[3].strip().lstrip().strip('"').lstrip('"'))
        for script in re.findall(reg_script, i18n_response)
    }


def i18n_format(script):
    output = re.sub(
        "{join_first}{name}\(e\.{placeholder},{any}\){join_last}".format(
            join_first="((\"|')\+)?",
            join_last="(\+(\"|'))?",
            name="([a-z])",
            any="([\s\S]*?)",
            placeholder="([A-Za-z0-9]*)",
        ),
        r"({\4},\5)",
        script,
    )
    output = re.sub(
        "{join_first}e\.{placeholder}{join_last}".format(
            join_first="((\"|')\+)?",
            join_last="(\+(\"|'))?",
            placeholder="([A-Za-z0-9]*)",
        ),
        r"{\3}",
        output,
    )

    return output.replace('"', "")
