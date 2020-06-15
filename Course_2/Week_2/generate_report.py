#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
        file = open(csv_file_location)
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        reader = csv.DictReader(file,dialect='empDialect')
        employee_list = []
        for data in reader:
                employee_list.append(data)
        return employee_list

def process_data(employee_list):
        department_list = []
        for data in employee_list:
                department_list.append(data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data

def write_report(dictionary, report_file):
        with open(report_file,"w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k)+':'+str(dictionary[k])+'\n')


employee_list = read_employees('/home/<username>/data/employees.csv')
#print(employee_list)
dictionary = process_data(employee_list)
#print(dictionary)
write_report(dictionary,'/home/<username>/test_report.txt')
