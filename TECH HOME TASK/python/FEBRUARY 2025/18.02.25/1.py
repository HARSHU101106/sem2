lst_strings=list(map(str,input().split()))
preffix=lst_strings[0]
for i in lst_strings[1:]:
    while not i.startswith(preffix):
        preffix=preffix[:-1]
        if not preffix:
            break