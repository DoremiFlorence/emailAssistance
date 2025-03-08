# -*- coding: utf-8 -*-
# @Time : 11/21/24 10:58 AM
# @Author : Florence
# @File : code.py
# @Project : final
import openai

client = openai.OpenAI(
    api_key="xxx",
    base_url="https://api.sambanova.ai/v1",
)
def search_code(city):

    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[{"role": "system",
                   "content": "你是一个查询机场对应三字代码的助手，用户的输入是城市名称，请你返回这个城市的机场三字代码。注意只返回三个字母"},
                  {"role": "user", "content": "北京机场的三字代码是什么"},
                  {"role": "assistant", "content": "PEK"},
                  {"role": "user", "content": city+"机场的三字代码是什么"}],
        temperature=0.8,
        top_p=0.8
    )
    code = response.choices[0].message.content
    # print(code)
    return code

def search_date(email):

    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[{"role": "system",
                   "content": "你是一个文本信息提取助手，输入一封邮件内容，请你帮忙提取出活动开始时间，以xxxx-xx-xx的格式输出，比如2025-01-01。"},
                  {"role": "user", "content": "which will take place in Toronto, Ontario, Canada, from Sunday, August 3, 2025, to Thursday, August 7, 2025."},
                  {"role": "assistant", "content": "2025-08-03"},
                  {"role": "user", "content": email}],
        temperature=0.8,
        top_p=0.8
    )
    date = response.choices[0].message.content
    # print(date)
    return date

def search_place(email):

    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[{"role": "system",
                   "content": "你是一个文本信息提取助手，输入一封邮件内容，请你帮忙提取出活动举办城市。请注意，你只需要输出城市名称。"},
                  {"role": "user", "content": "which will take place in Toronto, Ontario, Canada."},
                  {"role": "assistant", "content": "Toronto"},
                  {"role": "user", "content": email}],
        temperature=0.8,
        top_p=0.8
    )
    place = response.choices[0].message.content
    # print(place)
    return place

def related_info(email):

    response = client.chat.completions.create(
        model='Meta-Llama-3.1-8B-Instruct',
        messages=[{"role": "system",
                   "content": "你是一个活动名称提取助手，输入是一封邮件内容，请你输出活动名称"},
                  {"role": "user", "content": email}],
        temperature=0.8,
        top_p=0.8
    )
    event = response.choices[0].message.content
    print(event)
    return event
# 你是一个活动信息搜索助手，输入一封邮件内容，请你给出一些活动相关信息。
