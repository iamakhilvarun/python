#I can set values of default parmeters inside the function and 
# still i can change that value when i am calling
def banner_text(text:str = " ",screen_width:int = 80)->None:
    """ 
     print ** either side of string ,the string should be centered 

    :param str text: The astrisk (*) will result in a row of (*)
                    , defaults to " "
    :param int screen_width: The screen_width we want to put , defaults to 80
    :raises ValueError: if len of text is bigger than screen width it will show error  
    """
    if len(text)>screen_width -4 :
            raise ValueError("String {0} is the larger than the specified width {1}"
                         .format(text,screen_width))
    

    if text == "*":
        print("*"*screen_width)
    else:
        centered_text=text.center(screen_width-4)
        output_string="**{0}**".format(centered_text)
        print(output_string)

banner_text("*")
banner_text("Oh-oh, ooh",)
banner_text("You've been runnin' 'round, runnin' 'round, runnin' 'round throwin' ")
banner_text("that dirt all on my name")
banner_text("'Cause you knew that I, knew that I, knew that I'd call you up",)
banner_text("You've been going 'round, going 'round, going 'round every party in L.A.")
banner_text(screen_width=60)
banner_text("'Cause you knew that I, knew that I, knew that I'd be at one, oh",70)
banner_text("I know that dress is karma, perfume regret",70)
banner_text("You got me thinking 'bout when you were mine, oh",70)
banner_text("*",70)
#“First it goes into the function and prints the banner text, 
# then since there is no return value, result becomes None, and printing it shows None.”
result=banner_text("Nothing is required",70)
print(result)