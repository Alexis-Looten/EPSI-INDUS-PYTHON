from manage_items import *

filePath = "One_Piece.json" #One_Piece.csv

if __name__ == "__main__":
     items = load_file(filePath)
     chosen = extract_10_random_items(items)
     print("Here are 10 random One Piece episodes, enjoy :)")
     pretty_show_items(chosen)
    