ipAddress = input("Please enter an IP Address: ")
if ipAddress[-1] != '.':
    ipAddress += "."
segment = 1
segment_length = 0
# char = ""

for char in ipAddress:
    if char == ".":
        print("segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# unless the final character in a string was a . then we haven't printed the last segment
# if char != ".":
#     print("segment {} contains {} characters".format(segment, segment_length))