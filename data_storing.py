list = ["aws", "gcp", "azure", "alibaba", "ibm"]
print("Cloud Providers:", list)

# adds elements to the end of the list
list.append("oracle")
print("Cloud Providers:", list)

list.append("digitalocean")
print("Cloud Providers:", list)

list.insert(1, "linode")
print("Cloud Providers:", list)

list.remove("ibm")
print("Cloud Providers:", list)
list.pop(2)
print("Cloud Providers:", list)

print(len(list))

# iteration through the list
for cloud in list:
    print("")
    print("Cloud Provider:", cloud)
    # print("Length of list:", len(list))
