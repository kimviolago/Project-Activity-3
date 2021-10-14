from tkinter import*
import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "UiOM9XuMWPZkCSJtwx2uwj3oCCgdClMv"
root = Tk()
root.geometry("1000x2000")
root.title("Map Quest")

heading = Label(text="Map Quest API", bg="black",
                fg="white", width="500", height="5")
heading.pack()

LabelLocation = Label(text="Enter your Current Location* ",
                      font="Helvetica 15", anchor='nw')
LabelLocation.pack(pady=20)
location = Entry(root, width=50)
location.pack(pady=20)

LabelDestination = Label(
    text="Enter your Destination Location* ", font="Helvetica 15")
LabelDestination.pack(pady=20)
destination = Entry(root, width=50)
destination.pack(pady=20)


def onClick():
    while True:

        url = main_api + \
            urllib.parse.urlencode(
                {"key": key, "from": location, "to": destination})
        print("URL ", (url))
        json_data = requests.get(url).json()
        json_status = json_data["info"]["statuscode"]
        if json_status == 0:
            argument = "\nAPI Status: " + str(json_status) + " = A successful route call.\n"\
                "\n=============================================" + "\nDirections from " + (location.get()) + " to " + (destination.get())\
                + "\nTrip Duration: " + (json_data["route"]["formattedTime"])\
                + "\nKilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6))\
                + "\nFuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78))\
                + "\n============================================="
            myResult1 = Label(root, text=argument)
            myResult1.pack()
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                argument2 = (each["narrative"]) + " (" + \
                    str("{:.2f}".format((each["distance"])*1.61) + " km)")
                myResult2 = Label(root, text=argument2,
                                  font="Helvetica 10", justify=LEFT)
                myResult2.pack()
        elif json_status == 402:
            argument3 = "**********************************************"\
                + "Status Code: " + str(json_status) + "; Invalid user inputs for one or bothlocations."\
                + "**********************************************\n"
            myLabel3 = Label(root, text=argument3)
            mylabel3.pack()
        elif json_status == 611:
            argument4 = "**********************************************"\
                + "Status Code: " + str(json_status) + "; Missing an entry for one or bothlocations."\
                + "**********************************************\n"
            myLabel4 = Label(root, text=argument4)
            mylabel4.pack()
        else:
            argument5 = "************************************************************************"\
                + "For Staus Code: " + str(json_status) + "; Refer to:"\
                + "https://developer.mapquest.com/documentation/directions-api/status-codes"\
                + "************************************************************************\n"
            myResult = Label(root, text=argument5)
            myResult.pack(pady=20)
        break


myButton = Button(root, text="Submit", command=onClick)
myButton.pack()


root.mainloop()
