import math
initialInput = input()
splitInput = initialInput.split(" ")
number_of_matches = int(splitInput[0])
width_of_box = int(splitInput[1])
length_of_box = int(splitInput[2])
max_match_height = float(math.sqrt((width_of_box ** 2) + (length_of_box ** 2)))
output_list = []
for _ in range(number_of_matches):
    match = int(input())
    if match > max_match_height:
        output_list.append("NE")
    else:
        output_list.append("DA")
for _ in range(number_of_matches):
    print(output_list[_ - 1])
