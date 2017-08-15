def begin_story():
	user_response = 0
	print("you start your day at your home.")
	user_response = int(input("1.wake up\n2.Go back to sleep\n3.lie in bed"))
	decision1(user_response)
	
def decision1(user_response):
	if user_response == 1:
		print("1. After waking up, What do you do next?")
		user_response = int(input("1.Eat breakfast\n2.Watch the news\n3.Take a shower"))
		decision1_1(user_response)
	elif user_response == 2:
		print("2. After sleeping a while, What do you do next?")
		user_response = int(input("1.Go back to sleep\n2.Go get ready\n3. look out the window"))
		decision1_2(user_response)
	elif user_response == 3:
		print("3. After lying in bed, What do you do next?")
		user_response = int(input("1.Get ready\n2. Look at your phone"))
		decision1_3(user_response)
	
def decision1_1(user_response):
	if user_response == 1:
		print("while you eat breakfast you hear a knock on the door")
		user_response = int(input("1.answer the door\n2.conutine to eat\n3.get ready to leave to work"))
		decision1_1_1(user_response)
	elif user_response == 2:
		print("You turn on the news and see something horrible (people attacking other people)")
		user_response = int(input("1.keep watching\n2.turn it off"))
		decision1_1_2(user_response)
	elif user_response == 3:
		print("you enter the shower as you do you hear a thumping noise outside")
		user_response = int(input("1.get in the shower\n2. answer the door"))
		decision1_1_3(user_response)

def decision1_2(user_response):
	if user_response == 1:
		print("After sleeping, you never wanted to get out of bed so you keep sleeping forever") #End
	elif user_response == 2:
		print("You got ready to head to work, do you do anything before you leave?")
		user_response = int(input("1.no\n2.yes"))
		decision1_2_2(user_response)
	elif user_response == 3:
		print("You look out thw window and see smoke in the distance")
		user_response = int(input("1.look at your phone\n2.watch the news"))
		decision1_2_3(user_response)

def decision1_3(user_response):
	if user_response == 1:
		print("you got dressed and ready to head out")
		user_response = int(input("1. Go outside"))
		decision1_3_1(user_response)
	elif user_response == 2:
		print("You see your phone with missed calls for your family")
		user_response = int(input("1.call your family"))
		decision1_3_2(user_response)
	
def decision1_1_1(user_response):
	if user_response == 1:
	  print("When you answered the door you died without knowing what happened")
	elif user_response == 2:
		print("You conutined to eat breakfast but the door keep knocking")
		user_response = int(input("1.answer door\n2.get a weapon"))
		decision1_1_1_1(user_response)
	elif user_response == 3:
		print("You are ready to leave to work")
		user_response = int(input("1.leave"))
		decision1_1_1_2(user_response)		

def decision1_1_2(user_response):
	if user_response == 1:
	  print("You leave the house without watching the news and die")
	elif user_response == 2:
		print("You conutine to watch and realize that they are zombies")
		user_response = int(input("1.answer door\n2.get a weapon"))
		decision1_1_2_2(user_response)
		
def	decision1_1_3(user_response):
  if user_response == 1:
    print("tbc")
		
#This runs the game
user_name = input("Enter your name")
begin_story()
