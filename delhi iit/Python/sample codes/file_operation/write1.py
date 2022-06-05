with open('C:\Users\kulbhushan.s\Desktop\ipv6_address.txt','r') as read_f:
    text=read_f.read()
read_f.close()

print text

with open('C:\Users\kulbhushan.s\Desktop\ipv6_address_copy.txt','w') as write_f:
    write_f.write(text)
write_f.close()
