# reflex game
# created by Sam Scott 10-06-2016
import os, sys, threading, time, random, subprocess

class Game:
	def __init__(self):
		self.pressed = False
		self.seconds = 0

	def wait(self):
		self.seconds = random.randint(3, 13)
		#print("Sleeping for", self.seconds, "seconds...")
		time.sleep(self.seconds)

	def t_blink(self):
		os.system("color 1a")
		#time.sleep(0.1)
		#os.system("color 7")

	def get_input(self):
		self.pressed = False
		input("Press enter when the screen turns blue. ")
		#print("Pressed.")
		self.pressed = True

	def timer(self):
		milliseconds = 0
		while not self.pressed:
			time.sleep(0.001)
			milliseconds += 1
		#print(milliseconds)
		if milliseconds < self.seconds / 1000:
			print("Too early.")
			time.sleep(1)
		else:
			print("Reaction Time: ", milliseconds - (self.seconds / 1000), "ms. ", (milliseconds - (self.seconds / 1000))/1000, " seconds.", sep="")

if __name__ == "__main__":
	if "idlelib.run" in sys.modules:
		subprocess.call(["python", "reflex_game.py"])
	else:
		game = Game()
		while True:
			get_input = threading.Thread(target=game.get_input)
			get_input.start()
			game.wait()
			blink = threading.Thread(target=game.t_blink)
			blink.start()
			timer = threading.Thread(target=game.timer)
			timer.start()
			timer.join()
			input("Press enter to restart...")
			os.system("color 7")
			os.system("cls")



