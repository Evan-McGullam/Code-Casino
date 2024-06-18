loop = 1

while loop == 1:
  print("")
  print("Here are our games. To pick one, type the number of the game you would like to play!")
  selection = input("1. Blackjack, 2. Hangman, 3.Makeshift Dice")
  if selection == "1":
    from subprocess import call
    def open_py_file():
          call(["python", "Blackjack.py"])
    open_py_file()
    loop = 0
  elif selection == "2":
      from subprocess import call
      def open_py_file():
          call(["python", "Hangman.py"])
      open_py_file()
      loop = 0
  elif selection == "3":
    from subprocess import call
    def open_py_file():
        call(["python", "Dice.py"])
    open_py_file()
    loop = 0
  else:
    print("Please enter a valid input.")