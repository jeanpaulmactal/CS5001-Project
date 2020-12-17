def banner(string):

#    print("*" * 94)
#    print("*" * 15 + " " * 5 + "Welcome to Jean Paul's Travelog and Recommendations!!!" + " " * 5 + "*" * 15) 
#    print("*" * 94)

    border = "*" * 94 
    main_text = "*" * 15 + " " * 5 + "Welcome to " + "{}'s " + "Travelog and Recommendations!!!" + " " * 5 + "*" * 15

    
    print(border)
    print(border)
    print(main_text.format(string))
    print(border)
    print(border)