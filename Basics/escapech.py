# \n skips the line in code
split_string = " these \n lines\n are \n going\n to \n appear \n in several\n lines"
print("split_string")
# print(splitstring)

splittab = "these\twords\tare\tare\tgoing\tto\nappear\tin\tseveral\ttabs"
# print(splittab)

print("the pet house owner said \"No, no, 'e's uh,...he's resting\".")
# or
print("the pet house owner said \"No, no, 'e's uh,...he's resting\".")
# or
print(
    """the pet house owner said "No, no, \
'e's uh,...he's resting"."""
)

anothersplitstring = """this line
is split
over
in
several
lines"""

print(anothersplitstring)
# if add \ then lines wont we in several lines couse i used escape
anothersplitstring = """this line \
is split \
over \
in \
several \
lines"""

print(anothersplitstring)


print("c:\\user\\terimaakabhosda\\notes.txt")  # preferable
print(
    r"c:\user\terimaakabhosda\notes.txt"
)  # A raw string tells Python NOT to treat backslashes (\) as escape characters.
