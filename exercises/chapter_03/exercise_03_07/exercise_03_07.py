# 3-7 Guest List

guest_list = ["Albert Einstein", "Isac Newton", "Marie Curie", "Galileo Galilei"]

message = "Hi " + guest_list[0] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[1] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[2] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[3] + " you are invited to dinner at 7 on saturday."
print(message)

cancelation_message = guest_list[1] + " can not attend the dinner."
print(cancelation_message)

guest_list[1] = "Charles Darwin"

message = "Hi " + guest_list[0] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[1] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[2] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[3] + " you are invited to dinner at 7 on saturday."
print(message)

message = "I have a bigger table now so three more people will be invited."
print(message)

guest_list.insert(0, "Stephen Hawking")
guest_list.insert(2, "Louis Pasteur")
guest_list.append("Nicolaus Copernicus")

message = "Hi " + guest_list[0] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[1] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[2] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[3] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[4] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[5] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[6] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Change of plans only two people can come to dinner this time."
print(message)

uninvited = guest_list.pop()
message = "Sorry " + uninvited + " you will have to come another time."
print(message)

uninvited = guest_list.pop()
message = "Sorry " + uninvited + " you will have to come another time."
print(message)

uninvited = guest_list.pop()
message = "Sorry " + uninvited + " you will have to come another time."
print(message)

uninvited = guest_list.pop()
message = "Sorry " + uninvited + " you will have to come another time."
print(message)

uninvited = guest_list.pop()
message = "Sorry " + uninvited + " you will have to come another time."
print(message)

message = "Hi " + guest_list[0] + " you are invited to dinner at 7 on saturday."
print(message)

message = "Hi " + guest_list[1] + " you are invited to dinner at 7 on saturday."
print(message)

del guest_list[1]
del guest_list[0]

print(guest_list)

