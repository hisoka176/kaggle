""" Now that the user can read in a file this creates a model which uses the price, class and gender
Author : AstroDave
Date : 18th September 2012
Revised : 28 March 2014

"""


import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb'))       # Load in the csv file
header = csv_file_object.next()                             # Skip the fist line as it is a header
data=[]                                                     # Create a variable to hold the data

for row in csv_file_object:                 # Skip through each row in the csv file
        data.append(row)                        # adding each row to the data variable
        data = np.array(data)                       # Then convert from a list to an array

        # In order to analyse the price column I need to bin up that data
        # here are my binning parameters, the problem we face is some of the fares are very large
        # So we can either have a lot of bins with nothing in them or we can just lose some
        # information by just considering that anythng over 39 is simply in the last bin.
        # So we add a ceiling
        fare_ceiling = 40
        # then modify the data in the Fare column to = 39, if it is greater or equal to the ceiling
        data[ data[0::,9].astype(np.float) >= fare_ceiling, 9 ] = fare_ceiling - 1.0

        fare_bracket_size = 10
        number_of_price_brackets = fare_ceiling / fare_bracket_size
        number_of_classes = 3                             # I know there were 1st, 2nd and 3rd classes on board.
        number_of_classes = len(np.unique(data[0::,2]))   # But it's better practice to calculate this from the Pclass directly:
                                                          # just take the length of an array of UNIQUE values in column index 2


                                                          # This reference matrix will show the proportion of survivors as a sorted table of
                                                          # gender, class and ticket fare.
                                                          # First initialize it with all zeros
                                                          survival_table = np.zeros([2,number_of_classes,number_of_price_brackets],float)

                                                          # I can now find the stats of all the women and men on board
                                                          for i in xrange(number_of_classes):
                                                                  for j in xrange(number_of_price_brackets):

                                                                              women_only_stats = data[ (data[0::,4] == "female") \
     # If there is no fare then place the price of the ticket according to class
