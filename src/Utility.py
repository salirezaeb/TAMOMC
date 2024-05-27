def utility(x):
    x = x.lower()
    if x == 'a':
        return '\nThe characteristics of the selected street are that this street has (2) lanes and its length is (10 kilometers). The density of this street is based on the calculations provided by article is (17.0)  Therefore, it can be said that this street is ( high safe and high quality) in terms of density and number of lanes\n'
    elif x == 'b':
        return '\nThe characteristics of the selected street are that this street has (2) lanes and its length is (5 kilometers). The density of this street is based on the calculations provided by article is (32.9)  Therefore, it can be said that this street is (safe and high quality) in terms of density and number of lanes\n'
    elif x == 'c':
        return '\nThe characteristics of the selected street are that this street has (2) lanes and its length is (5 kilometers). The density of this street is based on the calculations provided by article is (18.09)  Therefore, it can be said that this street is ( high safe and high quality) in terms of density and number of lanes\n'
    elif x == 'd':
        return '\nThe characteristics of the selected street are that this street has (2) lanes and its length is (10 kilometers). The density of this street is based on the calculations provided by article is (35.7)  Therefore, it can be said that this street is (safe and high quality) in terms of density and number of lanes\n'
    elif x == 'e':
        return '\nThe characteristics of the selected street are that this street has (1) lane and its length is (10 kilometers). The density of this street is based on the calculations provided by article is (52.2)  Therefore, it can be said that this street is ( low safe and low quality) in terms of density and number of lanes\n'
    elif x == 'f':
        return '\nThe characteristics of the selected street are that this street has (2) lanes and its length is (7 kilometers). The density of this street is based on the calculations provided by article is (90.5)  Therefore, it can be said that this street is (not safe and low quality) in terms of density and number of lanes\n'
    elif x == 'g':
        return '\nThe characteristics of the selected street are that this street has (2) lanes and its length is (7 kilometers). The density of this street is based on the calculations provided by article is (79.6)  Therefore, it can be said that this street is (safe and low quality) in terms of density and number of lanes\n'
    elif x == 'h':
        return '\nThe characteristics of the selected street are that this street has (1) lane and its length is (9 kilometers). The density of this street is based on the calculations provided by article is (21.4)  Therefore, it can be said that this street is (safe and high quality) in terms of density and number of lanes\n'
    elif x == 'i':
        return '\nThe characteristics of the selected street are that this street has (1) lane and its length is (8 kilometers). The density of this street is based on the calculations provided by article is (18.5)  Therefore, it can be said that this street is (safe and high quality) in terms of density and number of lanes\n'
    elif x == 'j':
        return '\nThe characteristics of the selected street are that this street has (2) lanes and its length is (20 kilometers). The density of this street is based on the calculations provided by article is (4.8)  Therefore, it can be said that this street is ( verysafe and  veryhigh quality) in terms of density and number of lanes\n'
    else:
        return '\nplease choose the correct letter'

continue_program = True

while continue_program:
    y = input("\n>.>.>.>.>.>.>.>.>  Please choose your desired street from the letters below  <.<.<.<.<.<.<.<.<\n\n **** a b c d e f g h i j **** \n")
    result = utility(y)
    print(result)

    y_or_n = input("Do you want to continue? (y/n): ")
    if y_or_n.lower() != 'y':
        continue_program = False
