# display_panel = [None] * 40 <-- debug
display_panel = [" "] * 40

def main():
	inputString = input("Enter a string of 40 characters: ")
	if len(inputString) > 40 or len(inputString) == 0:
		print("Error: String too long or too short!")
		return
	
	# determine "buffer" by taking the difference b/w input length and
	# 40 chars (display_panel length) and dividing it by two, one half for
	# the front and the other for the end for a "centered" position, rounding
	# down with int division for odd-count input string lengths
	spaceBuffer = (40 - len(inputString))//2
	
	# iterate starting at start buffer position
	counter = 0
	for index in range(spaceBuffer, spaceBuffer + len(inputString)):
		display_panel[index] = inputString[counter]
		counter += 1

	# print("/{}/".format("".join(str(display_panel)))) <-- debug
	print("/{}/".format("".join(display_panel)))
	

# Call function / run
main()