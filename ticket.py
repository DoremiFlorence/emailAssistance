# -*- coding: utf-8 -*-
# @Time : 11/21/24 3:37 PM
# @Author : Florence
# @File : ticket.py
# @Project : final
from interpreter import interpreter
from datetime import datetime, timedelta
from code import search_code, search_date, search_place, related_info

interpreter.os = True
interpreter.llm.supports_vision = True
interpreter.llm.api_key = "sk-NV51c58fKzcyLM6tAanoETOmzzkcx4j9nuyMK5t6RvSV9qcL"  # LiteLLM, which we use to talk to LM Studio, requires this
interpreter.llm.api_base = "https://api.chatanywhere.tech"  # Point this at any OpenAI compatible server

interpreter.llm.supports_functions = True
interpreter.llm.context_window = 110000
interpreter.llm.max_tokens = 4096
interpreter.auto_run = True
interpreter.loop = True

interpreter.messages = []

interpreter.llm.model = "gpt-3.5-turbo"
file_path = '/Users/florence/Desktop/hku/nlp/CVPRemail.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    email_content = file.read()

date = search_date(email_content)
# print("时间：", date)

place = search_place(email_content)
# print("地点：", place)

departure = input("Where will you be departing from?")
arrival = place
departure_code = search_code(departure)
arrival_code = search_code(arrival)
leave_date = date

request = f"open google chrome and visit https://flights.ctrip.com/online/list/oneway-{departure_code}-{arrival_code}?depdate={leave_date}&cabin=y_s_c_f&adult=1&child=0&infant=0"

interpreter.chat(request)

weather_req = f"what is the whether like in {place} this week. Please search and record the weather in /Users/florence/Desktop/hku/nlp/weather.txt"
interpreter.chat(weather_req)

event = related_info(email_content)
info_req = f"please give me some information about the {event}, including what this event about, the website of the event, and what should I prepare. And record in /Users/florence/Desktop/hku/nlp/event.txt"
interpreter.chat(info_req)
