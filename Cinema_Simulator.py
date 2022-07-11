films={
     "Hridayam":[15,3],
    "GoDaddy":[18,10],
    "Supper Sharanya":[18,2]
}
while True:
    name=input("What is your Name?: ").strip().capitalize()
    print("Hello welcome {}!".format(name))
    choice=input("Which film would you like to watch?: ").strip().title()
    if choice in films:
        age=int(input("How old are you?: ").strip())
        if age>=films[choice][0]:
            if films[choice][1]>0:
                print("Enjoy the film.....")
                films[choice][1]=films[choice][1]-1
            else:
                print("Sorry,Tickets are sold out...!")
        else:
            print("Soryy,your age is too long for that film....!")
    else:
        print("Soryy We don't have that film...")
