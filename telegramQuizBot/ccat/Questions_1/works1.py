import csv
with open('quiz_3.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'parameters{row[0]} = {{"chat_id":  "".format(chat_id) ,"question": "{row[1]}","options": json.dumps (["{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}"]),"is_anonymous":False,"correct_option_id": {row[6]},"type": "quiz"}}')
            line_count +=  1
    print(f'Processed {line_count} lines.')

    
