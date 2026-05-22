def  ft_count_harvest_iterative():
    days_to_harvest = int(input("Days until harvest: "))
    for day in range(1, days_to_harvest + 1):
        print("Day " + str(day))
    print("Harvest time!")