# display_panel = [None] * 40 <-- debug
display_panel = [" "] * 40
doPrint = 0

def main():
	inputString = input("Enter a string of 40 characters: ")
	if len(inputString) > 40 or len(inputString) == 0:
		print("Error: String too long or too short!")
		return
	spaceBuffer = (40 - len(inputString))//2
	
	counter = 0
	for index in range(spaceBuffer, spaceBuffer + len(inputString)):
		display_panel[index] = inputString[counter]
		counter += 1

	# print("/{}/".format("".join(str(display_panel)))) <-- debug
	print("/{}/".format("".join(display_panel)))
	

# Call function / run
while doPrint < 1:
	main()