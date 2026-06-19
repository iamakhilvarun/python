def removeprefix(string: str,prefix:str)-> str:
    if string.startswith(prefix):
        return string(len(prefix):)
    else:
        return string(:) # Return a copy of string
    
def removesuffix(string:str,suffix:str)->str:
    if suffix.endswith(suffix):
        return string(:-len(suffix))
    else:
        return string(:)
    
filename='Jabberwocky.txt'
with open(filename) as poem:
    first=poem.readline().rstrip()

print(first)

chars="' Twasebv"
# no_astrophe= first.strip(chars)
# print(no_astrophe)

# telling how strip() removes char from start of the string
for charcter in first:
    if charcter in chars:
        print(f'removing "{charcter}"')
    else:
        break

print('*'*80)
# telling how strip() removes char from behind
for charcter in first(::-1):
     if charcter in chars:
        print(f'removing "{charcter}"')
     else:
        break
     
print('*'*80)

# twas_removed= first.removeprefix("'Twas")
twas_removed= removeprefix(first,"'Twas")
print(twas_removed)
# toves_removed= first.removesuffix("toves")
toves_removed= removesuffix(first,"toves")
print(toves_removed)