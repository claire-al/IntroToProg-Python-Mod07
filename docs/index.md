# Pickling and Error Handling
*Claire Lynch, 12.1.2020*

## Introduction
This week, I learned about pickling, a concept I am entirely unfamiliar with. 
I also went further into understanding Exception/Error handling, and how to deal 
with them when they arise. Unlike previous weeks, this week focused on doing my 
own research on Exceptions and Pickling and applying this knowledge to my script to show how they work.

##Pickling and Unpickling
Pickling is a process that converts any sort of Python object, such a list or dictionary,
into byte streams (0’s and 1’s). Files that have been pickled are not able to easily be 
read, and instead have to be unpickled for people to be able to read and understand what 
is in them. Pickling can be useful as it can reduce file size and allow for quicker 
transfer of files and data.

###Useful Links about Pickling:

https://www.tutorialspoint.com/python-pickling
This link was most useful for me, as I thought it did the best job of explaining pickling and unpickling in simple terms. It had easy-to-follow and understand examples that I was able to use to help me build my own scripts. It also listed some pickling exceptions I might encounter, which was helpful to include in this script.
https://www.geeksforgeeks.org/understanding-python-pickling-example/
I liked this webpage as the pickling example included two different dictionaries, with each dictionary describing characteristics about one person. Despite the slightly more complicated example, I was able to understand what was going on, and applied some elements of this script example they had to my own code.
https://stackoverflow.com/questions/7501947/understanding-pickling-in-python
I liked looking at this link as it helped explain pickling and unpickling, but the examples were a little further in-depth than other ones I’ve seen. I found it helpful to look at a variety of examples and make sure I understood the script to ensure I know how pickling works.

```
    def save_data_to_file(file_name, list_of_data):
        # ----Pickling------------------------------#
        try:
            with open(theFile, "wb") as file:
                pickle.dump(albumArtistDictionary, file)
            file.close()
        except:  # Pickle.PicklingError, if the pickle object doesn't support pickling
            print("There is an issue pickling your dictionary!")
            
```



