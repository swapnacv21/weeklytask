hostel=[]
hostellers=[]
workers=[]
while True:
    print(
        '''
        1.Room Details
        2.Person Details
        3.Worker's Details
        4.Exit
    '''
    )
    choice=int(input("Enter your choice : "))
    if choice==1:
        while True:
            print(
                '''
                1.Add Rooms
                2.View room details
                3.Update room details
                4.Delete room
                5.Exit
                '''
            )
            sub_choice=int(input("Enter your choice : "))
            if sub_choice==1:
                room_number=int(input("Enter room number : "))
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
            elif sub_choice==2:
                print('{:<12}{:<12}{:<12}{:<12}{:<12}'.format('room_number','room_floor','room_type','room_members','room_rent'))
                print('-'*70)
                for i in hostel:
                    print('{:<12}{:<12}{:<12}{:<12}{:<12}'.format(i['room_number'],i['room_floor'],i['room_type'],i['room_members'],i['room_rent']))
            elif sub_choice==3:
                r_number=int(input("Enter room number : "))
                f=0
                while True:
                    print(
                        '''
                        1.Update room type
                        2.Update room person
                        3.Update room rent
                        4.Exit
                    '''
                    )
                    up_choice=int(input("Enter your choice : "))
                    if up_choice==1:
                        for i in hostel:
                            if i['room_number']==r_number:
                                new_type=(input("Enter new room type : "))
                                i['room_type']=new_type
                                f=1
                                print("updated")
                        if f==0:
                            print("Inavlid room number")
                    elif up_choice==2:
                        for i in hostel:
                            if i['room_number']==r_number:
                                new_persons=(input("Enter number of persons in this room : "))
                                i['room_person']=new_persons
                                f=1
                                print("updated")
                        if f==0:
                            print("Inavlid id")
                    elif up_choice==3:
                        for i in hostel:
                            if i['room_number']==r_number:
                                new_rent=(input("Enter new rent : "))
                                i['room_rent']=new_rent
                                f=1
                                print("updated")
                        if f==0:
                            print("Inavlid id")
                    elif up_choice==4:
                        break
            elif sub_choice==4:
                r_number=int(input("Enter room number : "))
                f=0
                for i in hostel:
                    if i['room_number']==r_number:
                        hostel.remove(i)
                        f=1
                if f==0:
                    print("invalid id")
            elif sub_choice==5:
                break
    elif choice==2:
        while True:
            print(
                '''
                1.Add hosteller
                2.View hosteller's deatils
                3.Update details
                4.Delete hosteller
                5.Exit
            '''
            )
            h_choice=int(input("Enter your choice : "))
            if h_choice==1:
                if len(hostellers)==0:
                    id=1
                else:
                    id=hostellers[-1]['id']+1
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
            elif h_choice==2:
                print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('id','name','age','address','phone','gaurdian_name','gaurdian_phone','room_no','floor','rent','join_date'))
                print('-'*163)
                for i in hostellers:
                    print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(i['id'],i['name'],i['age'],i['address'],i['phone'],i['gaurdian_name'],i['gaurdian_phone'],i['room_no'],i['floor'],i['rent'],i['join_date']))
            elif h_choice==3:
                id=int(input("enter id : "))
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
                if f==0:
                    print("Invalid id")
            elif h_choice==4:
                id=int(input("Enter id : "))
                f=0
                for i in hostellers:
                    if i['id']==id:
                        f=1
                        hostellers.remove(i)
                if f==0:
                    print("Invalid  id")
            elif h_choice==5:
                break
    elif choice==3:
        while True:
            print(
                '''
                1.Details of cook
                2.Details of cleaner
                3.Exit
            '''
            )
            w_choice=int(input("Enter your choice :: "))
            if w_choice==1:
                while True:
                    print(
                        '''
                        1.Add cook
                        2.View cook deatails
                        3.Update cook details
                        4.Delete cook
                        5.Exit
                        '''
                    )
                    cook_choice=int(input("Enter your choice : "))
                    if cook_choice==1:
                        cook_id=int(input("Enter id of cook : "))
                        cook_name=input("Enter name of cook : ")
                        cook_place=input("Enter place : ")
                        cook_contact=int(input("Enter contact number : "))
                        workers.append({'cook_id':cook_id,'cook_name':cook_name,'cook_place':cook_place,'cook_contact':cook_contact})
                    elif cook_choice==2:
                        print('{:<12}{:<12}{:<12}{:<12}'.format('cook_id','cook_name','cook_place','cook_contact'))
                        print('-'*70)
                        for i in workers:
                            print('{:<12}{:<12}{:<12}{:<12}'.format(i['cook_id'],i['cook_name'],i['cook_place'],i['cook_contact']))
                    elif cook_choice==3:
                        id=int(input("enter cook id : "))
                        f=0
                        for i in workers:
                            if i['cook_id']==id:
                                f=1
                                new_cname=input("Enter new name : ")
                                new_contact=int(input("Enter new phone number : "))
                                i['cook_name']=new_cname
                                i['cook_contact']=new_contact
                    elif cook_choice==4:
                        id=int(input("Enter cook id : "))
                        f=0
                        for i in workers:
                            if i['cook_id']==id:
                                f=1
                                workers.remove(i)
                    elif cook_choice==5:
                        break
            elif w_choice==2:
                while True:
                    print(
                        '''
                        1.Add cleaner
                        2.View cleaner details
                        3.Update cleaner
                        4.Delete cleaner
                        5.Exit
                        '''
                    )
                    clean_choice=int(input("Enter your choice : "))
                    if clean_choice==1:
                        cleaner_id=int(input("Enter id : "))
                        cleaner_name=input("Enter name of cleaner")
                        cleaner_place=input("Enter place of cleaner : ")
                        cleaner_phone=int(input("Enter contact : "))
                        workers.append({'cleaner_id':cleaner_id,'cleaner_name':cleaner_name,'cleaner_place':cleaner_place,'cleaner_phone':cleaner_phone})
                    elif clean_choice==2:
                        print('{:<12}{:<12}{:<12}{:<12}'.format('cleaner_id','cleaner_name','cleaner_place','cleaner_phone'))
                        print('-'*70)
                        for i in workers:
                            print('{:<12}{:<12}{:<12}{:<12}'.format(i['cleaner_id'],i['cleaner_name'],i['cleaner_place'],i['cleaner_phone']))
                    elif clean_choice==3:
                        id=int(input("enter cleaner id : "))
                        f=0
                        for i in workers:
                            if i['cleaner_id']==id:
                                f=1
                                new_clname=input("Enter new name : ")
                                new_clcontact=int(input("Enter new phone number : "))
                                i['cleaner_name']=new_clname
                                i['cleaner_phone']=new_clcontact
                    elif clean_choice==4:
                        id=int(input("Enter cleaner id : "))
                        f=0
                        for i in workers:
                            if i['cleaner_id']==id:
                                f=1
                                workers.remove(i)
                    elif clean_choice==5:
                        break
            elif w_choice==3:
                break
    elif choice==4:
        break