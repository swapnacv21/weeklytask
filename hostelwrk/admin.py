hostel=[]
hostellers=[]
workers=[]
def add_rooms():
    room_number=input("Enter room number : ")
    f1=0
    for i in hostel:                     
        if i['room_number']==room_number:
            f1=1
            print("room number already exists")
    if f1==0:
        room_floor=input("Enter room floor :")
        room_type=input("Enter room type :")
        room_members=int(input("Enter number of persons for this room : "))
        room_rent=int(input("enter rent : "))
        hostel.append({'room_number':room_number,'room_floor':room_floor,'room_type':room_type,'room_members':room_members,'room_rent':room_rent})
        

def view_room():
    print('{:<12}{:<12}{:<12}{:<12}{:<12}'.format('room_number','room_floor','room_type','room_members','room_rent'))
    print('-'*70)
    for i in hostel:
        print('{:<12}{:<12}{:<12}{:<12}{:<12}'.format(i['room_number'],i['room_floor'],i['room_type'],i['room_members'],i['room_rent']))


def update_room():
    r_no=input("enter room number : ")
    f=0
    for i in hostel:
        if i['room_number']==r_no:
            f=1
            new_type=input("Enter New type : ")
            new_persons=input("Enter New no of persons in room : ")
            new_rent=int(input("Enter New rent : "))
            i['room_type']=new_type
            i['room_person']=new_persons
            i['room_rent']=new_rent
    if f==0:
        print("invalid room number")

def delete_room():
    r_no=input("Enter room number : ")
    f=0
    for i in hostel:
        if i['room_number']==r_no:
            hostel.remove(i)
            f=1
    if f==0:
        print("invalid room number")
        

def add_hosteller():
    id=input("Enter hosteller id : ")
    f1=0
    for i in hostellers:
        if i['id']==id:
            f1=1
            print("id exists")
    if f1==0:
        name=input("Enter name of hosteller : ")
        age=int(input("Enter age : "))
        address=input("Enter address : ")
        phone=int(input("Enter phone number : "))
        gaurdian_name=input("Enter name of guardian : ")
        gaurdian_phone=int(input("Enter phone number of guardian : "))
        room_no=int(input("Enter room number : "))
        floor=int(input("Enter room floor : "))
        rent=int(input("Enter rent : "))
        join_date=(input("Enter joined date : "))
        hostellers.append({'id':id,'name':name,'age':age,'address':address,'phone':phone,'gaurdian_name':gaurdian_name,'gaurdian_phone':gaurdian_phone,'room_no':room_no,'floor':floor,'rent':rent,'join_date':join_date})
   
def view_hosteller():
    print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('id','name','age','address','phone','gaurdian_name','gaurdian_phone','room_no','floor','rent','join_date'))
    print('-'*163)
    for i in hostellers:
        print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(i['id'],i['name'],i['age'],i['address'],i['phone'],i['gaurdian_name'],i['gaurdian_phone'],i['room_no'],i['floor'],i['rent'],i['join_date']))

def update_hosteller():
    id=input("enter id : ")
    f=0
    for i in hostellers:
        if i['id']==id:
            f=1
            new_name=input("enter new name : ")
            new_age=int(input("Enter new age : "))
            new_address=input("Enter new address : ")
            new_phone=int(input("Enter new phone number :"))
            new_gphone=int(input("Enter guardian phone number : "))
            new_roomno=int(input("Enter new room number : "))
            new_floor=input("Enter new floor : ")
            new_rent=int(input("Enter new rent : "))
            i['name']=new_name
            i['age']=new_age
            i['address']=new_address
            i['phone']=new_phone
            i['gaurdian_phone']=new_gphone
            i['room_no']=new_roomno
            i['floor']=new_floor
            i['rent']=new_rent
            print("updated")
    if f==0:
        print("Invalid id")

def remove_hosteller():
    id=input("Enter id : ")
    f=0
    for i in hostellers:
        if i['id']==id:
            f=1
            hostellers.remove(i)
            print("removed")
    if f==0:
        print("Invalid  id")

def add_cook():
    cook_id=int(input("Enter id of cook : "))
    cook_name=input("Enter name of cook : ")
    cook_place=input("Enter place : ")
    cook_contact=int(input("Enter contact number : "))
    workers.append({'cook_id':cook_id,'cook_name':cook_name,'cook_place':cook_place,'cook_contact':cook_contact})
    print("cook added")

def view_cook():
    print('{:<12}{:<12}{:<12}{:<12}'.format('cook_id','cook_name','cook_place','cook_contact'))
    print('-'*70)
    for i in workers:
        print('{:<12}{:<12}{:<12}{:<12}'.format(i['cook_id'],i['cook_name'],i['cook_place'],i['cook_contact']))

def update_cook():
    id=int(input("enter cook id : "))
    f=0
    for i in workers:
        if i['cook_id']==id:
            f=1
            new_cname=input("Enter new name : ")
            new_contact=int(input("Enter new phone number : "))
            i['cook_name']=new_cname
            i['cook_contact']=new_contact
            print("updated")
    if f==0:
        print("invalid id")

def remove_cook():
    id=int(input("Enter cook id : "))
    f=0
    for i in workers:
        if i['cook_id']==id:
            f=1
            workers.remove(i)
            print("removed")
    if f==0:
        print("invalid id")


def add_cleaner():
    cleaner_id=input("Enter id : ")
    cleaner_name=input("Enter name of cleaner")
    cleaner_place=input("Enter place of cleaner : ")
    cleaner_phone=int(input("Enter contact : "))
    workers.append({'cleaner_id':cleaner_id,'cleaner_name':cleaner_name,'cleaner_place':cleaner_place,'cleaner_phone':cleaner_phone})
    print("cleaner added")

def view_cleaner():
    print('{:<15}{:<15}{:<15}{:<15}'.format('cleaner_id','cleaner_name','cleaner_place','cleaner_phone'))
    print('-'*70)
    for i in workers:
        print('{:<15}{:<15}{:<15}{:<15}'.format(i['cleaner_id'],i['cleaner_name'],i['cleaner_place'],i['cleaner_phone']))

def update_cleaner():
    id=input("enter cleaner id : ")
    f=0
    for i in workers:
        if i['cleaner_id']==id:
            f=1
            new_clname=input("Enter new name : ")
            new_clcontact=int(input("Enter new phone number : "))
            i['cleaner_name']=new_clname
            i['cleaner_phone']=new_clcontact
            print("updated")


def remove_cleaner():
     id=input("Enter cleaner id : ")
     f=0
     for i in workers:
        if i['cleaner_id']==id:
            f=1
            workers.remove(i)
            print("removed")
