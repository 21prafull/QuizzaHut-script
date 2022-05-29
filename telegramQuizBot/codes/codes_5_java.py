import requests
import json
import time

question1 = {"chat_id": "-1001750788753","question": "1. What is output of this java program?","options": json.dumps (["-1,0,1,2", "2,1,0,-1", "Stack overflow", "No output"]),"is_anonymous":False,"correct_option_id": 0,"type": "quiz"}
code1 = {"chat_id": "-1001750788753","text": "public class MemoryJava {\n public static void main(String[] args) {\n decreaseNumberbyOne(2);\n }\n public static void decreaseNumberbyOne(int num){ \n if(num >= 0){\n decreaseNumberbyOne(num -1);\n }\n System.out.println(""Number:""+num);\n }\n}"}


question3 = {"chat_id": "-1001750788753","question": "2. In what memory area, variable temp and variable card written in main () get stored?","options": json.dumps (["Heap, Heap", "Stack, stack", "Heap, Stack", "Stack, Heap"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz"}   
code3 = {"chat_id": "-1001750788753","text": "class CreditCard{\n int num;\n}\n\npublic class Bank { \n public static void main(String[] args) {\n int temp;\n CreditCard card;\n }\n}"}        


question4 = {"chat_id": "-1001750788753","question": "3. Choose the correct answer about the interface implementation in the code.","options": json.dumps (["Two interfaces cannot have a method with the same name.", "Compile-time error.", "Run-time error because of ambiguous call of the fill() method", "The interface implementation is fine."]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
code4 = {"chat_id": "-1001750788753","text": "interface Charger {\n void fill();\n}\ninterface Fuel {\n void fill();\n}\nclass Car implements Charger, Fuel {\n @Override\n public void fill() {\n System.out.println(""filling"");\n }\n}"}


question5 = {"chat_id": "-1001750788753","question": "4. The expressions in the if conditions 1, 2, and 3 will evaluate to:","options": json.dumps (["true, true, false", "false, true, false", "false, false, true", "true, false, true"]),"is_anonymous":False,"correct_option_id": 2 ,"type": "quiz"}
code5 = {"chat_id": "-1001750788753","text": "public class Sample { \npublic static void main(String[] args) { \nif (new String(""Java"") == ""Java"");//1 \nif (new String(""Java"") == new String(""Java""));// 2 \nif (new String(""Java"").equals(""Java"")); // 3 \n} \n}\n"}


question6 = {"chat_id": "-1001750788753","question": "5. What is the size of the HashMap?","options": json.dumps (["Compile-time error", "1", "2", "Run time error"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz"}    
code6 = {"chat_id": "-1001750788753","text": "import java.util.HashMap;\npublic class Sample {\npublic static void main(String[] args) {\nHashMap<Integer, String> map = new HashMap<Integer, String>();\nmap.put(1, ""Java"");\nmap.put(null, ""OOP"");\nmap.put(null, null);\n}\n}\n"}


question7 = {"chat_id": "-1001750788753","question": "6. What is the output of the program?","options": json.dumps (["Kiwi", "Kiwi, Mango", "Kiwi, Mango, Orange", "Compiler error"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
code7 = {"chat_id": "-1001750788753","text": "public class Sample { \npublic static void main(String[] args) { \nint n = 1; \nswitch(n){ \ncase 0:System.out.println(""Apple""); \nbreak; \ncase 1:System.out.println(""Kiwi""); \ncase 2:System.out.println(""Mango""); \ncase 4%3:System.out.println(""Orange""); \n} \n} \n}\n"}


question8 = {"chat_id": "-1001750788753","question": "7. What is the output?","options": json.dumps (["55QuizzaHut, Mock50", "10QuizzaHut, Mock5", "10, 5", "10QuizzaHut, Mock50"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
code8 = {"chat_id": "-1001750788753","text": "public class QuizzaHut {\npublic static void main(String args[]) {\nSystem.out.println(5 + 5 + ""QuizzaHut"");\nSystem.out.println(""Mock"" + 5 + 0);\n}\n}\n"}


question9 = {"chat_id": "-1001750788753","question": "8. What is the output of the following program?","options": json.dumps (["677", "Compilation error due to line 1", "Compilation error due to line 2", "Compilation error due to line 1 and line 2"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
code9 = {"chat_id": "-1001750788753","text": "public class Test \n{ \npublic static void main(String[] args) \n{ \nint value = 554; \nString var = (String)value; //line 1 \nString temp = ""123""; \nint data = (int)temp; //line 2 \nSystem.out.println(data + var); \n} \n}\n"}


question10 = {"chat_id": "-1001750788753","question": "9. What is the output of the following program?","options": json.dumps (["444.324", "444", "Runtime error", "Compilation error"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
code10 = {"chat_id": "-1001750788753","text": "public class Test \n{ \npublic static void main(String[] args) \n{ \ndouble data = 444.324; \nint value = data; \nSystem.out.println(data); \n} \n}\n"}


base_url = "https://api.telegram.org/bot5128510600:AAGp4B4kXQ3q2DLZxQrHAWtolwvaO61S7ZQ/sendMessage"
base_urlQ = "https://api.telegram.org/bot5128510600:AAGp4B4kXQ3q2DLZxQrHAWtolwvaO61S7ZQ/sendPoll"

arrayQ = [ question1, question3, question4 , question5 , question6, question7, question8, question9, question10  ]
arrayC = [ code1, code3, code4 , code5 , code6, code7, code8, code9, code10 ]

common = {  "chat_id": "-1001750788753",
            "text": " 👩🏻‍💻🖥️💻⌨️🧾👩🏻‍💻 \nRefer Following Code to Answer Next Question"
         }

for i in range (0, 9):
    resp = requests.get(base_url, data = common)
    resp = requests.get(base_url, data = arrayC[i])
    print(resp.text)
    respQ = requests.get(base_urlQ, data = arrayQ[i])
    print(respQ.text)
    time.sleep(45)
