# snackInput = input("What is your favorite snack? ")
# # if snackInput == "cookies":
# #     print("You chose cookies!")
# # elif snackInput == "samosa":
# #     print("You chose samosa!")
# # else:
# #     print("Sorry, that's not available.")


# if snackInput == "cookies" or snackInput == "samosa":
#     print("Yum!")
# else:
#     print("Sorry, we don't have that.")

# cupSize = input("What size cup do you want? (small, medium, large) ")
# if cupSize == "small":
#     print("You chose a small cup. That will be 10Rs.")
# elif cupSize == "medium":
#     print("You chose a medium cup. That will be 15Rs.")
# elif cupSize == "large":
#     print("You chose a large cup. That will be 30Rs.")
# else:
#     print("Sorry, that's not available.")

# device_Status = True
# temperature = 40
# if device_Status:
#     if temperature > 35:
#         print("Warning: temperature is very high")
#     else:
#         print("temperature is normal")
# else:
#     print("The device is OFF")

# order_amount = int(input("Enter the order amount: "))
# message = "You get a Free Delivery!" if order_amount > 300 else "Delivery charge is 30Rs."
# print(message)

seat_type = input("Enter the seat type (sleeper,general,ac,luxury): ").lower()

match seat_type:
    case "sleeper":
        print("You chose a sleeper seat. That will be 500Rs.")
    case "general":
        print("You chose a general seat. That will be 300Rs.")
    case "ac":
        print("You chose an AC seat. That will be 600Rs.")
    case "luxury":
        print("You chose a luxury seat. That will be 1000Rs.")
    case _:
        print("Sorry, that's not available.")