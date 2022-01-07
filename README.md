# Tangram

## Assignment Objective:

### Task One

Check that each piece is convex, and if it represents a polygon with n sides (n ≥ 3) then the representation consists
of an enumeration of the n vertices, either clockwise or anticlockwise. 

### Task Two

Check whether the sets of pieces represented in two .xml files are identical, allowing for pieces to
be flipped over horizontally, flipped over vertically, and rotated by 90 degrees. 

### Task Three

Check whether the pieces represented in an .xml file are a solution to a tangram puzzle represented
in another .xml file. 

## Program Design Notes
This was also my first program utilising Object Orientated Programmming Principles, utilising classes to apply all requisite checks to each shape provided in XML format
1. Firstly the available_coloured_pieces function will take each shape and transfer the information provided in XML format to lists and dictionaries so that further analysis and comparison can be applied
2. To check that each shape is convex and a polygon, each shape has the TangramPieces class applied which inherits the same properties as the parent Tangram Shapeclass - the are_valid function is then utilised to check this
3. Each shape is then correspondingly checked against every additional piece in the set to see if they are identicial applied through the are_identical function
4. Finally the has_as_solution function checks whether each of the pieces together fit the solution provided in an additional XML file

## Further Notes
**This was my first 'large' coding assignment completed - Received 11.2 out of 13**
