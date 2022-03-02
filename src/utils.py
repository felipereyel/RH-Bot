import re

def search_user(CALL, message):
    reference = message.replace(RH_CALL, "").strip()
    search = re.search(r"<@!(\d*)>", reference)
    
    return [reference, search]