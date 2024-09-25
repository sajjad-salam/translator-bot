import telebot
import requests
import json
import os
from telebot import types
langs = {
    'af': 'الأفريكانية',
    'ar': 'العربية',
    'az': 'الأذربيجانية',
    'bg': 'البلغارية',
    'bn': 'البنغالية',
    'bs': 'البوسنية',
    'ca': 'الكاتالونية',
    'cs': 'التشيكية',
    'cy': 'الويلزية',
    'da': 'الدانماركية',
    'de': 'الألمانية',
    'el': 'اليونانية',
    'en': 'الإنجليزية',
    'es': 'الإسبانية',
    'et': 'الإستونية',
    'fa': 'الفارسية',
    'fi': 'الفنلندية',
    'fr': 'الفرنسية',
    'ga': 'الأيرلندية',
    'gu': 'الغوجاراتية',
    'he': 'العبرية',
    'hi': 'الهندية',
    'hr': 'الكرواتية',
    'hu': 'الهنغارية',
    'hy': 'الأرمينية',
    'id': 'الإندونيسية',
    'is': 'الأيسلندية',
    'it': 'الإيطالية',
    'ja': 'اليابانية',
    'ka': 'الجورجية',
    'kk': 'الكازاخية',
    'km': 'الخميرية',
    'kn': 'الكانادية',
    'ko': 'الكورية',
    'ky': 'القيرغيزية',
    'lo': 'اللاوية',
    'lt': 'الليتوانية',
    'lv': 'اللاتفية',
    'mk': 'المقدونية',
    'ml': 'المالايالامية',
    'mn': 'المنغولية',
    'mr': 'الماراثية',
    'ms': 'الماليزية',
    'mt': 'المالطية',
    'my': 'الميانمارية',
    'ne': 'النيبالية',
    'nl': 'الهولندية',
    'no': 'النرويجية',
    'pa': 'البنجابية',
    'pl': 'البولندية',
    'pt': 'البرتغالية',
    'ro': 'الرومانية',
    'ru': 'الروسية',
    'si': 'السنهالية',
    'sk': 'السلوفاكية',
    'sl': 'السلوفينية',
    'sq': 'الألبانية',
    'sr': 'الصربية',
    'sv': 'السويدية',
    'sw': 'السواحلية',
    'ta': 'التاميلية',
    'te': 'التيلجو',
    'th': 'التايلاندية',
    'tr': 'التركية',
    'uk': 'الأوكرانية',
    'ur': 'الأردية',
    'uz': 'الأوزبكية',
    'vi': 'الفيتنامية',
    'zh-Hans': 'الصينية (المبسطة)',
    'zh-Hant': 'الصينية (التقليدية)'
}


def tokkk():
    url = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken"
    headers = {
        'User-Agent': "okhttp/4.11.0",
        'Accept-Encoding': "gzip",
        'ocp-apim-subscription-key': "429588a945804ec09a8c981c3b324c5f"
    }
    res = requests.post(url, headers=headers)
    return res.text


def texttttttttttttt(txt, frm, to):
    url = "https://api.cognitive.microsofttranslator.com/translate"
    params = {'api-version': "3.0", 'from': frm, 'to': to}
    data = json.dumps([{"Text": txt}])
    headers = {
        'User-Agent': "okhttp/4.11.0",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'authorization': f"Bearer {tokkk()}"
    }
    res = requests.post(url, params=params, data=data, headers=headers)
    if res.status_code != 200:
        return f"Error: Unable to translate. Status: {res.status_code}"
    try:
        res_data = res.json()
        if res_data and 'translations' in res_data[0]:
            return res_data[0]['translations'][0]['text']
    except:
        return "Error: Failed to parse response."


bot = telebot.TeleBot("your-bot-token")
users = {}


def A5():
    markup = types.InlineKeyboardMarkup(row_width=3)
    for code, name in langs.items():
        markup.add(types.InlineKeyboardButton(name, callback_data=code))
    return markup


@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.send_message(msg.chat.id, "اختر اللغة الأصلية:", reply_markup=A5())
    users[msg.chat.id] = {}


@bot.callback_query_handler(func=lambda call: True)
def F0(call):
    if 'from' not in users[call.message.chat.id]:
        users[call.message.chat.id]['from'] = call.data
        bot.send_message(call.message.chat.id,
                         "اختر اللغة الهدف:", reply_markup=A5())
    else:
        users[call.message.chat.id]['to'] = call.data
        bot.send_message(call.message.chat.id, "اكتب النص الذي ترغب بترجمته:")


@bot.message_handler(func=lambda msg: msg.chat.id in users and 'to' in users[msg.chat.id])
def T3(msg):
    frm = users[msg.chat.id]['from']
    to = users[msg.chat.id]['to']
    text = msg.text
    result = texttttttttttttt(text, frm, to)
    bot.send_message(
        msg.chat.id, f"النص المترجم: {result}\n\nحقوق الترجمة: @S_J_O_D")


@bot.message_handler(content_types=['document'])
def C0(msg):
    file_info = bot.get_file(msg.document.file_id)
    file_path = file_info.file_path
    file_data = bot.download_file(file_path)

    with open(msg.document.file_name, 'wb') as f:
        f.write(file_data)

    with open(msg.document.file_name, 'r', encoding='utf-8') as f:
        text = f.read()

    frm = users[msg.chat.id]['from']
    to = users[msg.chat.id]['to']
    result = texttttttttttttt(text, frm, to)

    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("ترجمة جديدة", callback_data="T0")
    markup.add(btn)

    bot.send_message(
        msg.chat.id, f"النص المترجم من الملف:\n{result}\n\nحقوق الترجمة: @S_J_O_D", reply_markup=markup)
    os.remove(msg.document.file_name)


@bot.callback_query_handler(func=lambda call: call.data == "T0")
def T0(call):
    bot.send_message(call.message.chat.id, "اكتب النص الجديد للترجمة:")


bot.polling()
