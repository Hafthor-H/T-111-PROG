import sys


def main():
    # Simple test script.
    sys.stderr.write("Input music, group, singer: ")
    music, group, singer = input().split(",")

    state_music_opinion(music, group, singer)
    print()
    state_music_opinion()


# Definition for state_music_opinion goes here.

def  state_music_opinion(genre="Classic Rock", music_group="The Beatles", vocalist="Freddie Mercury"):
    print("The best type of music is ", genre + ".")
    print("The best music group is ", music_group + ".")
    print("The best lead vocalist is ", vocalist + ".")
if __name__ == "__main__":
    main()