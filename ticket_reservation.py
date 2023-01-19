print("\n\nWelcome! To Ticket Booking System\n")
restart= ('Y')
while restart not in ['N','n','NO','no']:
    print("New Ticket Reservation")
    people = int(input("\nEnter no. of Ticket you want : "))
    name_l = []
    age_l = []
    sex_l = []
    start_l = []
    end_l = []
    for p in range(people):
        name = str(input("\nName : "))
        name_l.append(name)
        age = int(input("\nAge : "))
        age_l.append(age)
        sex = str(input("\nMale or Female : "))
        sex_l.append(sex)
        start = str(input("\nStarting Destination : "))
        start_l.append(start)
        end = str(input("\nEnding Destination : "))
        end_l.append(end)
    print("\nTotal Ticket : ",people,"\n")
    for i in range(0,people):
        print("Ticket Number: ",i+1)
        print("Name : ",name_l[i])
        print("Age : ",age_l[i])
        print("Sex : ",sex_l[i])
        print("Starting Destination : ",start_l[i])
        print("Ending Destination : ",end_l[i])
        print("\n")
    restart = str(input("\nNew Booking Y/N : "))
    if restart in ('y','YES','yes','Yes','Y'):
        restart = ('Y')
    else:
        print("Thank You")
        restart=('N')

        
