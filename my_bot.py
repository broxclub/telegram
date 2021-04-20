#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import packages 
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import telebot
bot = telebot.TeleBot('1777415629:AAEMDt8aA0froDlLmHJTtDHaZIhSOwLhL4Y')


# In[3]:





# In[ ]:


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
        
    stock = message.text
    #dwonload finance data 
    data = yf.download(stock,'2016-01-01', '2021-04-20')
    #specifying strategy parameters 
    short_ma = 5
    long_ma = 12
    fee = 0.002
    #coding technical analysis signals 
    data['MA'+str(short_ma)] = data['Close'].rolling(short_ma).mean()
    data['MA'+str(long_ma)] = data['Close'].rolling(long_ma).mean()
    data['return'] = data['Close'].pct_change()
    #simulating trading strategy
    start = long_ma
    data['signal'] = 2*(data['MA'+str(short_ma)] > data['MA'+str(long_ma)]) - 1
    BnH_return = np.array(data['return'][start+1:])
    MACD_return = np.array(data['return'][start+1:])*np.array(data['signal'][start:-1]) - fee*abs(np.array(data['signal'][start+1:]) - np.array(data['signal'][start:-1]))
    BnH = np.prod(1+BnH_return)**(252/len(BnH_return)) - 1
    MACD = np.prod(1+MACD_return)**(252/len(MACD_return)) - 1
    BnH_risk = np.std(BnH_return)*(252)**(1/2)
    MACD_risk = np.std(MACD_return)*(252)**(1/2)
    #visualising the results 
    print('buy-and-hold strategy return and risk :'+ str(round(BnH*100,2)) + ' % and ' + str(round(BnH_risk*100,2))+ ' %')
    print('MACD strategy return and risk '+ str(round(MACD*100,2)) + ' % and ' + str(round(MACD_risk*100,2))+ ' %')
    print(data['signal'])
    plt.plot(np.append(1,np.cumprod(1+BnH_return)))
    plt.plot(np.append(1,np.cumprod(1+MACD_return)))
    
    if data['signal'] == 1 : 
        bot.send_message(message.from_user.id, 'BUY')
    elif: data['signal'] == -1
        bot.send_message(message.from_user.id, 'SELL')
    else: 
        bot.send_message(message.from_user.id, 'HOLD')
        


# In[ ]:


bot.polling(none_stop=True)


# In[ ]:




