def ft_count_harvest_recursive(day_to_harvest=None, day=1):
    if day == 1:
        day_to_harvest = int(input("Days until harvest: "))
    if day > day_to_harvest:
        print("Harvest time!")
        return
