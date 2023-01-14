import requests
import json

#that stuff after /bot is the api token given by bot father /sendPoll is endpoint

# mc_bot API Token: 5507486988:AAFLXo1lKHqSuJm5NSLp418xjTDRC7cytec
base_url = "https://api.telegram.org/bot5507486988:AAFLXo1lKHqSuJm5NSLp418xjTDRC7cytec/sendMessage"


parameters1 = {
                "chat_id": "-1001750788753",
                "text": "Hi we are testing Bots! This bot will be used to post questions for CCAT and CCEE when we conduct mock exams."
               }

#this one is stupid way to do it but i am too lazy to find better way.
#array = [ parameters1, parameters2, parameters3, parameters4, parameters5 ]

resp = requests.get(base_url, parameters1)
print(resp.text)