
from COLD_PREDICT import model_C
from FLU_PREDICT import model_Fl
from FEVER_PREDICT import model_F
from COVID_PREDICT import model_C19
from NORMAL_PREDICT import model_N
import telebot
from telebot import types
import time


chat_token = "<chat bot token>"

bot = telebot.TeleBot(chat_token)

user_dict= {}

num = [ 95 ,  95.1,  95.2,  95.3,  95.4,  95.5,  95.6,  95.7,  95.8,
        95.9,  96,  96.1,  96.2,  96.3,  96.4,  96.5,  96.6,  96.7,
        96.8,  96.9,  97,  97.1,  97.2,  97.3,  97.4,  97.5,  97.6,
        97.7,  97.8,  97.9,  98,  98.1,  98.2,  98.3,  98.4,  98.5,
        98.6,  98.7,  98.8,  98.9,  99 ,  99.1,  99.2,  99.3,  99.4,
        99.5,  99.6,  99.7,  99.8,  99.9, 100, 100.1, 100.2, 100.3,
       100.4, 100.5, 100.6, 100.7, 100.8, 100.9, 101, 101.1, 101.2,
       101.3, 101.4, 101.5, 101.6, 101.7, 101.8, 101.9, 102, 102.1,
       102.2, 102.3, 102.4, 102.5, 102.6, 102.7, 102.8, 102.9, 103,
       103.1, 103.2, 103.3, 103.4, 103.5, 103.6, 103.7, 103.8, 103.9,
       104, 104.1, 104.2, 104.3, 104.4, 104.5, 104.6, 104.7, 104.8,
       104.9, 105, 105.1, 105.2, 105.3, 105.4, 105.5, 105.6, 105.7,
       105.8, 105.9, 106, 106.1, 106.2, 106.3, 106.4, 106.5, 106.6,
       106.7, 106.8, 106.9, 107, 107.1, 107.2, 107.3, 107.4, 107.5,
       107.6, 107.7, 107.8, 107.9, 108, 108.1, 108.2, 108.3, 108.4,
       108.5, 108.6, 108.7, 108.8, 108.9, 109, 109.1, 109.2, 109.3,
       109.4, 109.5, 109.6, 109.7, 109.8, 109.9, 110, 110.1, 110.2,
       110.3, 110.4, 110.5, 110.6, 110.7, 110.8, 110.9, 111, 111.1,
       111.2, 111.3, 111.4, 111.5, 111.6, 111.7, 111.8, 111.9]

class User:
    def __init__(self,name):
        self.name = name
        self.age = None
        self.Btemp = None
        self.outside = None
        self.cough = None
        self.phlegm = None
        self.chillness = None
        self.chestPressure = None
        self.congestion = None
        self.muscleAche = None
        self.runnyStuffnose = None
        self.fatigue = None
        self.sneezing = None
        self.soreThroat = None
        self.breathingProb = None
        self.tasteProb = None
        self.smellProb = None
        self.speechProb = None
        self.output = None

#handle "/start" and "/help" command
@bot.message_handler(commands = ['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.reply_to(message,"""\
Hi there, im Predictor19_bot!
made by Deepak Avudiappan
(BlueOceanAi.Tech)
for predicting COVID-19.
""")
    time.sleep(1)
    bot.send_message(chat_id, "😇")
    msg = bot.send_message(chat_id, "What is your name?")
    bot.register_next_step_handler(msg,greet)


def greet(message):
    chat_id = message.chat.id
    name = message.text
    global user
    user = User(name)
    bot.send_message(chat_id, 'Nice to meet you ' + user.name)
    #msg = bot.send_message(chat_id, 'To start your test type /test!')
    test(message)
    

def test(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id,"Hey " + user.name + """ If you face any problem, please type /help""")
    time.sleep(1)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Start Test!')
    msg = bot.send_message(chat_id, 'Hope your result is normal ' + user.name , reply_markup=markup)
    bot.send_message(chat_id,'😊')
    time.sleep(1)
    bot.register_next_step_handler(msg,process_name_step)
    
@bot.message_handler(commands = ['help'])
def helpc(message):
    bot.reply_to(message,"""\
If you got Backend error, you can start your test by /start.
Else write to blueoceanai.tech@gmail.com
Our team will respond to you shortly.
""")
    #bot.register_next_step_handler(msg,process_name_step)
    
def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        time.sleep(1)
        st = message.text
        if st == u'Start Test!':
            bot.send_message(chat_id,"PLEASE ANSWER CAREFULLY!! ")
            time.sleep(1)
            bot.reply_to(message, """Let's start your test! ====>""")
            user_dict[chat_id] = user
            msg = bot.reply_to(message,"How old are you?")
            bot.register_next_step_handler(msg,process_age_step)
    except Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
    
def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message,"Age should be a number. How old are you?")
            bot.register_next_step_handler(msg,process_age_step)
            return
        else:
            user = user_dict[chat_id]
            user.age = int(age)
        bot.reply_to(message,"What is your current body temprature in 'fahrenheit'?")
        bot.register_next_step_handler(message,process_Btemp_step)
    except Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_Btemp_step(message):
    try:
        chat_id = message.chat.id
        Btemp = message.text
        if float(Btemp) not in num:
            msg = bot.reply_to(message,"Body Temperature must be range(95 to 112)fahrenheit!")
            bot.register_next_step_handler(msg,process_Btemp_step)
            return
        user = user_dict[chat_id]
        user.Btemp = float(Btemp)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Have you visited any public place within this month?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_outside_step)
    except Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_outside_step(message):
    try:
        chat_id = message.chat.id
        outside = message.text
        user = user_dict[chat_id]
        if (outside == u'Yes') or (outside == u'No'):
            user.outside = outside
        else:
            raise Exception()
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you Cough?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_cough_step)
    except Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")

def process_cough_step(message):
    try:
        chat_id = message.chat.id
        cough = message.text
        user = user_dict[chat_id]
        if (cough == u'Yes') or (cough == u'No'):
            user.cough = cough
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you have Phlegm?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_phlegm_step)
    except Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")

def process_phlegm_step(message):
    try:
        chat_id = message.chat.id
        phlegm = message.text
        user = user_dict[chat_id]
        if (phlegm == u'Yes') or (phlegm == u'No'):
            user.phlegm = phlegm
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you feel chillness?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_chillness_step)
    except Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_chillness_step(message):
    try:
        chat_id = message.chat.id
        chillness = message.text
        user = user_dict[chat_id]
        if (chillness == u'Yes') or (chillness == u'No'):
            user.chillness = chillness
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you feel succumbed in chest?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_chestPressure_step)
    except Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_chestPressure_step(message):
    try:
        chat_id = message.chat.id
        chestPressure = message.text
        user = user_dict[chat_id]
        if (chestPressure == u'Yes') or (chestPressure == u'No'):
            user.chestPressure = chestPressure
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you feel congestion?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_congestion_step)
    except Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
            
def process_congestion_step(message):
    try:
        chat_id = message.chat.id
        congestion = message.text
        user = user_dict[chat_id]
        if (congestion == u'Yes') or (congestion == u'No'):
            user.congestion = congestion
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you have muscle pain?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_muscleAche_step)
    except Exception as e:
         bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_muscleAche_step(message):
    try:
        chat_id = message.chat.id
        muscleAche = message.text
        user = user_dict[chat_id]
        if (muscleAche == u'Yes') or (muscleAche == u'No'):
            user.muscleAche = muscleAche
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you have runny or stuffed nose?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_runnyStuffnose_step)
    except  Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_runnyStuffnose_step(message):
    try:
        chat_id = message.chat.id
        runnyStuffnose = message.text
        user = user_dict[chat_id]
        if (runnyStuffnose == u'Yes') or (runnyStuffnose == u'No'):
            user.runnyStuffnose = runnyStuffnose
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you feel fatigue?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_fatigue_step)
    except  Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")

def process_fatigue_step(message):
    try:
        chat_id = message.chat.id
        fatigue = message.text
        user = user_dict[chat_id]
        if (fatigue == u'Yes') or (fatigue == u'No'):
            user.fatigue = fatigue
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you sneeze often?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_sneezing_step)
    except  Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_sneezing_step(message):
    try:
        chat_id = message.chat.id
        sneezing = message.text
        user = user_dict[chat_id]
        if (sneezing == u'Yes') or (sneezing == u'No'):
            user.sneezing = sneezing
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you have sore throat?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_soreThroat_step)
    except  Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_soreThroat_step(message):
    try:
        chat_id = message.chat.id
        soreThroat = message.text
        user = user_dict[chat_id]
        if (soreThroat == u'Yes') or (soreThroat == u'No'):
            user.soreThroat = soreThroat
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you have difficulty in breathing?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_breathingProb_step)
    except  Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_breathingProb_step(message):
    try:
        chat_id = message.chat.id
        breathingProb = message.text
        user = user_dict[chat_id]
        if (breathingProb == u'Yes') or (breathingProb == u'No'):
            user.breathingProb = breathingProb
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you feel tasteless when having meal?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_tasteProb_step)
    except  Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_tasteProb_step(message):
    try:
        chat_id = message.chat.id
        tasteProb = message.text
        user = user_dict[chat_id]
        if (tasteProb == u'Yes') or (tasteProb == u'No'):
            user.tasteProb = tasteProb
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you have sense of smell?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_smellProb_step)
    except  Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_smellProb_step(message):
    try:
        chat_id = message.chat.id
        smellProb = message.text
        user = user_dict[chat_id]
        if (smellProb == u'Yes') or (smellProb == u'No'):
            user.smellProb = smellProb
        else:
            raise Exception
        markup = types.ReplyKeyboardMarkup(one_time_keyboard = True)
        markup.add('Yes','No')
        msg = bot.reply_to(message,"Do you suffer difficuly in speech?",reply_markup=markup)
        bot.register_next_step_handler(msg,process_speechProb_step)
    except  Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")
        
def process_speechProb_step(message):
    try:
        chat_id = message.chat.id
        speechProb = message.text
        user = user_dict[chat_id]
        if (speechProb == u'Yes') or (speechProb == u'No'):
            user.speechProb = speechProb
        else:
            raise Exception
        msg = bot.send_message(chat_id,"Predicting=======>")
        lis = [user.age, user.Btemp, user.outside, user.cough, user.phlegm, user.chillness, user.chestPressure, user.congestion, user.muscleAche, user.runnyStuffnose, user.fatigue, user.sneezing, user.soreThroat, user.breathingProb, user.tasteProb, user.smellProb, user.speechProb]
        user.output = lis
        #bot.register_next_step_handler(msg,process_final_step)
        process_final_step(message)
    except  Exception as e:
        bot.send_message(chat_id, """Ooops, Backend error!\
Please write to blueoceanai.tech@gmail.com
Our team will respond to you.""")

def predict(X,P_value_cold,P_value_flu,P_value_fever,P_value_covid,P_value_normal):
    temp = []
    if sum(model_C.select(X)) >= P_value_cold:
        temp.append(1)
    else:
        temp.append(0)
    if sum(model_Fl.select(X)) >= P_value_flu:
        temp.append(1)
    else:
        temp.append(0)
    if sum(model_F.select(X)) >= P_value_fever:
        temp.append(1)
    else:
        temp.append(0)
    if sum(model_C19.select(X)) >= P_value_covid:
        temp.append(1)
    else:
        temp.append(0)
    if sum(model_N.select(X)) >= P_value_normal:
        temp.append(1)
    else:
        temp.append(0)
    return(temp)
def conv(val):
    num = []
    out = []
    for string in val:
        if type(string) == str:
            if string == "No":
                st = string.replace("No", "0") 
            else :
                st = string.replace("Yes","1")
            num.append(st)
        else:
            num.append(string)

    for sr in num:
        if type(sr) is str:
            sr = int(sr)
            out.append(sr)
        else:
            out.append(sr) 
    return out

def process_final_step(message):
    chat_id = message.chat.id
    user = user_dict[chat_id]
    print(user.output)
    l= conv(user.output)
    li = predict(l,5,7,3,6,5)
    if li[0] == 1: #cold
        bot.send_message(chat_id, "Our model predicted that you have 'Cold'")
        bot.send_message(chat_id,"Most people recover on their own within two weeks. If you Not recover please visit nearby doctor or contact (India)corona-virus help line: +91-11-23978046, or 1075 (toll free")
        time.sleep(1)
        bot.send_message(chat_id, "Dont forget the safty protocols!")
        time.sleep(1)
        bot.send_message(chat_id, "1) Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water. This eliminates germs including viruses that may be on your hands.")
        time.sleep(0.7)
        bot.send_message(chat_id, "2) Avoid touching your eyes, nose and mouth. Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth. From there, the virus can enter your body and infect you.")
        time.sleep(0.7)
        bot.send_message(chat_id, "3) Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately into a closed bin and wash your hands. By following good ‘respiratory hygiene’, you protect the people around you from viruses, which cause colds, flu and COVID-19.")
        time.sleep(0.7)
        bot.send_message(chat_id, "4) Clean and disinfect surfaces frequently especially those which are regularly touched, such as door handles, faucets and phone screens.")
        time.sleep(0.7)
        bot.send_message(chat_id, "😇")
    elif li[1] == 1: #flu
        bot.send_message(chat_id, "Our model predicted that you have 'Flu'")
        bot.send_message(chat_id,"Most people recover on their own within two weeks. If you Not recover please visit nearby doctor or contact (India)corona-virus help line: +91-11-23978046, or 1075 (toll free")
        time.sleep(1)
        bot.send_message(chat_id, "Dont forget the safty protocols!")
        time.sleep(1)
        bot.send_message(chat_id, "1) Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water. This eliminates germs including viruses that may be on your hands.")
        time.sleep(0.7)
        bot.send_message(chat_id, "2) Avoid touching your eyes, nose and mouth. Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth. From there, the virus can enter your body and infect you.")
        time.sleep(0.7)
        bot.send_message(chat_id, "3) Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately into a closed bin and wash your hands. By following good ‘respiratory hygiene’, you protect the people around you from viruses, which cause colds, flu and COVID-19.")
        time.sleep(0.7)
        bot.send_message(chat_id, "4) Clean and disinfect surfaces frequently especially those which are regularly touched, such as door handles, faucets and phone screens.")
        time.sleep(0.7)
        bot.send_message(chat_id, "😇")
        
    elif li[2] == 1: #fever
        bot.send_message(chat_id, "Our model predicted that you have 'Fever'")
        bot.send_message(chat_id,"Most people recover on their own within hours or 1 day. If you Not recover please visit nearby doctor or contact (India)corona-virus help line: +91-11-23978046, or 1075 (toll free")
        time.sleep(1)
        bot.send_message(chat_id, "Dont forget the safty protocols!")
        time.sleep(1)
        bot.send_message(chat_id, "1) Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water. This eliminates germs including viruses that may be on your hands.")
        time.sleep(0.7)
        bot.send_message(chat_id, "2) Avoid touching your eyes, nose and mouth. Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth. From there, the virus can enter your body and infect you.")
        time.sleep(0.7)
        bot.send_message(chat_id, "3) Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately into a closed bin and wash your hands. By following good ‘respiratory hygiene’, you protect the people around you from viruses, which cause colds, flu and COVID-19.")
        time.sleep(0.7)
        bot.send_message(chat_id, "4) Clean and disinfect surfaces frequently especially those which are regularly touched, such as door handles, faucets and phone screens.")
        time.sleep(0.7)
        bot.send_message(chat_id, "😇")
        
    elif li[3] == 1: #covid-19
        bot.send_message(chat_id, "Our model predicted that you have 'COVID-19'")
        bot.send_message(chat_id,"Most people recover,if symptoms is getting worst. Please visit nearby doctor or contact (India)corona-virus help line: +91-11-23978046, or 1075 (toll free")
        time.sleep(1)
        bot.send_message(chat_id, "Dont forget the safty protocols!")
        time.sleep(1)
        bot.send_message(chat_id, "1) Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water. This eliminates germs including viruses that may be on your hands.")
        time.sleep(0.7)
        bot.send_message(chat_id, "2) Avoid touching your eyes, nose and mouth. Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth. From there, the virus can enter your body and infect you.")
        time.sleep(0.7)
        bot.send_message(chat_id, "3) Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately into a closed bin and wash your hands. By following good ‘respiratory hygiene’, you protect the people around you from viruses, which cause colds, flu and COVID-19.")
        time.sleep(0.7)
        bot.send_message(chat_id, "4) Clean and disinfect surfaces frequently especially those which are regularly touched, such as door handles, faucets and phone screens.")
        time.sleep(0.7)
        bot.send_message(chat_id, "😇")
        
    elif li[4] == 1: #normal
        bot.send_message(chat_id, "Our model predicted that you are 'Normal'")
        time.sleep(1)
        bot.send_message(chat_id, "😎")
        bot.send_message(chat_id, "Have fun but dont forget the safty protocols!")
        time.sleep(1)
        bot.send_message(chat_id, "1) Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with soap and water. This eliminates germs including viruses that may be on your hands.")
        time.sleep(0.7)
        bot.send_message(chat_id, "2) Avoid touching your eyes, nose and mouth. Hands touch many surfaces and can pick up viruses. Once contaminated, hands can transfer the virus to your eyes, nose or mouth. From there, the virus can enter your body and infect you.")
        time.sleep(0.7)
        bot.send_message(chat_id, "3) Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. Then dispose of the used tissue immediately into a closed bin and wash your hands. By following good ‘respiratory hygiene’, you protect the people around you from viruses, which cause colds, flu and COVID-19.")
        time.sleep(0.7)
        bot.send_message(chat_id, "4) Clean and disinfect surfaces frequently especially those which are regularly touched, such as door handles, faucets and phone screens.")
        time.sleep(0.7)
        bot.send_message(chat_id, "😇")

    
    
    
# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling()
