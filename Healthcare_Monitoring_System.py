# Healthcare Monitoring & Alert System

"""
--------------------------------------
 Healthcare Monitoring & Alert System
--------------------------------------
This program checks common health indicators (vitals + lifestyle habits)
and gives alerts if values are outside the safe range.

Features:
- Handles multiple health parameters (Blood Pressure, Heart Rate, Sugar, BMI, Oxygen, Sleep, Water Intake)
- Error handling for wrong / invalid inputs
- Works with both sample data (predefined) and user inputs
- Outputs alerts for abnormal readings
"""

from datetime import datetime                                          # We imported datetime just in case because we want to add time/date in reports later


#--------------------------------------------------------------------------------------------
#                       CONFIGURATION: Normal Ranges
#--------------------------------------------------------------------------------------------
'''
 # we made a dictionary (basically key-value pairs) to keep all the normal health ranges in one place
 # reason is to make it easier to update or reuse later instead of writing conditions again and again
'''

HEALTH_RANGES = {                                                      
    "blood_pressure": (("Systolic", 90, 120), ("Diastolic", 60, 80)),  # label, min, max
    "heart_rate": (60, 100),                                           # normal resting heart rate, min and max values
    "blood_sugar": (70, 140),                                          # sugar range after eating (mg/dL), kept it simple
    "bmi": (18.5, 24.9),                                               # healthy bmi range so we can quickly compare
    "oxygen": (95, 100),                                               # SpO2 percentage, below 95 usually not good
    "sleep_hours": (7, 9),                                             # minimum & maximum sleep hours required daily
    "water_liters": (2, 4),                                            # daily water intake in liters
}


#--------------------------------------------------------------------------------
#                      ERROR HANDLING INPUT FUNCTION
#--------------------------------------------------------------------------------
def safe_input(prompt, datatype = float, min_val = None, max_val = None):
    '''
    # we made this function because sometimes users type wrong values (like text instead of numbers)
    # so this function will keep asking again and again until we get a proper valid input
    '''
    
    while True:                                                         # we keep looping until the user gives correct input
        try:
            val = datatype(input(prompt))                               # we convert the input into whatever datatype we want (int/float)
            if min_val is not None and val < min_val:                   # here we are checking if the value is less than the minimum allowed
                print(f" Value cannot be less than {min_val}. Try again.")
                continue                                                # So that it can go back and ask again
            if max_val is not None and val > max_val:                   # same check but for maximum allowed value
                print(f" Value cannot be greater than {max_val}. Try again.")
                continue                                                # if everything is fine, we just return the value
            return val
        except ValueError:                                              # if the user enters something which cannot be converted into number then we show error
            print(" Invalid input! Please enter a number.") 


#--------------------------------------------------------------------------------
#                      HEALTH CHECK FUNCTION
#--------------------------------------------------------------------------------
def check_health(data):
    '''
    # this function is basically checking all the health values one by one
    # we compare the user's data with normal healthy ranges
    # if something is not okay, we add an alert message to the list
    '''

    alerts = []                                                          # we are keeping an empty list here to store all the warning messages

    # Blood Pressure 
    sys = data.get("systolic")                                           # we take systolic value from the data
    dia = data.get("diastolic")                                          # we take diastolic value from the data
    if not (90 <= sys <= 120 and 60 <= dia <= 80):                       # we check if both are inside normal range
        alerts.append(f"Blood Pressure Abnormal: {sys}/{dia} mmHg")

    # Heart Rate
    hr = data.get("heart_rate")
    if not (60 <= hr <= 100):                                            # normal range is 60–100 bpm
        alerts.append(f"Heart Rate Abnormal: {hr} bpm")

    # Blood Sugar 
    sugar = data.get("blood_sugar")
    if not (70 <= sugar <= 140):                                         # if sugar is outside 70–140
        alerts.append(f"Blood Sugar Abnormal: {sugar} mg/dL")

    # BMI
    bmi = data.get("bmi")
    if not (18.5 <= bmi <= 24.9):                                        # healthy BMI should be between 18.5 and 24.9
        alerts.append(f"BMI Abnormal: {bmi:.1f}")

    # Oxygen
    oxy = data.get("oxygen")
    if not (95 <= oxy <= 100):                                           # oxygen should not drop below 95%
        alerts.append(f"Oxygen Level Low: {oxy}%")

    # Sleep 
    sleep = data.get("sleep_hours")
    if not (7 <= sleep <= 9):                                            # we should ideally sleep 7–9 hrs
        alerts.append(f"Sleep Hours Abnormal: {sleep} hrs")

    # Water Intake 
    water = data.get("water_liters")
    if not (2 <= water <= 4):                                            # 2–4 liters is considered normal
        alerts.append(f"Water Intake Abnormal: {water} L")

    return alerts                                                        # after checking everything, we return all the alerts we collected
 

#----------------------------------------------------------
#                 SAMPLE DATA (for demo)
#----------------------------------------------------------
'''
# here we are keeping some sample values to test our program quickly
# so even if the user doesn’t give any input, we can still run and see how it works
# we purposely made most of these abnormal so that we can check if our alerts are firing properly
'''

SAMPLE_DATA = {
    "systolic": 135,                                                     # systolic BP is higher than normal (should be 90–120)
    "diastolic": 95,                                                     # diastolic BP is also high (should be 60–80)
    "heart_rate": 110,                                                   # above the safe range of 60–100
    "blood_sugar": 180,                                                  # high sugar, normal range is 70–140
    "bmi": 27.5,                                                         # this is overweight, healthy BMI is 18.5–24.9
    "oxygen": 92,                                                        # oxygen is below 95, so it’s not okay
    "sleep_hours": 5,                                                    # less sleep than recommended 7–9 hrs
    "water_liters": 1.5,                                                 # less water than required 2–4 liters
}


##-----------------------------------------------------------------
#                        MAIN PROGRAM
#------------------------------------------------------------------
'''
# this is the entry point of our program
# so whenever we run this file directly, everything inside this block will execute
# (but if we import this file somewhere else, this part won't run - which makes our code reusable)
'''

if __name__ == "__main__":
    print("\n🏥 Healthcare Monitoring & Alert System \n")
    print("Using sample data for demo:")                                  # first we are doing a demo run with the SAMPLE_DATA we defined earlier
    for k, v in SAMPLE_DATA.items():                                      # this helps us quickly check if our alerts are working fine without entering data again and again
        print(f" - {k}: {v}")                                             # printing each parameter and its value

    alerts = check_health(SAMPLE_DATA)                                    # now we check health for the sample data
    print("\n🔍 Alerts from sample data:")                               # showing results of the demo run
    if alerts:
        for a in alerts:
            print(" ", a)                                                 # print each alert if abnormal
    else:
        print(" ✅ All vitals within normal range!")                      # no alerts means everything normal

    print("\n-----------------------------------")
    print("Now enter your own health details 👇")                         # after demo, we ask the user for their own health details
    print("-----------------------------------")


# USER INPUTS (with error handling)

# Here we are asking the user to enter their health details.
# We are using the safe_input() function we created earlier so that if the user types
# something wrong (like letters instead of numbers, or values out of range), the program
# won’t crash and will ask again. This makes the program more reliable.

    user_data = {
        "systolic": safe_input("Enter Systolic BP (90 - 200): ", int, 50, 250),
        "diastolic": safe_input("Enter Diastolic BP (60 - 120): ", int, 30, 150),
        "heart_rate": safe_input("Enter Heart Rate (40 - 200): ", int, 30, 250),
        "blood_sugar": safe_input("Enter Blood Sugar (50 - 300): ", float, 40, 400),
        "bmi": safe_input("Enter BMI (10 - 40): ", float, 10, 50),
        "oxygen": safe_input("Enter Oxygen % (70 - 100): ", float, 70, 100),
        "sleep_hours": safe_input("Enter Sleep Hours (0 - 24): ", float, 0, 24),
        "water_liters": safe_input("Enter Water Intake in Liters (0 - 10): ", float, 0, 10),
    }


# Final Report

# now we are showing the summary of the health data entered by the user
# first we call the check_health() function which will give us any warnings/alerts
# if there are alerts → print them one by one and also give a suggestion
# if no alerts → print a positive message that everything is fine
# at the end just print a small closing line for neatness

    print("\n📝 Final Health Report")
    print("--------------------------")
    user_alerts = check_health(user_data)

    if user_alerts:                                                       # means there are some health issues
        for a in user_alerts:
            print(" ", a)
        print("\n💡 Suggestion: Please consult a doctor / improve lifestyle where needed.")
    else:                                                                 # means everything is normal
        print(" ✅ Congratulations! All your vitals are within the healthy range.")
    print("\nDone ✅ Stay Healthy!\n")

    
