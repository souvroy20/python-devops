list2 = ["aws", "gcp", "azure", "alibaba", "ibm"]
print("Cloud Providers:", list2)

# adds elements to the end of the list2
list2.append("oracle")
print("Cloud Providers:", list2)

list2.append("digitalocean")
print("Cloud Providers:", list2)

list2.insert(1, "linode")
print("Cloud Providers:", list2)

list2.remove("ibm")
print("Cloud Providers:", list2)
list2.pop(2)
print("Cloud Providers:", list2)

print(len(list2))

# iteration through the list2
for cloud in list2:
    print("")
    print("Cloud Provider:", cloud)
    # print("Length of list2:", len(list2))

test_list = list("abcdef")
print(test_list)
