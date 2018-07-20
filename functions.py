import requests
from decorators import no_data_decorator
import config
import json
from tkinter import messagebox, END


def search_event_listener(*args):
    phone_number = retrieve_number()
    if phone_number is None:
        return None
    request_names(phone_number[0])
    request_carrier(phone_number[1])


def request_names(phone_number):
    r = requests.post(config.N_API_URL,
                      data={"number": phone_number})
    r.encoding = config.ENCODING
    parsed_data = parse_data_n(r.text)
    show_names(parsed_data)


def request_carrier(phone_number):
    r = requests.post(config.C_API_URL,
                      json=config.get_c_context(phone_number))
    r.encoding = config.ENCODING
    parsed_data = parse_data_c(r.text)
    show_carrier(parsed_data)


def retrieve_number():
    phone_number = validify(config.GUI.get_entry_value())
    phone_number_formatted = phone_number[:3] + "-" + phone_number[3:]
    if phone_number.isdigit():
        return (phone_number, phone_number_formatted)
    messagebox.showerror("ჰმმ?!", "ნომერი იყო ვითომ ეგ, რაც დაწერე?!")
    clear_entry()
    return None


@no_data_decorator
def show_names(data):
    clear_listbox()
    for name in data:
        config.GUI.Listbox1.insert(END, name)


@no_data_decorator
def show_carrier(data):
    config.GUI.Label1.config(text=data)


def parse_data_n(dot_text):
    tmp_dict = json.loads(dot_text)
    if tmp_dict["res"] == "no":
        clear_entry()
        clear_listbox()
        messagebox.showwarning("უპს!", "სამწუხაროდ ვერაფერი მოიძებნა.")
        return None
    return tmp_dict["items"]


def parse_data_c(dot_text):
    tmp_dict = json.loads(dot_text)
    if not tmp_dict["success"]:
        return None
    return tmp_dict["data"]["title"]


def validify(phone_number):
    return phone_number.replace("-", "").replace(".", "").replace(" ", "")


def clear_entry():
    config.GUI.Entry1.delete(0, END)


def clear_listbox():
    config.GUI.Listbox1.delete(0, END)
