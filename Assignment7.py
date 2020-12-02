# ------------------------------------------------- #
# Title: Lab7-1
# Description: An example of pickling/unpickling a
# dictionary of songs and artists, with try/exception
# error handling.
# ChangeLog: (Who, When, What)
# CLynch,12.1.2020,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
# Declare variables and constants
theFile = 'AppData.dat'
albumArtistDictionary = {"Folklore":"Taylor Swift", "Melodrama":"Lorde", "Punisher":"Phoebe Bridgers",
                         "Brothers in Arms":"Dire Straits"}

# Processing -------------------------------------- #
class Processor:
    def save_data_to_file(file_name, list_of_data):
        # ----Pickling------------------------------#
        try:
            with open(theFile, "wb") as file:
                pickle.dump(albumArtistDictionary, file)
            file.close()
        except:  # Pickle.PicklingError, if the pickle object doesn't support pickling
            print("There is an issue pickling your dictionary!")

    def read_data_from_file(file_name):
        # ----Unpickling----------------------------#
        try:
            with open(theFile, "rb") as pickle_off:
                print(pickle.load(pickle_off))
            pickle_off.close()
        except:  # Pickle.UnpicklingError, if the file contains bad or corrupted data
            print("There is an issue unpickling the data!")


# Main -------------------------------------------- #
while(True):

    strChoice = str(input("Please choose to Pickle (1), Unpickle (2), or Exit (3): "))
    if strChoice.strip() == '1': #input data
        Processor.save_data_to_file(theFile, albumArtistDictionary)
        print("Pickling the song and artist dictionary!")

    elif strChoice.strip() == '2': #Pickle
        Processor.read_data_from_file(theFile)

    elif strChoice.strip() == '3': #Unpickle
        print("Goodbye!")
        break

