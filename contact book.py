contact_list={}
def disp_cont():
    print("name \t \t contact Number")
    for key in contact_list:
        print("{} \t\t {}".format(key,contact_list.get(key)))

while True:
    select=int(input("1. Add new contact \n2. View contact \n3. Search contact \n4. Update contact \n5. Delete Contact\n 6.Exit\n"))
    if select == 1:
        name=input("Enter The Contact Name ")
        phone=input("Enter The Mobile Number ")
        contact_list[name] = phone
    elif select == 3:
        search = input("Enter The Contact Name ")
        if search in contact_list:
            print(search,"'s Contact Number Is",contact_list[search])
        else:
            print("Name Is Not Found In The Contact Book ")
    elif select == 2:
        if not contact_list:
            print("Empty Contact Book")
        else:
            disp_cont()
    elif select == 4:
        update_cont=input("Enter The Contact To Be Edited ")
        if update_cont in contact_list:
            phone =input("Enter Mobile Number" )
            contact_list[update_cont]=phone
            print("Contact Updated")
            disp_cont()
        else :
            print("Name Is Not Found In The Contact Book")
    elif select == 5:
        del_cont = input("Enter The Contact To Be Deleted ")
        if del_cont in contact_list:
            confirm =input("Do You Want To Delete This Contact y/n?")
            if confirm =="y" or confirm =="Y":
                contact_list.pop(del_cont)
                disp_cont()
            else:
                print("Name Is Not Found In The Contact Book")
    else:
        break
