import csv
import requests
import json
import time

#that stuff after /bot is the api token given by bot father /sendPoll is endpoint 
base_url = "https://api.telegram.org/bot5128510600:AAGp4B4kXQ3q2DLZxQrHAWtolwvaO61S7ZQ/sendPoll"
base_url_m = "https://api.telegram.org/bot5128510600:AAGp4B4kXQ3q2DLZxQrHAWtolwvaO61S7ZQ/sendMessage"

#test group
#chat_id = "-622742013"

#QuizzaHut_CCEE_Preparation
chat_id = "-1001750788753"

#Marathi Coders
#chat_id = "-1001751456595"

#CCAT
#QuizzaHut_CCAT_Preparation
#chat_id = "-1001868785533"

#interval in seconds
interval = 30


with open('Codes_java.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            i = {"chat_id": "{}".format(chat_id),
                 "question": "{}".format(row[1]),
                 "options": json.dumps (["{}".format(row[2]), "{}".format(row[3]), "{}".format(row[4]), "{}".format(row[5])]),
                 "is_anonymous":False,
                 "correct_option_id": row[6],
                 "type": "quiz"
                 }

            j =   {"chat_id": "{}".format(chat_id),
               "text": "{}".format(row[7])
               }  

            resp = requests.get(base_url_m, data = j)
            resp = requests.get(base_url, data = i)
            print(resp.text)
            line_count +=  1
            time.sleep(interval)
    print(f'Processed {line_count} lines.')
    
