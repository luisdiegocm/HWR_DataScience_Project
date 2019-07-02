## Code to convert pdfs to text

# Import Os to get to the root directory
import os
import sys

# Root directory of the project
ROOT_DIR = os.path.abspath("../")
sys.path.append(ROOT_DIR)

WHITE_PAPER_DIR = os.path.join(ROOT_DIR, "white-papers")

TXT_DIR = os.path.join(ROOT_DIR, "white-papers")

# Import own functions
from libraries import corpus
from libraries import pdf2text

# Import other libraries
from tika import parser
import io



def get_dataset(path = WHITE_PAPER_DIR):
    """
        Function that iterates over all the White Paper files, and return a dictionary with all the files and its text.
        Input:
        
        Output:
            dataset - dictionary with all the files and its text
    
    """
    dataset = {} #define the dataset dictionary
    for file in os.listdir(path): #iterating over all the files in the directory
        filename = os.fsdecode(file)
        if(filename!="unranked"):
            filename = filename.lower().replace(" ","")
            parsed = parser.from_file(os.path.join(path, str(filename))) #parsing the texts within the file
            if ('content' in list(parsed.keys())):
                text = parsed['content'] #putting the parsed text into a variable
                filename = filename.split(".")[0] #splitting the name to remove the .pdf
                dataset[filename] = text #add file to the dictionary
            
    return dataset