with open("file.txt", "r") as f:
    lines = f.readlines()
    addresses = []
    private_keys = []
    for i in lines:
        addresses.append(i.split('\t')[0] + '\n')
        private_keys.append(i.split('\t')[1])

with open("addresses.txt", "w") as f:
    f.writelines(addresses)

with open("private_keys.txt", "w") as f:
    f.writelines(private_keys)
