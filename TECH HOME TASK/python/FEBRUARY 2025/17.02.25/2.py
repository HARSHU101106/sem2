from collections import Counter
def common_elements_dict():
    list1 = list(map(int, input("Enter first list (space-separated): ").split()))
    list2 = list(map(int, input("Enter second list (space-separated): ").split()))
    common = set(list1) & set(list2)
    count1 = Counter(list1)
    count2 = Counter(list2)
    result = {key: count1[key] + count2[key] for key in common}
    print("Common Elements with Counts:", result)
common_elements_dict()
