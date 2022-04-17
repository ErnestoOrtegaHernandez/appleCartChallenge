import json
import datetime
from dateutil.relativedelta import relativedelta
import argparse


#comment out the following lines to run unit tests
parser = argparse.ArgumentParser(description='Finds the people connected to a person')
parser.add_argument('person_id', type=int, help='The id of the person')
args = parser.parse_args()


#loads the entries from the json file into memory
def load_file(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

#check if the dates overlap by at least six months
def check_company_dates(p_exp, op_exp):
    p_start_date = datetime.datetime.strptime(p_exp["start"], "%Y-%m-%d")
    p_end_date = datetime.datetime.strptime(p_exp["end"], "%Y-%m-%d") if p_exp["end"] else datetime.datetime.now()
    op_start_date = datetime.datetime.strptime(op_exp["start"], "%Y-%m-%d")
    op_end_date = datetime.datetime.strptime(op_exp["end"], "%Y-%m-%d") if op_exp["end"] else datetime.datetime.now()
    if p_start_date <= op_start_date:
        sixthMonth = op_start_date + relativedelta(months=6)
        if(sixthMonth <= op_end_date and sixthMonth <= p_end_date):
            return True
    if op_start_date <= p_start_date:
        sixthMonth = p_start_date + relativedelta(months=6)
        if(sixthMonth <= p_end_date and sixthMonth <= op_end_date):
            return True
    return False
#normalize phone number in the format X-XXXXXXXXXX from +XXXXXXXXXXX and (XXX) XXX-XXXX
def normalize_phone(phone):
    if phone[0] == '+':
        normalized_phone = phone[1] + '-' + phone[2:]
    if phone[0] == '1':
        if(phone[1] == '-'):
            normalized_phone = phone[0:]
        elif(len(phone) > 10):
            normalized_phone = phone[0] + '-' + phone[1:]
        else:
            normalized_phone = '1-' + phone[0:]
    if phone[0] == '(':
        normalized_phone = '1-' + phone[1:4] + phone[6:9] + phone[10:]
    return normalized_phone

#returns a list of people connected to the given person (person_id)
def get_connected_people(people_file, person_id, contact_file, connection_type):
    connected_company_people = []
    connected_contact_people = []
    connected_people = []
    people = load_file(people_file) if people_file else None
    contacts = load_file(contact_file) if contact_file else None
    connection_type = connection_type.lower()
    for person in people: #iterate through people
        if person["id"] == person_id:
            p_exps = person["experience"] #experiences of the person
            p_phone = person["phone"] #phone number of the person
            if(connection_type == "company" or connection_type == "both"):
                for other_person in people:
                    if other_person["id"] != person_id: 
                        op_exps = other_person["experience"] #experiences of the other person
                        for p_exp in p_exps:
                            for op_exp in op_exps: #iterate through the experiences of the person and the other person
                                if(p_exp["company"] == op_exp["company"]): #check if the company is the same, can have multiple entries of the same company (hired, left, rehired)
                                    if(check_company_dates(p_exp, op_exp)): #check if the dates overlap by at least six months
                                        connected_company_people.append(other_person["id"]) #add the other person to the list of connected people
            if(connection_type == "contact" or connection_type == "both"):
                for contact in contacts: #iterate through the contacts
                    for entry in contact["phone"]: #iterate through the phone numbers of the contact
                        normal_number = normalize_phone(entry["number"])   #normalize the phone number
                        if(p_phone == normal_number): #check if the phone number of the person is the same as the contact
                            connected_contact_people.append(contact["owner_id"]) #add the contact owner to the list of connected people
                            break #move on to the next contact
            break #no other person should have the same id as the person
    connected_people = list(set(connected_company_people + connected_contact_people)) #remove duplicates  
    connected_people.sort()            
    return connected_company_people if connection_type == "company" else connected_contact_people if connection_type == "contact" else connected_people

def print_connected_names(person_id): #prints the names of the connected people
    connected_people = get_connected_people('./persons.json', person_id, './contacts.json', "both")
    people = load_file('./persons.json')
    for person in people:
        if person["id"] in connected_people:
            print(person["first"], person["last"], "\n")

#comment out the following line to run unit tests
print_connected_names(args.person_id)
