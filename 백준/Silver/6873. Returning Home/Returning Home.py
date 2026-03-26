way = ''
street = ''
way_list = []
street_list = []
while street != 'SCHOOL':
    way = input()
    street = input()
    way_list.append(way)
    street_list.append(street)

for i in range(len(way_list) - 1, -1, -1):
    if i != 0:
        if way_list[i] == 'R':
            print(f"Turn LEFT onto {street_list[i - 1]} street.")
        else:
            print(f"Turn RIGHT onto {street_list[i - 1]} street.")
    else:
        if way_list[i] == 'R':
            print("Turn LEFT into your HOME.")
        else:
            print("Turn RIGHT into your HOME.")