# # jabber = open('Jabberwocky.txt', 'r')

# # for line in jabber:
# #     print(line.strip())
# #     # print(len(line))
# # jabber.close()

# with open ('Jabberwocky.txt','r')  as jabber:  # 'r' means read mode --> telling python to open the file so 
                                                 # I can read its contents
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines=jabber.readlines()
#     # print(lines)

# print(lines)
# print(lines(-1:))
# for line in reversed(lines):
#     print(line,end='') # do some processing in reverse order


# with open ('Jabberwocky.txt') as jabber:
#     text=jabber.read()

# # print(text)
# for charcter in reversed(text):
#     print(charcter,end='')


with open('Jabberwocky.txt') as jabber:
    while True:
        line=jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*'*80)
with open ('jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break