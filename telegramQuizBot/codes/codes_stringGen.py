import csv
chat_id = "-622742013"
with open('java_codes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'question{row[0]} = {{"chat_id": ""{chat_id},"question": "{row[1]}","options": json.dumps (["{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}"]),"is_anonymous":False,"correct_option_id": {row[6]},"type": "quiz"}}')
            print(f'code{row[0]} = {{"chat_id": ""{chat_id},"text": "{row[7]}"}}')
            print('\n')
            line_count +=  1
    print(f'Processed {line_count} lines.')

    
