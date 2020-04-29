##
#  This program processes a file containing a count followed by data values.
#  If the file doesn't exist or the format is incorrect, you can specify another file.
#

import re

def main() :
   done = False
   while not done :
      try :
         filename = input("Please enter the file name: ")
         data = readFile(filename)

         # As an example for processing the data, we compute the sum.
         total = 0
         for value in data :
            total = total + value

         print("The sum is", total)
         done = True

         if not filename.endswith(".txt"):                                  ##### Checks to make sure the file is .txt
             raise ValueError()                             ##### Throws an exception if the file is in a wrong format

      except IOError :                                                      ##### Checks if a FileNotFoundError raises
         print("Error: file not found.")

      except ValueError :
         print("Error: wrong file format.")

      except RuntimeError as error :
         print("Error:", str(error))

## Opens a file and reads a data set.
#  @param filename the name of the file holding the data
#  @return a list containing the data in the file
#
def readFile(filename) :
   with open(filename, "r") as inFile:
      return readData(inFile)

## Reads a data set.
#  @param inFile the input file containing the data
#  @return the data set in a list
#
def readData(inFile) :
   data = []
   for line in inFile:
        value = re.sub(r'[^0-9]', '', str(line))                            ##### Removes all non-numbers from the file
        value = int(value)        # May raise a ValueError exception.
        data.append(value)

   # Make sure there are no more values in the file.
   line = inFile.readline()
   if line != "" :
      raise RuntimeError("End of file expected.")
   return data

# Start the program.
main()
