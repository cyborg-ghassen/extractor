with open("file.txt", "r") as f:
    lines = f.readlines()
    addresses = []
    private_keys = []
    for i in lines:
        splitted = i.split('\t')
        addresses.append(splitted[0] + '\n')
        private_keys.append(splitted[1] + '\n')

with open("addresses.txt", "w") as f:
    f.writelines(addresses)

with open("private_keys.txt", "w") as f:
    f.writelines(private_keys)
