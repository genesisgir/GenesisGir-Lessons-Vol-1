""" 
█▀▀ █▀▀ █▄░█ █▀▀ █▀ █ █▀   █░░ █▀▀ █▀ █▀ █▀█ █▄░█ █▀   █░█ █▀█ █░░ ░ ▄█
█▄█ ██▄ █░▀█ ██▄ ▄█ █ ▄█   █▄▄ ██▄ ▄█ ▄█ █▄█ █░▀█ ▄█   ▀▄▀ █▄█ █▄▄ ▄ ░█ 
Welcome to the genesis gir lesson tutorials Volume 1! We start of the lessons with
you getting to know me! This program tells you more about me and who I am and is more like 
a cool story line about me make sure to pay attention to the functions used and the variables
how they are approached. Thanks for downloading~ 
⼕ㄖᗪ🝗ᗪ & 山尺讠セセ🝗𝓝 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂 Ꮆ讠尺
"""
"""
█░░█ █▀▀█ █░░░█ 　 ▀▀█▀▀ █▀▀█ 　 █▀▀ █▀▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀ 
█▀▀█ █░░█ █▄█▄█ 　 ░░█░░ █░░█ 　 █░░ █░░█ █░▀░█ █░▀░█ █▀▀ █░░█ ░░█░░ ✎
▀░░▀ ▀▀▀▀ ░▀░▀░ 　 ░░▀░░ ▀▀▀▀ 　 ▀▀▀ ▀▀▀▀ ▀░░░▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░
First things first you need to learn how to make single line comments and multi line comments 
so you can add little reminders or give insight on what that line of code does! comments are
fun great ways to just add notes to a line so you can reflect on them later , They wont show
up in the program its specifically for the developer(you) to look at! So Single line comments
star with a hashtag (#) and anything after that will be comments in a greyish tone. Great! now
you know how to make single line comments but what about multi line comments like this one bro?
Easy all you need to do is start the line with (3 quotes) and than anything after that will be 
comments and to end the finish off the line with another 3 quotes and viola! your welcome I know 
im awesome no need to thank me! (─‿‿─)
"""
#This program is about a creepy interviewer that asks you questions beyond the scope!
#The functions and methods on how it was made will be explained at the end of the code
# functions , variables mostly enjoy the code Thanks for downloading!
"""
█▀▄▀█ █▀█ ░ █ █▄░█ ▀█▀ █▀▀ █▀█ █░█ █ █▀▀ █░█░█ █▀▀ █▀█
█░▀░█ █▀▄ ▄ █ █░▀█ ░█░ ██▄ █▀▄ ▀▄▀ █ ██▄ ▀▄▀▄▀ ██▄ █▀▄
"""
print('The door opens and a man in a suit walks threw.')#using the print function to print values onto the screen
""" The print function is used to print the values in the containers onto the stream(screen)
and in this case to generate text to the program. Its pretty useful and I first start off by
thinking what i want the program to be about and use creative little ideas to conjure up plots
in this case I chose to make a program that interviews you that being Mr.interviewer that asks
you random questions with a creepy horror type scence set to it!
"""
print()# using the print() to create a space between the lines of code you can do this by typing print() into the line
print('hes wearing a black suit and red tie but his face is strangely blank and white')#using print function to type more values onto screen
"""
█░█ █▀█ █░█░█   ▀█▀ █▀█   █░█ █▀ █▀▀   █▀█ █▀█ █ █▄░█ ▀█▀
█▀█ █▄█ ▀▄▀▄▀   ░█░ █▄█   █▄█ ▄█ ██▄   █▀▀ █▀▄ █ █░▀█ ░█░
The print function always comes with two parentheses and any function in that matter and we 
enter what data types we want inside of them and everything inside of it is called an
argument and the print is called a function and in this case im using a (stir) or better known
as a string to make a storyline! so print(    ) and anything inside it will be printed onto 
stream(screen) just make sure its a correct data type: interger , float or a string value.
""" 
print('He sits down at your table as you both are surrounded by white walls')#using print 
print('in a errie bright white room.')# letting the user know what setting they are in!
print('The room gets colder and colder and he begins to stare at you and utters the words.')
#line 32 By saying the room gets colder we let the user know its horror themed.
print()# an empty line of text using the print() function!
print('Mr.Interviewer: Whats your name sir?')#asking the user their name. using print 
name=input()# by entering input() we let the users intake become the variable
#The """ create a multi line comment as you can see below to create multiple lines of comments
#very useful if you need to leave larger comments but make sure to end it with another """ on the bottom
"""
█░█ █▀█ █░█░█   ▀█▀ █▀█   █░█ █▀ █▀▀   █ █▄░█ █▀█ █░█ ▀█▀
█▀█ █▄█ ▀▄▀▄▀   ░█░ █▄█   █▄█ ▄█ ██▄   █ █░▀█ █▀▀ █▄█ ░█░
input() waits for the users keyboard input and when they press enter it takes that input
this can be very essential to make variables by the user and can be used to your advantage
make sure to pratice input() often! and in line 33 im using the input() function
to create a variable using the users input to later use it in the program
"""
print()# empty line of text created using the print() function to put spaces between lines
print('Mr.interviewer:Okay '+name+' Im going to be asking you some Q&A.')#using the print again to print values
print()# an empty void of line
print('Mr.Interviewer:Whats your favorite thing to do currently?. . .')#asking them whats their hobby is
hobby=input() # creating the hobby variable from users input
print()# using the print function to create a empty line
print(' Mr.Interviewer:'+hobby+' Seems pointless you should invest in giving me your data.')
print()#empty line
print('Mr.interviewer:What are your goals in life if any?. . .')#asking user for goals
goals=input()# using the input() to create the goals variable by users intake
print()#empty line
print('The room gets colder. . .')# more story line to add character to the program using print('enter text here')
print()#empty line
print('Mr.interviewer:These goals must be important to you '+name+'.')
"""

█▀▀ █ █░█ █ █▄░█ █▀▀   █▀▀ █░█ ▄▀█ █▀█ ▄▀█ █▀▀ ▀█▀ █▀▀ █▀█
█▄█ █ ▀▄▀ █ █░▀█ █▄█   █▄▄ █▀█ █▀█ █▀▄ █▀█ █▄▄ ░█░ ██▄ █▀▄
Notice on how we are brining life to the character by making him ask redimentary questions
giving the feel that you are connected with mr.interviewer and giving a sense of personality
very important to be creative during the writing process. Choose a personality for your character!
which is the fun part you can create all type of personalities using your brain meat. Is the
character a mean or fancy type? or maybe they are cute and friendly? Roleplay and imagination
is really important as well but its all entirely up to you
                     
░░░░░░░▄█▄▄▄█▄
▄▀░░░░▄▌─▄─▄─▐▄░░░░▀▄  print('Mr.Roboto:Hello Twitch!')  
█▄▄█░░▀▌─▀─▀─▐▀░░█▄▄█  print('Mr.Roboto: Follow genesis @ https://www.twitch.tv/cashbunny2k ')
░▐▌░░░░▀▀███▀▀░░░░▐▌   
████░▄█████████▄░████  𝙏𝙞𝙥: 𝙎𝙩𝙖𝙮 𝙝𝙮𝙙𝙧𝙖𝙩𝙚𝙙 𝙖𝙣𝙙 𝙙𝙧𝙞𝙣𝙠 𝙥𝙡𝙚𝙣𝙩𝙮 𝙤𝙛 𝙬𝙖𝙩𝙚𝙧 𝙬𝙝𝙞𝙡𝙚 𝙘𝙤𝙙𝙞𝙣𝙜                  

"""
#The program continues here
print()#empty line using the print() function to create space for other lines to breathe
print('Mr.inteviwer:Are you scared to be poor?. . .')#asking the user a question
fearofpoverty=input()#fearofpoverty is the variable and the input from the user makes it
print()#yay another empty line
print('Mr.interviewer:Thats understandable. . .')#talking to the user even more using print
print()#more empty space
print('Mr.interviewer:i believe you know more than your telling me.')# we make the character agitated
print('(respond to Mr.interviewer than press [ENTER])')##here we are letting user know to reply to the character
reply=input()#reply is the variable thati used to later on use to my benefit
print('-You lean in onto the table and say to Mr.interviewer '+reply+'-')# using the print + variable to make sentences
print()#empty line using the print() function , type print() to use this feature
print('Mr.interviewer:I know so many things about you Ive been watching you for the past')#character small talk using print function
print('3 days and I know where you sleep , eat , and spend time with family.')#more small talk
print('(tell him how you feel about invading your privacy)')
reply=input()#creating the avriable with the user input using the input() function!
print('-Your face shocked and angry at the same time you say '+reply+'-')#roleplaying with variables+print
print()#using print() to create space
print('mr.interviewer: Dont waste my time '+name+' Im accociated with a organization to study')#driving storyline and adding a variable of the users name 
print('you and gather information about you and this bullshitting is getting us nowhere.')#more story line speech with the print function
print('(respond to Mr.interviewer than press [ENTER])')#asking the user to respond to mr.interviewer
reply=input()#the input function takes input from user and overwrites the old variable
print()#empty line of text! using the print() function
print('You look around the white room and cross your arms and say '+reply+'-')
print()#oh look another empty line using the print() fucntion
print('Mr.interviewer walks out the room and gathers his paper work')#i used the print function to print values to stream(screen)
print('he closes the door behind him and the room goes dark.')#i used print function to print stir values to stream.
print('((press [ENTER] to continue)')#letting the user know to progress
"""
▀█░█▀ █▀▀█ █▀▀█ ░▀░ █▀▀█ █▀▀▄ █░░ █▀▀ █▀▀ 
░█▄█░ █▄▄█ █▄▄▀ ▀█▀ █▄▄█ █▀▀▄ █░░ █▀▀ ▀▀█ 
░░▀░░ ▀░░▀ ▀░▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀▀▀ ▀▀▀
Variables are like little tiny safes or cardboard boxes that you can label! In them you can
insert data types from intergers , strings(stirs) ,floating-points and values to later use
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
  ██                  ▓▓▓▓      ▓▓▒▒                  ▓▓  𝙏𝙞𝙥: 𝙝𝙩𝙩𝙥𝙨://𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙚𝙩𝙝𝙚𝙗𝙤𝙧𝙞𝙣𝙜𝙨𝙩𝙪𝙛𝙛.𝙘𝙤𝙢/2𝙚/𝙘𝙝𝙖𝙥𝙩𝙚𝙧1/ 𝙞𝙨 𝙚𝙨𝙨𝙚𝙣𝙩𝙞𝙖𝙡              
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
input()# once user press key the program will progress to next section of code
print('The organization now knows your name is '+name)#letting the user know their name
print('((press [ENTER] to continue)')#telling user to continue using the print function
input()#using the input() function as a continue button
print('The Organization was fed that your hobbies are '+hobby)#combining the print function and a variable
print('((press [ENTER] to continue)')#lets the user know to progress using print
input()#we used the input() function here to let the user know its okay to continue
print('The Organization now know that one day you want to '+goals+' at some point in your life.')
print('((press [ENTER] to continue])')# telling user to opress any key to progress
input()#using the input() function as a menu to continue to next line
print()#empty line to create space between lines 
print('Thank you for Playing! created by genesis gir')# Thanking the user
print('(press [ENTER] to exit)')#a little menu letting the user know to press any key to end program
input()#once user presses key program will close.