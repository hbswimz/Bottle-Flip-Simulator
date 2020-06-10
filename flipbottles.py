# Bottle-Flip-Simulator
# This program flips as many bottles as the user desires and if they would like, email them the results.#

import time
import random
import smtplib
from email.message import EmailMessage


total_flips = 0.0
flip_in_a_row = 0.0
miss_in_a_row = 0.0

print("""
Welcome to the bottle flipping simulator, where you tell us how many bottles you want to be flipped
and we will give you some statistics on how many flips you are likely to get in a row, how many
will be flipped, and stuff like that!  
    """)
name = input("What is your name? ")
name = name.capitalize()
feeling = input(f"How are you doing today {name}? ")
print(f"That's great {name}!")
bottles = input("How many bottles do you want flipped? ")
emailed = input("Would you like the results to be emailed to you (Y/N)? ")
if emailed.lower() == 'y':
    email_address = input("What is your email address? ")
else:
    pass
bottles = float(bottles)


def flips_in_a_row():
    global flip_in_a_row, miss_in_a_row, total_flips
    _range_ = float(random.uniform(0.1, 0.3))
    for i in range(2):
        total_flips += 1
        if total_flips == 0:
            flip_in_a_row = flip_in_a_row + 1
            flip_in_a_row = flip_in_a_row + 1
            if flip_in_a_row < flip_in_a_row:
                flip_in_a_row = flip_in_a_row
                flip_in_a_row = 0
            else:
                flip_in_a_row = 0
        else:
            miss_in_a_row = miss_in_a_row + 1
            miss_in_a_row = miss_in_a_row + 1
            if miss_in_a_row < miss_in_a_row:
                miss_in_a_row = miss_in_a_row
                miss_in_a_row = 0
            else:
                miss_in_a_row = 0


def bottle_flip_analytics():
    try:
        t1 = time.time()
        total_bottles_flipped = bottles * random.uniform(0.1, 0.3)
        total_bottles_missed = bottles - total_bottles_flipped
        percent_flipped = (100/bottles) * total_bottles_flipped
        percent_missed = (100/bottles) * total_bottles_missed
        flipped_in_a_row = total_bottles_flipped / (total_bottles_flipped / 1/2)
        if total_bottles_missed > total_bottles_flipped:
            difference = total_bottles_missed - total_bottles_flipped
        if total_bottles_flipped > total_bottles_missed:
            difference = total_bottles_flipped - total_bottles_missed
        time.sleep(0.7)
        t2 = time.time()
        time_taken = t2 - t1

        print(""
              
              "")
        print(f"Flipped bottles {bottles} times.")
        print(f"Total time taken: {time_taken}s")
        print(f"Bottles were flipped successfully {percent_flipped.__round__()}% of the time.")
        print(f"Bottles were missed {percent_missed.__round__()}% of the time")
        print(f"The difference between missed and flipped: {difference.__round__()}.")
        print(f"The longest bottle flips in a row was {flipped_in_a_row}.")

        email = EmailMessage()
        email['from'] = '<enter your email>'
        email['to'] = email_address
        email['subject'] = 'Bottle Flip Simulator'

        email.set_content(f"""
Hello {name}!
    
These are the statistics from the bottle flipping simulator:
Flipped bottles {bottles} times.
Total time taken: {time_taken}s."
Bottles were flipped successfully {percent_flipped.__round__()}% of the time.
The difference between missed and flipped: {difference.__round__()}.
The longest bottle flips in a row was {flipped_in_a_row}.
    
Thank you for using bottle flip simulator,
Henry
    
        """)
    except NameError as err:
        print(" ")

    with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('<enter your email >', '<enter your password>')
        smtp.send_message(email)
        print('Email sent!')


flips_in_a_row()
bottle_flip_analytics()
