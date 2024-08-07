import os
import time as t
delay=1

base_path = os.path.join(os.getcwd(), "File management app")
if not os.path.exists(base_path):
    os.makedirs(base_path)

def create_file(fileName):
    try:
        with open(os.path.join(base_path,fileName),"x"):
            print(f"\tFile name {fileName} successfully created.")
    except FileExistsError:
        print(f"\tFile name {fileName} already exists.")
    except Exception as e:
        print("\tAn error occurred.")
    
def view_all_files():
        
    files=os.listdir(base_path)

    if not files:
        print("\tNo file found!")
    else:
        print("Files in directory are : ")
        for file in files:
            print(f"\t{file}")

def delete_file(fileName):
    try:
        os.remove(os.path.join(base_path,fileName))
        print(f"\t{fileName} has been successfully deleted.")
    except FileNotFoundError:
        print("\tFile not found!")
    except Exception as e:
        print("Error!")

def read_file(fileName):
    try:
        with open(os.path.join(base_path,fileName),"r") as f:
            content=f.read()
            print(f"Contents of {fileName} are : \n\t{content}")
    except FileNotFoundError:
        print(f"\t{fileName} doesn't exists!")
    except Exception as e:
        print("\tAn error occurred!")

def edit_file(fileName):
    try:
        with open(os.path.join(base_path,fileName),"a") as f:
            content=input("Enter data to add : ")
            f.write(content+"\n")
            print(f"\tNew data added to {fileName} successfully.")

    except FileNotFoundError:
        print(f"\t{fileName} doesn't exists!")
    except Exception as e:
        print("\tAn error occurred!")


def main():
    while(True):
        print("File Management APP")
        print("\t1: Create file")
        print("\t2: View all files")
        print("\t3:Delete file")
        print("\t4: Read file")
        print("\t5: Edit file")
        print("\t6: Exit")

        t.sleep(delay)

        choice=int(input("Enter your choice : "))
        if(choice==1):
            fileName=input("Enter file name to create : ")
            create_file(fileName)
        elif(choice==2):
            view_all_files()
        elif(choice==3):
            fileName=input("Enter file name to delete : ")
            delete_file(fileName)
        elif(choice==4):
            fileName=input("Enter file name to read file : ")
            read_file(fileName)
        elif(choice==5):
            fileName=input("Enter file name to edit file : ")
            edit_file(fileName)
        if(choice==6):
            break
        t.sleep(delay)

if __name__=="__main__":
    main()


