  # lets us use the csv module to read and write csv files
import lossy_list_example  # comment out this line before adding the csv import!

### =========================================================== ###
###    Lists, CSVs, and making forgetful programs remember      ###
### =========================================================== ###
'''
Lists are great for storing information in a program at runtime:
'''
minecraft_materials = [
    "Oak Plank",
    "Stick"
]
'''
But if a user adds things to the list either by input or programmatically, these items are lost when the program shuts down. 

STEP 0: Run the example code
============================

***Try running this program now***. 

Add 3 materials to the list (if you don't know any Minecraft materials, copy this url into a new tab on your browser:  https://game8.co/games/Minecraft/archives/377743 for some ideas):
'''


'''Take note of the list that prints out after you enter your favorite materials.

Next, run the program again, but this time just read the list that prints out, then press the Stop button. What did you notice in the list that printed?

The list reset to the original list and only had Oak Plank and Stick in it! All the data you entered was lost because our program doesn't include persistent storage -- meaning we can't save our data and we've broken the first rule of programming: be lazy and type less! Let's change that.

INTRODUCING CSV

CSV stands for Comma Separated Values. A CSV file is a text file that is often made from a spreadsheet. We can create one without Excel or Sheets, right here in Replit!

STEP 1: Set up your CSV file
============================

If it isn't open, click your Explorer icon (upper left corner, looks like two pieces of paper) so that you see the Open Editors list.

A CSV file is just a text file, so we can create one very easily in VS Code. Go to the File menu and choose New Text File (or type Command-N). Go to the File menu again and choose Save (or press Command-S) to save the file. When prompted, name the file: materials.csv

Drag this tab over to the left where the line numbers are (you'll see the left half of the window light up). This rearranges your window so you can read this text while entering some values in your new CSV file. Close the Explorer by clicking the icon with 2 pages on the left if you need more room.

Type or copy the following into your CSV file, making sure to leave a blank line at the end:

material,color
Oak Plank, brown
Stick, brown
Diamond,turquoise
Wheat,yellow
Brick,red
Coal,black


The first row of our data is a header row. It tells us how the data in the columns is categorized. This data can be represented like this:
+-----------+-------------------+
| material  | color             |  This is our header row
+-----------+-------------------+
| Oak Stick | brown             |
+-----------+-------------------+
| Stick     | brown             |
+-----------+-------------------+
| Diamond   | turquoise         |
+-----------+-------------------+
| Wheat     | yellow            |
+-----------+-------------------+
| Brick     | red               |
+-----------+-------------------+
| Coal      | black             |
+-----------+-------------------+
(blank line at end)

We load the data using the csv module. A module is a package of code that someone made that we can use in our programs. The csv module comes with Python. There are many, many other modules you can install and import, too. 

STEP 2: Reading data with the csv module
========================================

Type this at the top of this file on the first line, above everything else:

import csv  # lets us use the csv module to read and write csv files

Next, comment out line 2 (import lossy_list_example) -- this will allow the program to move on to the next step.

Next, we need to create a context manager. A context manager handles file management: it opens the file for reading and closes the file when the data has been read in. It's important to remember to close files after you use them so other programs can access them. Python doesn't do this by default, so we use a context manager to open and close the file for us automatically. Read through the code below before running the program again.
'''

from pprint import pprint  # prints data structures in a more human-readable format

# flags to keep the next step from running before we get to it!
ok_next_step = False  
ok_final_step = False
data = []  # create a new, empty list to put our data in
with open("materials.csv", mode="r") as file_reader:
    csv_reader = csv.DictReader(file_reader)  
    '''
    to store the row in our data list, we'll use a list
    comprehension. These work like a for loop. In fact, the 
    list comprehension below this comment is equivalent to the
    following code:

    for row in csv_reader:
        data.append(row)

    List comprehensions have a very specific syntax:
    [expression for item in iterable if condition]

    'expression' is the outcome of each iteration if the condition is True. The 'if condition' part is optional.

    list comprehensions are one way to flex your python coding
    skills because they are more "pythonic" -- meaning you are
    using the tools Python gives you both elegantly and 
    efficiently! Pythonic code is a goal of most Python coders.
    
    '''
    data = [row for row in csv_reader]
    # the above reads as "for each row in csv_reader, store it in data"
    
'''
Now that we have the data stored in a dictionary, we leave the context manager's code block by un-indenting the next code line (notice the line is all the way to the left. That's an un-indent):
'''
pprint(data)  # prints our data in a more human-readable format

'''
Run the program, noticing that the data that is read in matches the data in your materials.csv file. Then, come back here to continue.

STEP 3: Writing data with the csv module
========================================

Welcome back!

So now we have loaded the data, but how do we add to it and finally store it so we can use it later? First, we need to get some new data. Uncomment the line below and then read through this code. 
'''
# ok_next_step = True
if ok_next_step:
    print("Press Enter on a blank line to stop inputting data.\n")
     # this block of code will only run if ok_next_step is True.

    while True: # just keep doing this forever, we will handle the break condition in the loop
        new_row = {}  # initialize a new dictionary to add to data
        new_row["material"] = input("Material: ").title()
        if new_row["material"] == "":
            break
        new_row["color"] = input("Color: ").lower()
        if new_row["color"] == "":
            break
        data.append(new_row)
        
        
    print()
    print("Here is the new data: \n")
    pprint(data)
    
'''
Run the program and come back here.

Welcome back! The data you just added won't show up the next time you run the program. Bummer! To save that data we need to write it to a file. Since we have a full copy of the data that was in the csv file, we will write all the data back to the csv file. 

First, let's make a backup of our csv file, just in case we make a mistake. Hover your mouse over 'materials.csv' in the Files Sidebar and click the 3 dots icon on the right, then click 'Duplicate file'. A copy of your csv file will be made. This is our backup.

Uncomment the next line, then read through this code.
'''
ok_final_step = True

if ok_final_step:
    with open("materials.csv", mode="w") as file_writer:
        fieldnames = ["material", "color"]
        # when writing the file we have to provide DictWriter the fieldnames
        csv_writer = csv.DictWriter(file_writer, fieldnames=fieldnames)
        csv_writer.writeheader()  # writes the header row to the file
    
        '''
        Remember the list comprehension we used when we read the file into our list? We can use a list comprehension to write to the file, too! This one does the same thing as these lines of code -- but looks cooler and is more pythonic:
    
        for row in data:
            # csv_writer.writerow(row)
        
        '''
        # this line writes each row to the csv file
        [csv_writer.writerow(row) for row in data]
    
    '''
    Run the program, and come back here.

    
    Welcome back! Check the csv file (materials.csv) to see your file changes! Run this program again and notice that the lines you added are read in and printed out! Feel free to use this code as inspiration for your projects!
    '''