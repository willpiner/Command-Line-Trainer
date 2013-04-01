import sys
# questions
basic_questions = [
  ["Change into a directory called 'cats'","cd cats"],
  ["Copy the contents of the file 'foo.txt' to the file 'bar.txt'","cp foo.txt bar.txt"],
  ["list the contents of your current directory", "ls"],
  ["Change the name of the file 'qux.txt' to 'baz.txt'", "mv qux.txt baz.txt"],
  ["Delete a file name 'foo.rb'", "rm foo.rb"],
  ["Print out the directory you are currently in", "pwd"],
  ["Make a new directory called 'cats'", "mkdir cats"]
]

apt_questions = [
  ["Search for a package named 'burgers'","apt-cache search burgers"],
  ["Become super-user then install a package named 'coolstory'","sudo apt-get install coolstory"],
  ["Find out information about a package named 'python'", "apt-cache show python"],
  ["Become super-user, Remove a package named 'cats'", "sudo apt-get remove cats"],
  ["Become super-user, Remove a package named 'cats' AND remove the config files", "sudo apt-get --purge remove cats"],
]

# Starting prompt

print """
Welcome to the Command Line Trainer!
What quiz would you like to take today?
Press 1 to take the basic Unix commands quiz.
Press 2 to take the Apt package manager commands quiz.
"""

user_selects = raw_input("> ")

# Quiz selector
if user_selects == "1":
    questions = basic_questions
else:
    questions = apt_questions

i = 0
for question in questions:
    prompt = questions[i][0]
    correct_answer = questions[i][1]
    print prompt
    user_input = raw_input("> ") 
    if user_input == correct_answer:
        print "\nCorrect!\n"
        i+=1
        continue
    elif user_input == "exit" or user_input == "quit":
        sys.exit()
    else:
        print "\nWrong!\n"
        i+=1
        continue

#future updates:
    #add how to compile
    #add how to add ubuntu ppa repository
    #rewrite in ruby
    #add hints
    #randomize questions
    #more questions
