fp = open ('F:\d_bratchykau\python\litle_access.txt', 'r')
# for line in fp:
    # fp.readline()
    # line.split()
    # print(line)

# l = (fp.readline().split())
# print(l[0])
# g = []
# g.append(l[0])

# print(g)

print(fp.readline().split()) 

ips = [] # создаём список для хранения IP

#цикл где осуществляется разбивка строки по пробелам и преобразование в список
for log in fp:
    just_ip = (fp.readline().split()[0])
    # just_browser = (fp.readline().split()[-8])
    ips.append(just_ip)
    # browser.append(just_browser)

print(ips)



    

