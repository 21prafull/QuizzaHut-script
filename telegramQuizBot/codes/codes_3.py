import requests
import json
import time

question1 = {"chat_id": "-1001760361185","question": "What is the output of this code?","options": json.dumps (["It will not compile because of line 4.", "It will not compile because of line 3.", "123", "1234"]),"is_anonymous":False,"correct_option_id": 0,"type": "quiz","explanation": ""}
code1 = {"chat_id": "-1001760361185","text": "1: class Main { \n2: public static void main (String[] args) { \n3: int array[] = {1, 2, 3, 4}; 1\n4: for (int i = 0; i < array.size(); i++) { \n5: System.out.print(array[i]); \n6: } \n7: } \n8: }\n"}


question2 = {"chat_id": "-1001760361185","question": "Which of the following can replace the CODE SNIPPET to make the code below print ""Hello World""?" ,"options": json.dumps (["super1.print(); super2.print();", "this.print();", "super.print();", "Interface1.print(); Interface2.print();"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz","explanation": ""}
code2 = {"chat_id": "-1001760361185","text": "interface Interface1 {\n static void print() {\n System.out.print(""Hello"");\n }\n}\n\ninterface Interface2 {\n static void print() {\n System.out.print(""World!"");\n }\n}"}


question3 = {"chat_id": "-1001760361185","question": "What does the following code print?","options": json.dumps (["CD", "CDE", "D", "abcde"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz","explanation": ""}
code3 = {"chat_id": "-1001760361185","text": "String str = ""abcde"";\nstr.trim();\nstr.toUpperCase();\nstr.substring(3, 4);\nSystem.out.println(str); "}


question4 = {"chat_id": "-1001760361185","question": "What does the following code print?","options": json.dumps (["It will show a stack trace with a runtime exception.", "java.lang.Exception", "It will run and throw an exception.", "It will not compile."]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz","explanation": ""}
code4 = {"chat_id": "-1001760361185","text": "class Main {\n public static void main (String[] args){\n System.out.println(print(1));\n }\n static Exception print(int i){\n if (i>0) {\n return new Exception();\n } else {\n throw new RuntimeException();\n }\n }\n}\n"}


question5 = {"chat_id": "-1001760361185","question": "What is the output of this code?","options": json.dumps (["The code does not compile.", "truefalse", "truetrue", "falsetrue"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz","explanation": ""}
code5 = {"chat_id": "-1001760361185","text": "class Main { \npublic static void main (String[] args) { \nList list = new ArrayList(); \nlist.add(""hello""); \nlist.add(2); \nSystem.out.print(list.get(0) instanceof Object); \nSystem.out.print(list.get(1) instanceof Integer); \n} \n} \n"}


question6 = {"chat_id": "-1001760361185","question": "What is the result of this code?","options": json.dumps (["It will not compile because of line 10.", "Hello!", "It will not compile because of line 2.", "World!"]),"is_anonymous":False,"correct_option_id": 0,"type": "quiz","explanation": ""}
code6 = {"chat_id": "-1001760361185","text": "1: class MainClass {\n2: final String message(){\n3: return ""Hello!"";\n4: }\n5: }\n\n6: class Main extends MainClass {\n7: public static void main(String[] args) {\n8: System.out.println(message());\n9: }\n\n10: String message(){\n11: return \"World!\";\n12: }\n13: }\n"}

question7 = {"chat_id": "-1001760361185","question": "Given this code, which command will output ""2""?","options": json.dumps(["java Main 1 2 \"3 4\" 5", "java Main 1 \"2\" \"2\" 5", "java Main.class 1 \"2\" 2 5", "java Main 1 \"2\" \"3 4\" 5"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz","explanation": ""}
code7 = {"chat_id": "-1001760361185","text": "class Main { \npublic static void main(String[] args) { \nSystem.out.println(args[2]); \n} \n}"}


question8 = {"chat_id": "-1001760361185","question": "What is the output of this code?","options": json.dumps (["123451234512345", "Nothing - this will not compile.", "a negative integer value", "12345100000"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz","explanation": ""}
code8 = {"chat_id": "-1001760361185","text": "class Main {  \npublic static void main(String[] args){  \nint a = 123451234512345;  \nSystem.out.println(a);  \n}  \n} \n"}


question9 = {"chat_id": "-1001760361185","question": "What is the output of this code?","options": json.dumps (["The code does not compile", "A runtime exception is thrown.", "world!!world", "world!world!"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz","explanation": ""}
code9 = {"chat_id": "-1001760361185","text": "class Main {  \npublic static void main (String[] args) {  \nString message = \"Hello world!\";  \nString newMessage = message.substring(6, 12)  \n+ message.substring(12, 6);  \nSystem.out.println(newMessage);  \n}  \n} \n"}


question10 = {"chat_id": "-1001760361185","question": "What is the output of this code?","options": json.dumps (["-1", "0", "StringIndexOutOfBoundsException", "ArrayIndexOutOfBoundsException"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz","explanation": ""}
code10 = {"chat_id": "-1001760361185","text": "public class CDAC{ \npublic static void main(String a[]){ \nString s1 = \"Sun\"; \nSystem.out.println(s1.substring(5)); \n} \n} \n"}


question11 = {"chat_id": "-1001760361185","question": "","options": json.dumps (["Prints: ABC", "Prints: A B C", "Prints: ABCD", "Prints: ABDC"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz","explanation": ""}
code11 = {"chat_id": "-1001760361185","text": "class DAC { \npublic static void main(String[] s) { \nString s1 = \"A\", s2 = \" B \", s3 = \"C\"; \ns2.trim(); s3.concat(\"D\"); \nSystem.out.print(s1 + s2 + s3); \n} \n} \n"}

base_url = "https://api.telegram.org/bot5128510600:AAGp4B4kXQ3q2DLZxQrHAWtolwvaO61S7ZQ/sendMessage"
base_urlQ = "https://api.telegram.org/bot5128510600:AAGp4B4kXQ3q2DLZxQrHAWtolwvaO61S7ZQ/sendPoll"

arrayQ = [ question1 , question2 , question3 , question4 , question5 , question6 , question7 , question8 , question9 , question10 , question11 ]
arrayC = [ code1 , code2 , code3 , code4 , code5 , code6 , code7 , code8 , code9 , code10 , code11 ]

common = {  "chat_id": "-1001750788753",
            "text": " 👩🏻‍💻🖥️💻⌨️🧾👩🏻‍💻 \nRefer Following Code to Answer Next Question"
         }

for i in range (0, 10):
  resp = requests.get(base_url, data = common)
  resp = requests.get(base_url, data = arrayC[i])
  print(resp.text)
  respQ = requests.get(base_urlQ, data = arrayQ[i])
  print(respQ.text)
  time.sleep(60)
