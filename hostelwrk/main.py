from admin import *
from hosteller import *
while True:
    print(
        '''
        1.Admin
        2.User
        3.Exit
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
                5.Add hosteller
                6.View hosteller's deatils
                7.Update details
                8.Delete hosteller
                9.Add cook
                10.View cook deatails
                11.Update cook details
                12.Delete cook
                13.Add cleaner
                14.View cleaner details
                15.Update cleaner
                16.Delete cleaner
                17.Exit

                
            '''
            )
            sub_choice=int(input("enter your choice : "))
            if sub_choice==1:
                add_rooms()
            elif sub_choice==2:
                view_room()
            elif sub_choice==3:
                update_room()
            elif sub_choice==4:
                delete_room()
            elif sub_choice==5:
                add_hosteller()
            elif sub_choice==6:
                view_hosteller()
            elif sub_choice==7:
                update_hosteller()
            elif sub_choice==8:
                remove_hosteller()
            elif sub_choice==9:
                add_cook()
            elif sub_choice==10:
                view_cook()
            elif sub_choice==11:
                update_cook()
            elif sub_choice==12:
                remove_cook()
            elif sub_choice==13:
                add_cleaner()
            elif sub_choice==14:
                view_cleaner()
            elif sub_choice==15:
                update_cleaner()
            elif sub_choice==16:
                remove_cleaner()
            elif sub_choice==17:
                break
    # elif choice==2:
        # user 


# while True:
#     print(
#         '''
#         1.Admin
#         2.User
#         3.Exit
#     '''
#     )
#     choice=int(input("Enter your choice : "))
#     if choice==1:
#         while True:
#             print(
#                 '''
#                 1.Room Details
#                 2.Person Details
#                 3.Worker's Details
#                 4.Exit
#             '''
#             )
#             sub_choice=int(input("enter your choice : "))
#             if sub_choice==1:
#                 while True:
#                     print(
#                         '''
#                         1.Add Rooms
#                         2.View room details
#                         3.Update room details
#                         4.Delete room
#                         5.Exit
#                     '''
#                     )
#                     admin_choice=print("enter your choice : ")
#                     if admin_choice==1:
#                         add_rooms()
#                     elif admin_choice==5:
#                         break
#             elif sub_choice==4:
#                 break
#     elif choice==3:
#         break