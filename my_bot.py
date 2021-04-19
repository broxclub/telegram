#!/usr/bin/env python
# coding: utf-8

# In[2]:


import telebot
bot = telebot.TeleBot('1777415629:AAEMDt8aA0froDlLmHJTtDHaZIhSOwLhL4Y')


# In[3]:


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')


# In[4]:


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


# In[ ]:


bot.polling(none_stop=True)


# In[ ]:




