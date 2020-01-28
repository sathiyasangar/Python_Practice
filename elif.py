#! /usr/bin/python


list =["Sathiya", "Sangar", "PS"]

if len(list)==3:
    print(len(list))
    if "P" in list:
        print("Sucess Nested Condition")
    else:
        print("Failure")
		

elif list.count("Sathiya")==1:
  

    print("Elif Success")

else:
    print("Else Success")

