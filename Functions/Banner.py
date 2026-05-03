def banner_text(text):
    screen_width=80
    if len(text)>screen_width -4 :
        print("EEK!!")
        print("THE TEXT IS TOO LONG TO FIT IN SPECIFIED WIDTH")
        return
       
    if text == "*":
        print("*"*screen_width)
    else:
        centered_text=text.center(screen_width-4)
        output_string="**{0}**".format(centered_text)
        print(output_string)

banner_text("*")
banner_text("Oh-oh, ooh")
banner_text("You've been runnin' 'round, runnin' 'round, runnin' 'round throwin' ")
banner_text("that dirt all on my name")
banner_text("'Cause you knew that I, knew that I, knew that I'd call you up")
banner_text("You've been going 'round, going 'round, going 'round every party in L.A.")
banner_text("")
banner_text("'Cause you knew that I, knew that I, knew that I'd be at one, oh")
banner_text("I know that dress is karma, perfume regret")
banner_text("You got me thinking 'bout when you were mine, oh")
banner_text("*")

result=banner_text("Nothing is reqired")
print(result)