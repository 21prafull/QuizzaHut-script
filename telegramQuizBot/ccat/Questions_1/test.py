import requests
import json
import time

# Marathi Coders Chat Id
# chat_id = "-1001751456595"

# Test Group Chat ID
chat_id = "-622742013"

#chat_id = "-1001751456595"


parameters1 = {"chat_id":  "{}".format(chat_id) ,"question": "1. If the given array is sorted which sorting algorithm uses minimum time?","options": json.dumps (["Merge Sort", " Quick Sort", "Selection ", "Insertion"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
parameters2 = {"chat_id":  "{}".format(chat_id) ,"question": "2. Which of the following data structure is used to implement depth first traversal algorithm?","options": json.dumps (["Array", "Linked List", "Stack", "Queue"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz"}
parameters3 = {"chat_id":  "{}".format(chat_id) ,"question": "3. What is the condition to check stack is full or not in a dynamic stack?","options": json.dumps (["top == SIZE", "top == SIZE-1", "top == NULL", "None of the above"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
parameters4 = {"chat_id":  "{}".format(chat_id) ,"question": "4. Convert given infix expression into its equivalent postfix expression: Infix expression is: (A*B)*(C/D)+E*F-G*H","options": json.dumps (["AB*CD/EF**+GH*-", "AB*CD/*EF*+GH*-", "ABCD*/*EF*+GH*-", "AB*CD/*EF*GH+*-"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz"}
parameters5 = {"chat_id":  "{}".format(chat_id) ,"question": "5. What is time complexity of addition and deletion operations on an array?","options": json.dumps (["O(1)", "O(n)", "O(log n)", "none of the above"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz"}
parameters6 = {"chat_id":  "{}".format(chat_id) ,"question": "6. On an array data structure searching operation can be performed efficiently in _____ time.","options": json.dumps (["O(1)", "O(log n)", "O(n log n)", "none of the above"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz"}
parameters7 = {"chat_id":  "{}".format(chat_id) ,"question": "7. Binary Search algorithm is also called as:","options": json.dumps (["Logarithmic Search", "Half-interval Search", "Exponential Search", "Both options 1 and 2)"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
parameters8 = {"chat_id":  "{}".format(chat_id) ,"question": "8. Which of the following is a system program?","options": json.dumps (["compiler", "loader", "assembler", "all of the above"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz"}
parameters9 = {"chat_id":  "{}".format(chat_id) ,"question": "9. Output of the linker is ___________.","options": json.dumps (["an object code", "an executable code", "an intermediate code", "an assembly language code"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz"}
parameters10 = {"chat_id":  "{}".format(chat_id) ,"question": "10. Which of the following program provides graphical user interface in Windows Operating System?","options": json.dumps (["cmd.exe", "explorer.exe", "command.com", "none of the above"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz"}
parameters11 = {"chat_id":  "{}".format(chat_id) ,"question": "11. In user mode, value of mode bit is ____.","options": json.dumps (["0", "-1", "1", "none of the above"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz"}
parameters12 = {"chat_id":  "{}".format(chat_id) ,"question": "12. _______ copies an execution context of a process which is scheduled by the scheduler from its PCB and restores it onto the CPU registers.","options": json.dumps (["Loader", "Interrupt Handler", "Job Scheduler", "Dispatcher"]),"is_anonymous":False,"correct_option_id": 3,"type": "quiz"}
parameters13 = {"chat_id":  "{}".format(chat_id) ,"question": "13. In which of the following page replacement algorithm page will not get used in near future will be replaced by requested page?","options": json.dumps (["LRU Page Replacement Algorithm", "FIFO Page Replacement Algorithm", "Optimal Page Replacement Algorithm", "MFU Page Replacement Algorithm"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz"}
parameters14 = {"chat_id":  "{}".format(chat_id) ,"question": "14. Ageing technique is used in which scheduling algorithm?","options": json.dumps (["Round Robin ", "Priority ", "SRTF", "all of the above"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz"}
parameters15 = {"chat_id":  "{}".format(chat_id) ,"question": "15. Which is the fastest IPC technnique?","options": json.dumps (["Shared Memory Model", "Socket", "Pipe Communication", "Message queue"]),"is_anonymous":False,"correct_option_id": 0,"type": "quiz"}
parameters16 = {"chat_id":  "{}".format(chat_id) ,"question": "16. OSI Model has ______________layers.","options": json.dumps (["5", "6", "7", "8"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz"}
parameters17 = {"chat_id":  "{}".format(chat_id) ,"question": "17. 172.31.25.151 is an example of_______________ IP Address.","options": json.dumps (["public", "private", "class A", "class B"]),"is_anonymous":False,"correct_option_id": 1,"type": "quiz"}
parameters18 = {"chat_id":  "{}".format(chat_id) ,"question": "18. Which of the following language does the computer understand?","options": json.dumps ([" Computer understands only C Language", " Computer understands only Assembly Language", "Computer understands only Binary Language", "Computer understands only BASIC"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz"}
parameters19 = {"chat_id":  "{}".format(chat_id) ,"question": "19. Which of the following is the smallest unit of data in a computer?","options": json.dumps (["Bit", "Byte ", "Nibble", "KB"]),"is_anonymous":False,"correct_option_id": 0,"type": "quiz"}
parameters20 = {"chat_id":  "{}".format(chat_id) ,"question": "20. Which of the following is designed to control the operations of a computer?","options": json.dumps (["User", "Application Software", "System Software", "Utility Software"]),"is_anonymous":False,"correct_option_id": 2,"type": "quiz"}

base_url = "https://api.telegram.org/bot5507486988:AAFLXo1lKHqSuJm5NSLp418xjTDRC7cytec/sendPoll"

arrayQ = [ parameters1, parameters2, parameters3, parameters4, parameters5, parameters6, parameters7, parameters8, parameters9, parameters10, parameters11, parameters12, parameters13, parameters14, parameters15, parameters16, parameters17, parameters18, parameters19, parameters20]
print(arrayQ[19])
# for i in range(0, 19):
#     respQ = requests.get(base_url, data = arrayQ[i])
#     print(respQ.text)
#     time.sleep(1)