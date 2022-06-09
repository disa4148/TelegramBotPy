import telebot
import random
import os
import python_weather
import asyncio

from telebot import types

KeyboardRemove = telebot.types.ReplyKeyboardRemove()


bot = telebot.TeleBot('') #Токен телеграмм-бота

@bot.message_handler(commands=['start']) # Какие команды обрабатывать боту
def start(message): # Ф-ция отправки сообщений
    mess = f' Привет, <b>{message.from_user.first_name} </b> меня звать Роби Малек \n \n Я буду твоим персональным помощником в пользовании компьютером'
    bot.send_message(message.chat.id, mess, parse_mode='html') # Первый параметр - выбор чата, Второй - текст, Третий - добавление тегов html
    sticker = open('stickers/sticker2.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)    

@bot.message_handler(commands=['help'])
def start(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) 
    submit_turn_off_pc = types.KeyboardButton('Выключить компьютер') 
    markup.add(submit_turn_off_pc)
    bot.send_message(message.chat.id, 'Вот что я могу:', parse_mode='html', reply_markup=markup)
    sticker = open('stickers/sticker4.webp', 'rb')
    bot.send_sticker(message.chat.id, sticker)


@bot.message_handler()
def get_user_text(message):

    checked_off_pc = True
    checked_off_pc2 = True

    if  message.text == "Выключить компьютер":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) 
        confirm_off_pc = types.KeyboardButton("Да, я уверен") 
        rejection_off_pc = types.KeyboardButton("Нет, я передумал") 
        markup2.add(confirm_off_pc, rejection_off_pc)
        bot.send_message(message.chat.id, 'Ты уверен, что хочешь выключить компьютер?', parse_mode='html', reply_markup=markup2)

    elif message.text == "Да, я уверен":
         checked_off_pc = False

    elif message.text == "Нет, я передумал":
        checked_off_pc2 = False

    if checked_off_pc == False:
        os.system("shutdown /s /t 60")
        sticker = open('stickers/sticker3.webp', 'rb')
        bot.send_message(message.chat.id, 'Goodbye, my friend', parse_mode='html')
        bot.send_sticker(message.chat.id, sticker, reply_markup=KeyboardRemove)

    if checked_off_pc2 == False:
        bot.send_message(message.chat.id, 'Ладно, живи', parse_mode='html')
        sticker = open('stickers/sticker5.webp', 'rb')
        bot.send_sticker(message.chat.id, sticker, reply_markup=KeyboardRemove)
       
bot.polling(none_stop=True) # Постоянное функционирование бота