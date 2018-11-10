# ip_add = input("enter ip address :")
# segment = 1
# segment_length = 0
# char = ""
#
# for char in ip_add:
#     if char == ".":
#         print("Segment {} is of {} length".format(segment, segment_length))
#         segment += 1
#         segment_length = 0
#     else:
#         segment_length += 1
#
# if char != ".":
#     print("Segment {} is of {} length".format(segment, segment_length))

ip_add = input("enter ip address :")
if ip_add == "":
    ip_add += "."
elif ip_add[-1] != ".":
    ip_add += "."
segment = 1
segment_length = 0


for char in ip_add:
    if char == ".":
        print("Segment {} is of {} length".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

