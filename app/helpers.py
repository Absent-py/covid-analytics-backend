def toRange(num):
    upper_bound = 15860457
    if num < upper_bound / 10:
        return 6
    if upper_bound / 10 < num < upper_bound / 10 * 2:
        return 8
    if upper_bound / 10 * 2 < num < upper_bound / 10 * 3:
        return 10
    if upper_bound / 10 * 3 < num < upper_bound / 10 * 4:
        return 12
    if upper_bound / 10 * 4 < num < upper_bound / 10 * 5:
        return 14
    if upper_bound / 10 * 5 < num < upper_bound / 10 * 6:
        return 16
    if upper_bound / 10 * 6 < num < upper_bound / 10 * 7:
        return 18
    if upper_bound / 10 * 7 < num < upper_bound / 10 * 8:
        return 20
    if upper_bound / 10 * 8 < num < upper_bound / 10 * 9:
        return 22
    if upper_bound / 10 * 9 < num < upper_bound / 10 * 10:
        return 24

