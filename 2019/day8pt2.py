'''
--- Day 8: Space Image Format ---
--- Part Two ---

Now you're ready to decode the image. The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent.

The layers are rendered with the first layer in front and the last layer in back. So, if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a black pixel at that position.

For example, given an image 2 pixels wide and 2 pixels tall, the image data 0222112222120000 corresponds to the following image layers:

Layer 1: 02
         22

Layer 2: 11
         22

Layer 3: 22
         12

Layer 4: 00
         00
Then, the full image can be found by determining the top visible pixel in each position:


The top-left pixel is black because the top layer is 0.
The top-right pixel is white because the top layer is 2 (transparent), but the second layer is 1.
The bottom-left pixel is white because the top two layers are 2, but the third layer is 1.
The bottom-right pixel is black because the only visible pixel in that position is 0 (from layer 4).
So, the final image looks like this:

01
10

The image you received is 25 pixels wide and 6 pixels tall.

What message is produced after decoding your image?
'''
import time
start_time = time.time()

### read puzzle_input from txt file
with open('./day8_data.txt', 'r') as file:                          # open txt file as raw with name=file
    puzzle_input = file.read()                                      # read content into input variable
    puzzle_input = puzzle_input[:-1]                                # remove empty character at the end

### break the puzzle_input in blocks of 150 (25Wx6H)
layers = [puzzle_input[i:i+150] for i in range(0, len(puzzle_input), 150)]

### convert list of layers to list of tuples of each layer's positions
merged = list(zip(*layers)) # e.g. input: layers=['123','456','789'] => output: merged=[('147'),('258'),('369')]

### determine resultant top layer colors by ignoring/skipping transparent layers (0-black, 1-white, 2-transparent)
top_layer = []                                                      # initialize top_layer variable
for j in range(len(merged)):                                        # loop through each tuple (100 layers)
    for i in range(len(merged[j])):                                 # loop through each value in tuple (150 positions)
        if merged[j][i] == '2':                                     # if a value is 2 (transparent) ...
            continue                                                # ... do nothing, skip to next value
        else:                                                       # otherwise, ... (presume value is 0 or 1)
            top_layer.append(merged[j][i])                          # ... add 0 or 1 to top layer
            break                                                   # quit looping through rest of 100 layers
                                                                    # and move to next of 150 positions
### prepare top_layer data for display/output
display = [top_layer[i:i+25] for i in range(0, len(top_layer), 25)] # create a list of lists for image width (25px)
for k in range(len(display)):                                       # loop through all 6 lists (image height) (6px)
    for i, n in enumerate(display[k]):                              # replace 1s and 0s with different characters
        if n == '0':                                                # if the digit is 0 (black) ...
            display[k][i] = "_"                                     # ... replace it with an underscore
        elif n == '1':                                              # elif the digits is 1 (white) ...
            display[k][i] = "◻️"                                    # ... replace it with an white square

### printout each row of final data
for i in range(len(display)):                                       # loop through list of lists
    print(f"{i}: {display[i]}")                                     # print the list, i.e. the answer
print("Pass! ")
print("The correct answer is CYUAH")

'''
  ◻️◻️    ◻️      ◻️  ◻️    ◻️    ◻️◻️    ◻️    ◻️
◻️    ◻️  ◻️      ◻️  ◻️    ◻️  ◻️    ◻️  ◻️    ◻️
◻️          ◻️  ◻️    ◻️    ◻️  ◻️    ◻️  ◻️◻️◻️◻️
◻️            ◻️      ◻️    ◻️  ◻️◻️◻️◻️  ◻️    ◻️
◻️    ◻️      ◻️      ◻️    ◻️  ◻️    ◻️  ◻️    ◻️
  ◻️◻️        ◻️        ◻️◻️    ◻️    ◻️  ◻️    ◻️
    C          Y          U          A         H
'''

print("--- %s seconds ---" % (time.time() - start_time))
