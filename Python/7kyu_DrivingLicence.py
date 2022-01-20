""" 
    Driving Licence

    Your task is to code a UK driving license number using an Array of data. 

    The Array will look like:
    data = ["John","James","Smith","01-Jan-2000","M"]

    Where the elements are as follows:
    0 = Forename
    1 = Middle Name (if any)
    2 = Surname
    3 = Date of Birth (In the format Day Month Year, this could include the full Month name or just shorthand ie September or Sep)
    4 = M-Male or F-Female

    Rules:
    1–5: The first five characters of the surname (padded with 9s if less than 5 characters)
    6: The decade digit from the year of birth (e.g. for 1987 it would be 8)
    7–8: The month of birth (7th character incremented by 5 if driver is female i.e. 51–62 instead of 01–12)
    9–10: The date within the month of birth
    11: The year digit from the year of birth (e.g. for 1987 it would be 7)
    12–13: The first two initials of the first name and middle name, padded with a 9 if no middle name
    14: Arbitrary digit – usually 9, but decremented to differentiate drivers with the first 13 characters in common. We will always use 9
    15–16: Two computer check digits. We will always use "AA"  """

def driver(data):
    
    licence = ''
    months = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06', 'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}
    
    if len(data[1]) > 0:
        data = {
        'name': data[0].upper(),
        'middle_name': data[1].upper(),
        'surname': data[2].upper(),
        'date_birth': data[3].upper(),
        'genre': data[4].upper()}
    
    else:
        data = {
        'name': data[0].upper(),
        'middle_name': '9',
        'surname': data[2].upper(),
        'date_birth': data[3].upper(),
        'genre': data[4].upper()}


    if len(data['surname']) >= 5:     #1-5 digit
        licence = (data['surname'][0:5])
    else:
        licence = (data['surname'])
        while(len(licence)) != 5:
            licence += '9'

    licence += (data['date_birth'][-2]) #6 - decade digit


    for mes, num in months.items():  #7-8 - month digit
        if data['genre'] == "M":
            if mes in data['date_birth']:
                licence += num
        if data['genre'] == "F":
            if mes in data['date_birth']:
                licence += str(int(num) + 50)

    licence += data['date_birth'][0:2] # 9-10 day of birth 
    licence += data['date_birth'][-1]  #11 the year digit of birth 
    licence += data['name'][0] + data['middle_name'][0]  #12-13 initials first and middle name
    licence += '9' + 'AA' #14 - 16 digit 

  
    return licence


