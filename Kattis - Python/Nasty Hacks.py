number_of_entries = int(input())
output_list = []
for _ in range(number_of_entries):
    line_of_data = input()
    working_data = line_of_data.split(" ")
    expect_without_advertising = int(working_data[0])
    expect_with_advertising = int(working_data[1])
    cost_of_adverising = int(working_data[2])
    determine_advertise = expect_without_advertising + cost_of_adverising
    if expect_with_advertising - determine_advertise == 0:
        output_list.append("does not matter")
    elif expect_with_advertising < determine_advertise:
        output_list.append("advertise")
    elif expect_with_advertising > determine_advertise:
        output_list.append("do not advertise")
for _ in range(number_of_entries):
    print(output_list[_ - 1])