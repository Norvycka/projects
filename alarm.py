import datetime
import time
import os

invalid = True

while (invalid):
    print("set an alarm. EX: 05:55")
    userInput = input(">>")

    alarmTime = [int(n) for n in userInput.split(":")]

    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    elif alarmTime[1] >= 60 or alarmTime[1] < 0:
        invalid = True
    else:
        invalid = False

seconds_hms = [3600, 60, 1]
alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(alarmTime)], alarmTime)])

now = datetime.datetime.now()
currentTimeInSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

secondsUntilAlarm = alarmSeconds - currentTimeInSeconds

if secondsUntilAlarm < 0:
    secondsUntilAlarm += 86400

print("alarm has been set!")
print("The alarm will ring at %s" % datetime.timedelta(seconds=secondsUntilAlarm))

for i in range(0, secondsUntilAlarm):
    time.sleep(1)
    secondsUntilAlarm -= 1
    print(datetime.timedelta(seconds=secondsUntilAlarm))
    
print("Ring Ring mofo, wake up")
os.system('spd-say "wake up bitch!"')
