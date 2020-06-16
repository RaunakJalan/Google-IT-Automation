#!/usr/bin/env python3

import re
import operator
import csv

error = {}
per_user = {}
userPat = r"\((.*)\)"
errorPat = r"ERROR (.*) \(.*\)"
infoPat = r"INFO"
with open("syslog.log",'r') as file:
        for i in file.readlines():
                i = i.strip()
                name = str(re.findall(userPat, i)[0])
                if name not in per_user:
                        per_user[name] = {"INFO":0,"ERROR":0}
                if re.search(errorPat,i):
                        err = re.findall(errorPat,i)[0]
                        if err not in error:
                                error[err]=1
                        else:
                                error[err]+=1
                        per_user[name]["ERROR"]+=1
                elif re.search(infoPat,i):
                        per_user[name]["INFO"]+=1


error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
per_user =  sorted(per_user.items(), key=operator.itemgetter(0))

error.insert(0,("Error", "Count"))
per_user.insert(0,("Username", "INFO", "ERROR"))

with open("error_message.csv","w") as file:
        file_write = csv.writer(file)
        for row in error:
                file_write.writerow(list(row))

with open("user_statistics.csv","w") as file:
        file_write = csv.writer(file)
        file_write.writerow(list(per_user[0]))
        for row in per_user[1:]:
                file_write.writerow([row[0],row[1]["INFO"],row[1]["ERROR"]])


