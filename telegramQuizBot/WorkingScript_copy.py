import csv
import requests
import json
import time

#that stuff after /bot is the api token given by bot father /sendPoll is endpoint 
base_url = "https://api.telegram.org/bot5128510600:AAGp4B4kXQ3q2DLZxQrHAWtolwvaO61S7ZQ/sendPoll"

#test group
#chat_id = "-622742013"

# Two Groups:
chat_id_2 = "-1001751456595"
chat_id = "-1001638053483"

#ccpp prep
#chat_id = "-1001638053483"

#ccee prep
#chat_id = "-1001760361185"
#QuizzaHut_CCEE_Preparation
#chat_id = "-1001750788753"
#Marathi Coders
#chat_id = "-1001751456595"

#Main interval in seconds
interval = 45

#Test interval in seconds
#interval = 5

with open('ccpp_1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            i = {
                "chat_id": "{}".format(chat_id),
                "question": "{}".format(row[1]),
                "options": json.dumps (["{}".format(row[2]), "{}".format(row[3]), "{}".format(row[4]), "{}".format(row[5])]),
                "is_anonymous":False,
                "correct_option_id": row[6],
                "type": "quiz"
                }
            j = {
               "chat_id": "{}".format(chat_id_2),
               "question": "{}".format(row[1]),
                "options": json.dumps (["{}".format(row[2]), "{}".format(row[3]), "{}".format(row[4]), "{}".format(row[5])]),
                "is_anonymous":False,
                "correct_option_id": row[6],
                "type": "quiz"
                }
            resp = requests.get(base_url, data = i)
            print(line_count, resp.text)
            resp = requests.get(base_url, data = j)
            print(resp.text)
            line_count +=  1
            time.sleep(interval)
    print(f'Processed {line_count} lines.')
    
