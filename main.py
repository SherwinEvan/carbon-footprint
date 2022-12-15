# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:20:08 2020

@author: Admin
"""

import math


def emW(x, y):
    elecemm1 = x * y
    elecemm2 = x * y / 1000
    print('Carbon Emissioned:', elecemm1, 'CO2/Wh or', elecemm2, 'CO2/kWh')
    print("******************************")


def emkW(x, y):
    elecemm1 = x * y * 1000
    elecemm2 = x * y
    print('Carbon Emissioned:', elecemm2, 'CO2/kWh or', elecemm1, 'CO2/Wh')
    print("******************************")


def ng(x):
    ef = 117
    ngemm = x * ef
    print('Carbon Emissioned:', ngemm, 'CO2/mmBtu (CO2 emitted per million British thermal units (Btu))')
    print("******************************")


def pet():
    lit = float(input('Please enter the amount of petrol used in Litre: '))
    ef = 2.95
    pem = lit * ef
    print('Carbon Emissioned:', pem, 'kg CO2-e/unit')
    print("******************************")


def die():
    lit = float(input('Please enter the amount of diesel used in Litre: '))
    ef = 161.3
    dem = lit * ef
    print('Carbon Emissioned:', dem, 'CO2/mmbtu')
    print("******************************")


def gas():
    lit = float(input('Please enter the amount of Gasoline used in Litre: '))
    ef = 157.2
    gem = lit * ef
    print('Carbon Emissioned:', gem, 'CO2/mmbtu')
    print("******************************")


def hyd():
    kg = float(input('Please enter the amount of Hydrogen used in Kilograms: '))
    ef = math.pi / 2
    hem = kg * ef
    print('Carbon Emissioned:', hem, 'CO2/kg')
    print("******************************")


# main
base = 'True'
while base == 'True':
    print('''\n1) Instant calculator
2) Footprint database 
3) Exit''')
    chk = input('Which mode do you want to use? (Please enter the index number next to the mode): ')
    chk.lower()
    if chk == '1' or chk == 'one':
        print('\nWhich of the following do you want to calculate for?')
        print('''1) Electricity
2) Natural gas
3) Road Vehicle (fuel) ''')
        inst = input('Which one do you want to calcuate for? (Please enter the index number next to the mode): ')
        inst.lower()
        if inst == '1' or inst == 'one':
            print('You have chosen Electricity')
            means = input('''Please enter the source of electricity from the following:
(WindMill, Coal, Hydro(Dams), Geothermal): ''')
            metric = input('''Do you want to enter in <unit> or in Kilo<unit>? 
(Please enter "unit" or "Kilo" ): ''')
            means.lower()
            metric.lower()
            if metric == 'unit':
                if means == 'windmill':
                    elec = float(input('Enter the value of power used: '))
                    ef = 2
                    emW(elec, ef)
                elif means == 'coal':
                    elec = float(input('Enter the amount of coal used: '))
                    ef = 227.4
                    emW(elec, ef)
                elif means == 'hydro' or means == 'dams':
                    elec = float(input('Enter the volume of water passed: '))
                    ef = 18.5
                    emW(elec, ef)
                elif means == 'geothermal' or means == 'geo':
                    elec = float(input('Enter the quantity of liquid heated: '))
                    ef = 122
                    emW(elec, ef)
                else:
                    print('Invalid input!')
            elif metric == 'kilo':
                if means == 'windmill':
                    elec = float(input('Enter the value of power used: '))
                    ef = 2
                    emkW(elec, ef)
                elif means == 'coal':
                    elec = float(input('Enter the amount of coal used: '))
                    ef = 227.4
                    emkW(elec, ef)
                elif means == 'hydro' or means == 'dams':
                    elec = float(input('Enter the volume of water passed:'))
                    ef = 18.5
                    emkW(elec, ef)
                elif means == 'geothermal' or means == 'geo':
                    elec = float(input('Enter the quantity of liquid heated: '))
                    ef = 122
                    emkW(elec, ef)
                else:
                    print('Invalid input!')
            else:
                print('Enter a vaild metric.')
        elif inst == '2' or inst == 'two':
            print('\nYou have chosen Natural Gas')
            liq = float(input('Please enter the amount of natural gas burnt in Litre: '))
            ng(liq)
        elif inst == '3' or inst == 'three':
            print('You have chosen Road Vehicle (fuel)')
            print('Which of the following fuel type do you want to calculate for?')
            print('''1) Petrol
2) Diesel
3) Gasoline (without ethanol)
4) Hydrogen ''')
            fuel = input('Please enter the index number next to the fuel you want to calculate for: ')
            if fuel == '1' or fuel == 'one':
                pet()
            elif fuel == '2' or fuel == 'two':
                die()
            elif fuel == '3' or fuel == 'three':
                gas()
            elif fuel == '4' or fuel == 'four':
                hyd()
            else:
                print('Invalid input!')
    if chk == '2' or chk == 'two':
        print('\nNow accessing avaliable Database...')
        import mysql.connector as sqltor

        mycon = sqltor.connect(host='localhost', user='root', password='0000', database='database1')
        cursor = mycon.cursor()
        if mycon.is_connected():
            print('Successfully conected to Database!')
        else:
            print(''''Failed to connect to database!
Please try again''')
        print('\nWhich of the following do you want to do?')
        print('''1) Create New Table
2) Access current table''')
        inst = input('Which one do you want to do? (Please enter the index number next to the mode): ')
        inst.lower()
        if inst == '1' or inst == 'one':
            print('\nYou have chosen to create new table')
            table = input("Enter new table's name: ")
            columns = []
            while True:
                cname = input("Enter column name ('No' to quit): ")
                if cname == 'No':
                    break
                else:
                    const = input("Enter its constraints seperated by ' ': ")
                    tab = cname + ' ' + const
                    columns.append(tab)
            print('Creating query...')
            qu1 = '('
            for i in range(0, len(columns)):
                if i == len(columns) - 1:
                    qu1 = qu1 + columns[i]
                else:
                    qu1 = qu1 + columns[i] + ','
            qu1 = qu1 + ')'
            qu = 'create table {0} {1};'.format(table, qu1)
            print('Executing the following query:\n', qu)
            try:
                cursor.execute(qu)
                print('Table Successfully Created!')
            except 'ProgrammingError':
                print('There is an error in your input! Please try again')
            val = input('Do you want to input values in your table? (y/n): ')
            val.lower()
            if val == 'n':
                pass
            else:
                while True:
                    print('This is the columns list:', columns)
                    val1 = input("Enter respective values seperated by ',': ")
                    val1 = '(' + val1 + ')'
                    qu2 = 'insert into {0} values {1};'.format(table, val1)
                    print('Executing the following query:\n', qu2)
                    try:
                        cursor.execute(qu2)
                        mycon.commit()
                        print('Successfully inserted values!')
                    except 'ProgrammingError':
                        print('There is an error in your input! Please try again')
                    cont1 = input('Do you want to input values in your table again? (y/n): ')
                    cont1.lower()
                    if cont1 == 'y':
                        continue
                    else:
                        break
            view = input('Do you want to view your table? (y/n): ')
            view.lower()
            if view == 'y':
                view1 = input('''Do you want to view:
1) The entire table
2) Table with select parameters
(Please enter the index number next to the mode):''')
                view1.lower()
                if view1 == 'one' or '1':
                    qn3 = 'select * from {0};'.format(table)
                    print('Executing the following query:\n', qn3)
                    cursor.execute('select * from {0};'.format(table))
                    data = cursor.fetchall()
                    for row in data:
                        print(row)
                else:
                    conts = input("Enter your parameter seperated by ' ': ")
                    qu4 = 'select * from {0} where {1};'.format(table, conts)
                    print('Executing the following query:\n', qu4)
                    try:
                        cursor.execute(qu4)
                        data = cursor.fetchall()
                        for row in data:
                            print(row)
                    except 'ProgrammingError':
                        print('There is an error in your input! Please try again')
            else:
                pass
            mod = input('Do you want to change values in your table? (y/n): ')
            mod.lower()
            if mod == 'y':
                para = input('Enter Parameter(s) where value has to be updated: ')
                newv = input('Enter the updated constrain: ')
                qu5 = 'update {0} set {1} where {2}'.format(table, newv, para)
                try:
                    cursor.execute(qu5)
                    mycon.commit()
                    print('Value updated')
                except 'ProgrammingError':
                    print('There is an error in your input! Please try again')
            else:
                pass
            rem = input('Do you want to remove values your table? (y/n): ')
            rem.lower()
            if rem == 'y':
                remp = input('Enter the parameter to delete the required: ')
                qu6 = 'delete from {0} where {1};'.format(table, remp)
                try:
                    print('Executing the following query:\n', qu6)
                    cursor.execute(qu6)
                    mycon.commit()
                    print('Record Deleted')
                except 'ProgrammingError':
                    print('There is an error in your parameter! Please try again')
            delt = input('Do you want to delete your table? (y/n): ')
            delt.lower()
            if delt == 'y':
                sure = input('Are you sure that you want delete the table? (THIS ACTION CANNOT BE UNDONE!) (y/n): ')
                sure.lower()
                if sure == 'y':
                    qu7 = 'drop table {0};'.format(table)
                    print('Executing the following query:\n', qu7)
                    try:
                        cursor.execute(qu7)
                        print('Table Deleted')
                    except 'ProgrammingError':
                        print('ERROR! Please try again')
                else:
                    pass
            else:
                continue
        elif inst == '2' or inst == 'two':
            print('\nYou have chosen to access available tables')
            print('Showing available tables: ')
            cursor.execute('show tables;')
            data = cursor.fetchall()
            for row in data:
                print(row)
            data = list(data)
            table = input('Please enter the table name: ')
            if table in data:
                print('Connecting to table...')
            print('This is the table:')
            cursor.execute('select * from {0};'.format(table))
            data = cursor.fetchall()
            for row in data:
                print(row)
            base = input('''Do you want to:
1) Edit
2) Calculate (Recomened for structured table)
(Please enter the index number next to the mode): ''')
            base.lower()
            if base == '1' or 'one':
                val = input('Do you want to input values in your table? (y/n): ')
                val.lower()
                if val == 'n':
                    pass
                else:
                    while True:
                        val1 = input("Enter respective values seperated by ',': ")
                        val1 = '(' + val1 + ')'
                        qu2 = 'insert into {0} values {1};'.format(table, val1)
                        print('Executing the following query:\n', qu2)
                        try:
                            cursor.execute(qu2)
                            mycon.commit()
                            print('Successfully inserted values!')
                        except 'ProgrammingError':
                            print('There is an error in your input! Please try again')
                        cont1 = input('Do you want to input values in your table again? (y/n): ')
                        cont1.lower()
                        if cont1 == 'y':
                            continue
                        else:
                            break
                view = input('Do you want to view your table? (y/n): ')
                view.lower()
                if view == 'y':
                    view1 = input('''Do you want to view:
    1) The entire table
    2) Table with select parameters
    (Please enter the index number next to the mode):''')
                    view1.lower()
                    if view1 == 'one' or '1':
                        qn3 = 'select * from {0};'.format(table)
                        print('Executing the following query:\n', qn3)
                        cursor.execute('select * from {0};'.format(table))
                        data = cursor.fetchall()
                        for row in data:
                            print(row)
                    else:
                        conts = input("Enter your parameter seperated by ' ': ")
                        qu4 = 'select * from {0} where {1};'.format(table, conts)
                        print('Executing the following query:\n', qu4)
                        try:
                            cursor.execute(qu4)
                            data = cursor.fetchall()
                            for row in data:
                                print(row)
                        except 'ProgrammingError':
                            print('There is an error in your input! Please try again')
                else:
                    pass
                mod = input('Do you want to change values in your table? (y/n): ')
                mod.lower()
                if mod == 'y':
                    para = input('Enter Parameter(s) where value has to be updated: ')
                    newv = input('Enter the updated constrain: ')
                    qu5 = 'update {0} set {1} where {2}'.format(table, newv, para)
                    print('Executing the following query:\n', qu5)
                    try:
                        cursor.execute(qu5)
                        mycon.commit()
                        print('Value updated')
                    except 'ProgrammingError':
                        print('There is an error in your input! Please try again')
                else:
                    pass
                rem = input('Do you want to remove values your table? (y/n): ')
                rem.lower()
                if rem == 'y':
                    remp = input('Enter the parameter to delete the required: ')
                    qu6 = 'delete from {0} where {1};'.format(table, remp)
                    try:
                        print('Executing the following query:\n', qu6)
                        cursor.execute(qu6)
                        mycon.commit()
                        print('Record Deleted')
                    except 'ProgrammingError':
                        print('There is an error in your parameter! Please try again')
                delt = input('Do you want to delete your table? (y/n): ')
                delt.lower()
                if delt == 'y':
                    sure = input('Are you sure that you want delete the table? (THIS ACTION CANNOT BE UNDONE!) (y/n): ')
                    sure.lower()
                    if sure == 'y':
                        qu7 = 'drop table {0};'.format(table)
                        print('Executing the following query:\n', qu7)
                        try:
                            cursor.execute(qu7)
                            print('Table Deleted')
                        except 'ProgrammingError':
                            print('ERROR! Please try again')
                    else:
                        pass
                else:
                    pass
            elif base == '2' or base == 'two':
                val = input('Do you want to Calculate Average emission for a given User (y/n): ')
                val.lower()
                if val == 'n':
                    pass
                else:
                    usr = int(input('Enter the user ID (Primary key): '))
                    qu6 = 'select emission from {0} where userid={1};'.format(table, usr)
                    print('Executing the following query:\n', qu6)
                    sum1: int = 0
                    tim = 0
                    try:
                        cursor.execute(qu6)
                        data = cursor.fetchall()
                        for row in data:
                            row = float(row)
                            sum1 += row
                            tim += 1
                        avg = sum1 / tim
                        print(usr, "'s average CO2 emission is:", avg, 'CO2')
                    except 'ProgrammingError':
                        print('There is an error in your input! Please try again')
                val2 = input('Do you want to Calculate total emission (y/n): ')
                val2.lower()
                if val2 == 'n':
                    pass
                else:
                    qu7 = 'select emission from {0};'.format(table)
                    print('Executing the following query:\n', qu7)
                    cursor.execute(qu7)
                    data = cursor.fetchall()
                    sum2 = 0
                    for row in data:
                        row = float(row)
                        sum1 += row
                    print("Total CO2 emission is:", sum2, 'CO2')
                usrlst = input('Do you want to see the list of users (y/n): ')
                usrlst.lower()
                if usrlst == 'n':
                    pass
                else:
                    qu7 = 'select user from {0};'.format(table)
                    print('Executing the following query:\n', qu7)
                    cursor.execute(qu7)
                    data = cursor.fetchall()
                    for row in data:
                        print(row)
                ussr = input("Do you want to see a user's data (y/n): ")
                ussr.lower()
                ussr.lower()
                if ussr == 'n':
                    pass
                else:
                    id2 = int(input('Please enter the user ID: '))
                    qu8 = 'select * from {0} where {1};'.format(table, id2)
                    print('Executing the following query:\n', qu8)
                    cursor.execute(qu8)
                    data = cursor.fetchall()
                    print(data)
                eusrlst = input('Do you want to see the list of users who emit more than average emission (y/n): ')
                eusrlst.lower()
                if eusrlst == 'n':
                    pass
                else:
                    qu9 = 'select user from {0} where emission>5.3*907.13;'.format(table)
                    print('Executing the following query:\n', qu9)
                    cursor.execute(qu9)
                    data = cursor.fetchall()
                    print(data)
                e1usrlst = input('Do you want to see the list of users who emit less than average emission (y/n): ')
                eusrlst.lower()
                if e1usrlst == 'n':
                    pass
                else:
                    qu10 = 'select user from {0} where emission<5.3*907.13;'.format(table)
                    print('Executing the following query:\n', qu10)
                    cursor.execute(qu10)
                    data = cursor.fetchall()
                    print(data)
                tax = input('Do you want to increase the tax on users who emit CO2, more than allowed  (y/n): ')
                tax.lower()
                if tax == 'n':
                    pass
                else:
                    taxm = float(input('Enter the increase in tax (input in percentage): '))
                    qu11 = 'update {0} set tax=tax+(tax*{1}/100) where emission<6.5*907.13;'.format(table, taxm)
                    print('Executing the following query:\n', qu11)
                    cursor.execute(qu11)
                    mycon.commit()
                    print('Tax Increased')
                blklst = input('Do you want to black list users with extremely high CO2 usage (y/n): ')
                blklst.lower()
                if blklst == 'n':
                    pass
                else:
                    qu12 = 'select user from {0} where emission>7.5*907.13;'.format(table)
                    print('Executing the following query:\n', qu12)
                    cursor.execute(qu12)
                    data = cursor.fetchall()
                    blacklist = []
                    for row in data:
                        blacklist.append(row)
                        print(row)
                gtax = input('Do you want to decrease the tax on users who emit less CO2 (y/n): ')
                gtax.lower()
                if gtax == 'n':
                    pass
                else:
                    tax1 = float(input('Enter the decrease in tax (input in percentage): '))
                    qu13 = 'update {0} set tax=tax+(tax*{1}/100) where tax>5.0*907.13;'.format(table, tax1)
                    print('Executing the following query:\n', qu13)
                    cursor.execute(qu13)
                    mycon.commit()
                    print('Tax decreased')
                hist = input('Do you want to clear all the CO2 emission history? (y/n): ')
                hist.lower()
                if rem == 'y':
                    conf = input(
                        'Are you sure that you want delete the history? (THIS ACTION CANNOT BE UNDONE!) (y/n): ')
                    conf.lower()
                    if conf == 'y':
                        qu14 = 'update {0} set emission=NULL;'.format(table)
                        print('Executing the following query:\n', qu14)
                        cursor.execute(qu14)
                        mycon.commit()
                        print('Emission History reset successfully')
                    else:
                        pass
    elif chk == '3' or chk == 'three':
        print('Thank You!')
        break
    else:
        print('ERROR! invalid input! Please try again')
