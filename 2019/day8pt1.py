'''
--- Day 8: Space Image Format ---

The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars rovers, and so they are curious if you would spend a brief sojourn on Mars. You land your ship near the rover.

When you reach the rover, you discover that it's already in the process of rebooting! It's just waiting for someone to enter a BIOS password. The Elf responsible for the rover takes a picture of the password (your puzzle input) and sends it to you via the Digital Sending Network.

Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding; instead, they're encoded in a special Space Image Format. None of the Elves seem to remember why this is the case. They send you the instructions to decode it.

Images are sent as a series of digits that each represent the color of a single pixel. The digits fill each row of the image left-to-right, then move downward to the next row, filling rows top-to-bottom until every pixel of the image is filled.

Each image actually consists of a series of identically-sized layers that are filled in this way. So, the first digit corresponds to the top-left pixel of the first layer, the second digit corresponds to the pixel to the right of that on the same layer, and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.

For example, given an image 3 pixels wide and 2 pixels tall, the image data 123456789012 corresponds to the following image layers:

Layer 1: 123
         456

Layer 2: 789
         012
The image you received is 25 pixels wide and 6 pixels tall.

To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied by the number of 2 digits?
'''
import time
start_time = time.time()

### read puzzle_input from txt file
with open('./day8_data.txt', 'r') as file:   # open txt file as raw with name=file
    puzzle_input = file.read()               # read content into input variable
    puzzle_input = puzzle_input[:-1]         # remove empty character at the end

### break the puzzle_input in blocks of 150 (25Wx6H)
layers = [puzzle_input[i:i+150] for i in range(0, len(puzzle_input), 150)]

### count 0s in each layer
counts_0s = [layers[i].count('0') for i in range(len(layers))]

### determine layer with fewest zeros (0s)
fewer_0s = min(counts_0s)                    # find lowest value in counts_0s
indexOf_fewer_0s = counts_0s.index(fewer_0s) # get index of lowest count
selected_layer = layers[indexOf_fewer_0s]    # create new list of digits

total = selected_layer.count('1') * selected_layer.count('2') # multiply 1s count and 2s
if total == 2500:
    print("Pass! ")
print(f"Your result is: {total}") # correct answer is '15' for test input & '2500' for puzzle_input

print("--- %s seconds ---" % (time.time() - start_time))
