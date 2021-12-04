# file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')
# list_1 = []
# for line in file_1:
#     splitted = line.split()
#     list_1.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
# file_1.close()
# print(list_1)
# list_2 = []
with open('nginx_logs.txt') as f:
    data = []
    spam_dict = {}
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam_dict.setdefault(splitted[0], 0)
        spam_dict[splitted[0]] += 1

spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
print(spam_dict[:5])  # Not only one spamer
