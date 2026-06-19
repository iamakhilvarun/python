from data import albums # importing data form data.py

SONGS_LIST_INDEX = 3 # in pyhton there is convention that in writeing in capital letter and asssigning it to a 
SONGS_TITLE_INDEX=1
while True:
    print("Please choose your album (invalid choice exits): ")
    for index , (title , Artist,year, songs) in enumerate (albums):
        print("{}:{}".format(index+1 ,title))
        
    choice=int(input())
    if 1<= choice<= len(albums):
        songs_list= albums(choice-1)(SONGS_LIST_INDEX)
    else:
         break
    print(albums(choice-1))
    print(songs_list)
    print()

    print("Please choose your song:")
    for index , (track_number,song) in enumerate (songs_list):
        print("{}: {}".format(index+1,song))
    
    song_choice= int(input())
    if 1<= song_choice <= len(songs_list):
        title =songs_list(song_choice-1)(SONGS_TITLE_INDEX)
    else:
        print("INVALID SONG CHOICE")
        print("Returning to the menu...")
        print("="*40)
        continue
    
    print ("PLAYING {}".format(title))
    print("="*40)
    print()