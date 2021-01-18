import os


def isBinod(filename):
    with open(filename, "r") as f:
        gupta = f.read()
    if "binod" in gupta.lower():
        return True
    else:
        return False


if __name__ == "__main__":
    # Listing the directory
    pappu = os.listdir()
    binodd=0
# Checking the Binod from .txt file
    for item in pappu:
        if item.endswith("txt"):
            print(f" Detecting Binod in {item}...")
            num = isBinod(item)
            if(num):
                print(f"Binod is encountered in given {item} file.")
                binodd +=1
            else:
                print(f"Binod is not encountered in given {item} file.")

    print("******Binod Summary is:******")
    print(f"{binodd} times Binod is Found Overall in all files")        
