import re


def search_user(CALL, message):
    reference = message.replace(CALL, "").strip()
    search = re.search(r"<@!*(\d*)>", reference)

    return [reference, search]
