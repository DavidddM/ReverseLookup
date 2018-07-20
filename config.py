N_API_URL = "http://simpleapi.info/apps/numbers-info/info.php?results=json"
C_API_URL = "https://api.tbcpay.ge/api/Service/NextStep"
ENCODING = "utf-8-sig"

GUI = None


def init_gui(g):
    global GUI
    GUI = g


def get_c_context(phone_number):
    context_dictionary = {
        "context": [{"key": "HAVEACCOUNT", "value": "1", "formatedValue": "1"},
                    {"key": "account", "value": phone_number}],
        "serviceId": 1213, "stepOrder": 2
        }
    return context_dictionary
