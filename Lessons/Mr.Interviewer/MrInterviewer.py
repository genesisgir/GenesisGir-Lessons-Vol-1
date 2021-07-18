""" 
█▀▀ █▀▀ █▄░█ █▀▀ █▀ █ █▀   █░░ █▀▀ █▀ █▀ █▀█ █▄░█ █▀   █░█ █▀█ █░░ ░ ▄█
█▄█ ██▄ █░▀█ ██▄ ▄█ █ ▄█   █▄▄ ██▄ ▄█ ▄█ █▄█ █░▀█ ▄█   ▀▄▀ █▄█ █▄▄ ▄ ░█ 
Welcome to the genesis gir lesson tutorials Volume 1! We start of the lessons with
you getting to know me! This program tells you more about me and who I am and is more like 
a cool story line about me make sure to pay attention to the functions used and the variables
how they are approached. Thanks for downloading!
⼕ㄖᗪ🝗ᗪ & 山尺讠セセ🝗𝓝 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂 Ꮆ讠尺
"""
"""
█░░█ █▀▀█ █░░░█ 　 ▀▀█▀▀ █▀▀█ 　 █▀▀ █▀▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀ 
█▀▀█ █░░█ █▄█▄█ 　 ░░█░░ █░░█ 　 █░░ █░░█ █░▀░█ █░▀░█ █▀▀ █░░█ ░░█░░ ✎
▀░░▀ ▀▀▀▀ ░▀░▀░ 　 ░░▀░░ ▀▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░
First things first you need to learn how to make single line comments and multi line comments 
so you can add little reminders or give insight on what that line of code does! Comments are
fun great ways to just add notes to a line so you can reflect on them later. They wont show
up in the program its specifically for the developer(you) to look at! So single line comments
start with a hashtag (#) and anything after that will be comments in a greyish tone. Great! Now
you know how to make single line comments but what about multi line comments like this one bro?
Easy all you need to do is start the line with (3 quotes) and than anything after that will be 
comments and to end the finish off the line with another 3 quotes and viola! Your welcome I know 
I'm awesome no need to thank me! (─‿‿─)
"""
# This program is about a creepy interviewer that asks you questions beyond the scope!
# The functions and methods on how it was made will be explained at the end of the code
# Enjoy the code! Thanks for downloading!
"""
█▀▄▀█ █▀█ ░ █ █▄░█ ▀█▀ █▀▀ █▀█ █░█ █ █▀▀ █░█░█ █▀▀ █▀█
█░▀░█ █▀▄ ▄ █ █░▀█ ░█░ ██▄ █▀▄ ▀▄▀ █ ██▄ ▀▄▀▄▀ ██▄ █▀▄
"""
print('The door opens and a man in a suit walks through.')# Using the print function to print values onto the screen
""" The print function is used to print the values in the containers onto the stream(screen)
and in this case to generate text to the program. Its pretty useful and I first start off by
thinking what I want the program to be about and use creative little ideas to conjure up plots.
In this case I chose to make a program that interviews you where Mr.interviewer asks
you random questions with a creepy horror type sense set to it!
"""
print()# Using the print() to create a space between the lines of code you can do this by typing print() into the line
print("He's wearing a black suit and red tie but his face is strangely blank and white") #Using print function to type more values onto screen
"""
█░█ █▀█ █░█░█   ▀█▀ █▀█   █░█ █▀ █▀▀   █▀█ █▀█ █ █▄░█ ▀█▀
█▀█ █▄█ ▀▄▀▄▀   ░█░ █▄█   █▄█ ▄█ ██▄   █▀▀ █▀▄ █ █░▀█ ░█░
The print function always comes with two parentheses and any function in that matter and we 
enter what data types we want inside of them and everything inside of it is called an
argument and the print is called a function and in this case im using a (stir) or better known
as a string to make a storyline! so print(    ) and anything inside it will be printed onto 
stream(screen) just make sure its a correct data type: interger , float or a string value.
""" 
print('He sits down at your table as you both are surrounded by white walls') # Using print 
print('In a errie bright white room.')# Letting the user know what setting they are in!
print('The room gets colder and colder and he begins to stare at you and utters the words.')
# By saying the room gets colder we let the user know its horror themed.
print() # An empty line of text using the print() function!
print("Mr.Interviewer: What's your name sir?") # Asking the user their name. Using print()
name=input()# By entering input() we let the users intake become the variable
#The """ create a multi line comment as you can see below to create multiple lines of comments
# Very useful if you need to leave larger comments but make sure to end it with another """ on the bottom
"""
█░█ █▀█ █░█░█   ▀█▀ █▀█   █░█ █▀ █▀▀   █ █▄░█ █▀█ █░█ ▀█▀
█▀█ █▄█ ▀▄▀▄▀   ░█░ █▄█   █▄█ ▄█ ██▄   █ █░▀█ █▀▀ █▄█ ░█░
input() waits for the users keyboard input and when they press enter it takes that input
this can be very essential to make variables by the user and can be used to your advantage
make sure to practice input() often! And in line 55 I'm using the input() function
to create a variable using the users input to later use it in the program
"""
print() # Empty line of text created using the print() function to put spaces between lines
print("Mr.interviewer: Okay "+name+" I'm going to be asking you some Q&A.") # Using the print again to print values
print()# An empty void of line
print("Mr.Interviewer: What's your favorite thing to do currently?. . .") # Asking them whats their hobby is
hobby=input() # Creating the hobby variable from users input
print() # Using the print function to create a empty line
print('Mr.Interviewer: '+hobby+' Seems pointless you should invest in giving me your data.')
print() # Empty line
print('Mr.interviewer: What are your goals in life if any?. . .') # Asking user for goals
goals=input() # Using the input() to create the goals variable by users intake
print() # Empty line
print('The room gets colder. . .') # More story line to add character to the program using print('enter text here')
print() # Empty line
print('Mr.interviewer: These goals must be important to you '+name+'.')
"""

█▀▀ █ █░█ █ █▄░█ █▀▀   █▀▀ █░█ ▄▀█ █▀█ ▄▀█ █▀▀ ▀█▀ █▀▀ █▀█
█▄█ █ ▀▄▀ █ █░▀█ █▄█   █▄▄ █▀█ █▀█ █▀▄ █▀█ █▄▄ ░█░ ██▄ █▀▄
<<<<<<< HEAD
Notice on how we are bringing life to the character by making him ask redimentary questions
giving the feel that you are connected with mr.interviewer and giving a sense of personality is
=======
Notice on how we are brining life to the character by making him ask redimentary questions
giving the feel that you are connected with Mr.interviewer and giving a sense of personality
>>>>>>> d75008cca94b88bd3e5c109fa2f50bfb5e8dc3a1
very important to be creative during the writing process. Choose a personality for your character!
Which is the fun part you can create all type of personalities using your brain meat. Is the
character a mean or fancy type? or maybe they are cute and friendly? Roleplay and imagination
is really important as well but its all entirely up to you.
                     
░░░░░░░▄█▄▄▄█▄
▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄  print('Mr.Roboto: Hello Twitch!')  
█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█  print('Mr.Roboto: Follow genesis @ https://www.twitch.tv/cashbunny2k ')
░▐▌░░░░▀▀███▀▀░░░░▐▌   
████░▄█████████▄░████  𝙏𝙞𝙥: 𝙎𝙩𝙖𝙮 𝙝𝙮𝙙𝙧𝙖𝙩𝙚𝙙 𝙖𝙣𝙙 𝙙𝙧𝙞𝙣𝙠 𝙥𝙡𝙚𝙣𝙩𝙮 𝙤𝙛 𝙬𝙖𝙩𝙚𝙧 𝙬𝙝𝙞𝙡𝙚 𝙘𝙤𝙙𝙞𝙣𝙜                  

"""
# The program continues here
print() # Empty line using the print() function to create space for other lines to breathe
print('Mr.inteviwer: Are you scared to be poor?. . .') # Asking the user a question
fearofpoverty=input() # fearofpoverty is the variable and the input from the user makes it
print() # Yay another empty line
print("Mr.interviewer: That's understandable. . .") # Talking to the user even more using print
print() # More empty space
print('Mr.interviewer: I believe you know more than your telling me.') # We make the character agitated
print('(Respond to Mr.interviewer than press [ENTER])') # Here we are letting user know to reply to the character
reply=input() # Reply is the variable thati used to later on use to my benefit
print('-You lean in onto the table and say to Mr.interviewer '+reply+'-') # Using the print + variable to make sentences
print() # Empty line using the print() function , type print() to use this feature
print("Mr.interviewer: I know so many things about you I've been watching you for the past") # Character small talk using print function
print('3 days and I know where you sleep, eat, and spend time with family.') # More small talk
print('(Tell him how you feel about invading your privacy)')
reply=input() # Creating the avriable with the user input using the input() function!
print('-Your face shocked and angry at the same time you say '+reply+'-') # Roleplaying with variables + print
print() # Using print() to create space
print('Mr.interviewer: Dont waste my time '+name+' Im accociated with a organization to study') # Driving storyline and adding a variable of the users name 
print('You and gather information about you and this bullshitting is getting us nowhere.') # More story line speech with the print function
print('(Respond to Mr.interviewer than press [ENTER])') # Asking the user to respond to mr.interviewer
reply=input() # The input function takes input from user and overwrites the old variable
print() # Empty line of text! using the print() function
print('You look around the white room and cross your arms and say '+reply+'-')
print() # Oh look another empty line using the print() fucntion
print('Mr.interviewer walks out the room and gathers his paper work') # I used the print function to print values to stream(screen)
print('He closes the door behind him and the room goes dark.') # I used print function to print stir values to stream.
print('((Press [ENTER] to continue)') # Letting the user know to progress
"""
▀█░█▀ █▀▀█ █▀▀█ ░▀░ █▀▀█ █▀▀▄ █░░ █▀▀ █▀▀ 
░█▄█░ █▄▄█ █▄▄▀ ▀█▀ █▄▄█ █▀▀▄ █░░ █▀▀ ▀▀█ 
░░▀░░ ▀░░▀ ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀▀▀ ▀▀▀
Variables are like little tiny safes or cardboard boxes that you can label! In them you can
insert data types from intergers, strings(stirs), floating-points and values to later use
them in your file editor and is a great way to store data.
ex.( box='a cat inside of it' ) we stored "a cat inside of it" inside box making box a variable!

                          ██████                                                                                        
                      ▓▓▓▓      ▓▓░░                                                                           
                  ░░░░              ▓▓▓▓                                                                
              ████                      ████                                                    
          ████                              ████                                        
      ████                                      ████                            
  ████                                              ████                
  ██  ████                                      ████  ▓▓  𝙏𝙞𝙥: 𝙂𝙤𝙤𝙜𝙡𝙚 𝙞𝙨 𝙖 𝙜𝙧𝙚𝙖𝙩 𝙨𝙚𝙖𝙧𝙘𝙝 𝙚𝙣𝙜𝙞𝙣𝙚 𝙛𝙤𝙧 𝙝𝙚𝙡𝙥              
  ██      ▓▓▓▓                              ▓▓▓▓      ▓▓                
  ██          ▓▓▓▓                      ▓▓▓▓          ▓▓  𝙁𝙪𝙣 𝙛𝙖𝙘𝙩: 𝙂𝙚𝙣𝙚𝙨𝙞𝙨 𝙂𝙞𝙧 𝙬𝙖𝙨 𝙤𝙣𝙡𝙮 7 𝙙𝙖𝙮𝙨 𝙞𝙣𝙩𝙤 𝙥𝙧𝙤𝙜𝙧𝙖𝙢𝙢𝙞𝙣𝙜 𝙬𝙝𝙚𝙣 𝙝𝙚 𝙢𝙖𝙙𝙚 𝙩𝙝𝙞𝙨              
  ██              ▓▓▒▒              ▓▓▓▓              ▓▓                
  ██                  ▓▓▓▓      ▓▓▒▒                  ▓▓  𝙏𝙞𝙥: 𝙝𝙩𝙩𝙥𝙨://www.𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙚𝙩𝙝𝙚𝙗𝙤𝙧𝙞𝙣𝙜𝙨𝙩𝙪𝙛𝙛.𝙘𝙤𝙢/2𝙚/𝙘𝙝𝙖𝙥𝙩𝙚𝙧1/ 𝙞𝙨 𝙚𝙨𝙨𝙚𝙣𝙩𝙞𝙖𝙡              
  ██                      ██████                      ▓▓                
  ██                        ▓▓                        ▓▓  𝙏𝙞𝙥: 𝙫𝙖𝙧𝙞𝙖𝙗𝙡𝙚𝙨 𝙖𝙧𝙚 𝙡𝙞𝙠𝙚 𝙗𝙤𝙭𝙚𝙨 𝙮𝙤𝙪 𝙨𝙩𝙤𝙧𝙚 𝙞𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣 𝙙𝙖𝙩𝙖 𝙩𝙮𝙥𝙚𝙨 𝙞𝙣              
  ██                        ▓▓                        ▓▓                
  ██                        ▓▓                        ▓▓  𝙏𝙞𝙥: 𝘾𝙤𝙙𝙞𝙣𝙜 𝙞𝙨 𝙡𝙞𝙠𝙚 𝙖𝙧𝙩 𝙚𝙭𝙥𝙡𝙤𝙧𝙚 𝙮𝙤𝙪𝙧 𝙘𝙤𝙣𝙘𝙚𝙥𝙩𝙨              
  ██                        ▓▓                        ▓▓                
  ██                        ▓▓                        ▓▓  𝙏𝙞𝙥: 𝙙𝙤𝙣𝙩 𝙧𝙪𝙨𝙝 𝙮𝙤𝙪𝙧 𝙘𝙤𝙙𝙚 , 𝙙𝙧𝙤𝙬𝙣 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙘𝙧𝙚𝙖𝙩𝙞𝙤𝙣𝙨              
  ██                      ▓▓▓▓▓▓                      ▓▓                
  ██                  ▓▓▓▓  ▓▓  ▓▓▒▒                  ▓▓  𝙏𝙞𝙥: 𝙞𝙣𝙩𝙚𝙧𝙖𝙘𝙩𝙞𝙫𝙚 𝙨𝙝𝙚𝙡𝙡𝙨 𝙬𝙞𝙡𝙡 𝙤𝙣𝙡𝙮 𝙝𝙖𝙫𝙚 𝙩𝙝𝙚 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 𝙥𝙧𝙤𝙢𝙥𝙩𝙨 >>>              
  ██              ▓▓▒▒      ▓▓      ▓▓▓▓              ▓▓                
  ██          ▓▓▓▓          ▓▓          ▓▓▓▓          ▓▓  𝙏𝙞𝙥: 𝙜𝙞𝙩𝙝𝙪𝙗 𝙞𝙨 𝙜𝙧𝙚𝙖𝙩 𝙩𝙤 𝙨𝙖𝙫𝙚 𝙮𝙤𝙪𝙧 𝙧𝙚𝙥𝙤𝙨𝙞𝙩𝙤𝙧𝙞𝙚𝙨 𝙖𝙣𝙙 𝙨𝙝𝙖𝙧𝙚 𝙘𝙤𝙙𝙚              
  ██      ▒▒▒▒░░░░          ▓▓            ░░▒▒▒▒      ▓▓                
  ██  ▒▒▒▒░░░░              ▓▓              ░░░░▒▒▒▒  ▓▓  𝙏𝙞𝙥: 𝙘𝙝𝙚𝙘𝙠 𝙤𝙪𝙩 𝙜𝙞𝙧 𝙤𝙣 𝙜𝙞𝙩𝙝𝙪𝙗 𝙝𝙩𝙩𝙥𝙨://𝙜𝙞𝙩𝙝𝙪𝙗.𝙘𝙤𝙢/𝙂𝙚𝙣𝙚𝙨𝙞𝙨𝙂𝙞𝙧              
  ████                      ▓▓                      ██▓▓                
      ████                  ▓▓                  ████                            
          ▓▓▓▓              ▓▓              ▓▓▓▓                                        
              ▓▓▓▓          ▓▓          ▓▓▓▓                                                  
                  ▓▓▓▓      ▓▓      ▓▓▓▓                                                                
                      ▓▓▓▓  ▓▓  ▓▓▓▓                                                                           
                          ▓▓▓▓▓▓                                                                                        


"""  
input() # Once user press key the program will progress to next section of code
print('The organization now knows your name is '+name) # Letting the user know their name
print('((press [ENTER] to continue)') # Telling user to continue using the print function
input() # Using the input() function as a continue button
print('The Organization was fed that your hobbies are '+hobby) # Combining the print function and a variable
print('((Press [ENTER] to continue)') # Lets the user know to progress using print
input() # We used the input() function here to let the user know its okay to continue
print('The Organization now know that one day you want to '+goals+' at some point in your life.')
print('((Press [ENTER] to continue])') # Telling user to opress any key to progress
input() # Using the input() function as a menu to continue to next line
print() # Empty line to create space between lines 
print('Thank you for Playing! Created by Genesis Gir') # Thanking the user
print('(Press [ENTER] to exit)') # A little menu letting the user know to press any key to end program
input() # Once user presses key program will close.
