import requests
import json
import time

question1 = {"chat_id": "-1001750788753","question": "What will happen when the below code snippet is executed?","options": json.dumps (["The code will be executed successfully and no output will be generated", "The code will be executed successfully and random output will be generated", "The code will show a compile time error", "The code will run for some time and stop when the stack overflows"]),"is_anonymous":False,"correct_option_id": 
3,"type": "quiz"}
code1 = {"chat_id": "-1001750788753","text": "void my_recursive_function()\n{\n   my_recursive_function();\n}\nint main()\n{\n   my_recursive_function();\n   return 0;\n}\n"}      


question2 = {"chat_id": "-1001750788753","question": "What is the output of the following code?","options": json.dumps (["10", "1", "10 9 8 … 1 0", " 10 9 8 … 1"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
code2 = {"chat_id": "-1001750788753","text": "void my_recursive_function(int n)\n{\n    if(n == 0)\n    return;\n    printf(\"%d \",n);\n    my_recursive_function(n-1);\n}\nint main()\n{\n    my_recursive_function(10);\n    return 0;\n}\n"}


question3 = {"chat_id": "-1001750788753","question": "What does the following recursive code do?","options": json.dumps (["Prints the numbers from 10 to 1", "Prints the numbers from 10 to 0", "Prints the numbers from 1 to 10", " Prints the numbers from 0 to 10"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz"}
code3 = {"chat_id": "-1001750788753","text": "void my_recursive_function(int n)\n{\n     if(n == 0)\n     return;\n     my_recursive_function(n-1);\n     printf(\"%d \",n);\n}\nint main()\n{\n     my_recursive_function(10);\n     return 0;\n}\n"}


question4 = {"chat_id": "-1001750788753","question": "What will be the output of the following Java program?","options": json.dumps (["1", "30", "120", "Runtime Error"]),"is_anonymous":False,"correct_option_id": 0,"type": "quiz"}
code4 = {"chat_id": "-1001750788753","text": "class recursion \n    {\n        int fact(int n) \n        {\n            int result;\n            if (n == 1)\n                return 1;\n            result = fact(n - 1) * n;\n            return result;\n        }\n    } \n    class Output \n    {\n        public static void main(String args[]) \n        {\n            recursion obj = new recursion() ;\n            System.out.print(obj.fact(1));\n        }\n    }\n"}


question5 = {"chat_id": "-1001750788753","question": "What will be the output of the following Java program?","options": json.dumps (["24", "30", "120", "720"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz"}
code5 = {"chat_id": "-1001750788753","text": "class recursion \n    {\n        int fact(int n) \n        {\n            int result;\n            if (n == 1)\n                return 1;\n            result = fact(n - 1) * n;\n            return result;\n        }\n    } \n    class Output \n    {\n        public static void main(String args[]) \n        {\n            recursion obj = new recursion() ;\n            System.out.print(obj.fact(5));\n        }\n    }\n"}


question6 = {"chat_id": "-1001750788753","question": "What will be the output of the following Java program?","options": json.dumps (["0", "1", "Compilation Error", "Runtime Error"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
code6 = {"chat_id": "-1001750788753","text": "class recursion \n    {\n        int func (int n) \n        {\n            int result;\n            result = func (n - 1);\n  return result;\n        }\n    } \n    class Output \n    {\n        public static void main(String args[]) \n        {\n            recursion obj = new recursion() ;\n            System.out.print(obj.func(12));\n        }\n    }\n"}


base_url = "https://api.telegram.org/bot5128510600:AAGp4B4kXQ3q2DLZxQrHAWtolwvaO61S7ZQ/sendMessage"
base_urlQ = "https://api.telegram.org/bot5128510600:AAGp4B4kXQ3q2DLZxQrHAWtolwvaO61S7ZQ/sendPoll"

arrayQ = [ question1 , question2 , question3 , question4 , question5 , question6 ]
arrayC = [ code1 , code2 , code3 , code4 , code5 , code6 ]

common = {  "chat_id": "-1001750788753",
            "text": " 👩🏻‍💻🖥️💻⌨️🧾👩🏻‍💻 \nRefer Following Code to Answer Next Question"
         }

#for i in range (0, 5):
resp = requests.get(base_url, data = common)
resp = requests.get(base_url, data = arrayC[5])
print(resp.text)
respQ = requests.get(base_urlQ, data = arrayQ[5])
print(respQ.text)
time.sleep(60)
