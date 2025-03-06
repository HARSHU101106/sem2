def tuples_to_dict():
    n = int(input("Enter number of key-value pairs: "))
    tuples_list = [tuple(input(f"Enter key-value pair {i+1} (format: key value): ").split()) for i in range(n)]
    result_dict = {k: int(v) if v.isdigit() else v for k, v in tuples_list}
    print("Converted Dictionary:", result_dict)
tuples_to_dict()
