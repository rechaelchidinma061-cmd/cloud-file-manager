import s3_manager

print("s3 manager conected!")
print("welcome to chidinma's cloud file manager!")

while True:
    print()
    print("1. create a file")
    print("2. view files")
    print("3. delete a file")
    print("4. download a file from s3")
    print("5. exit")

    choice = input("choose an option: ")

    if choice == "1":
        filename = input("Enter the file name: ")

        with open(filename, "w") as file:
            file.write("This file was created by chidinma's cloud file manager.")

        print("file created successfully!")    

        s3_manager.upload_file(filename)

    elif choice == "2":
        print("files stored in Amazon s3:")
        s3_manager.list_files()

    elif choice == "3":
        filename = input("Enter the file name to delete: ")

        s3_manager.delete_file(filename) 

    elif choice == "4":
        filename = input("Enter the s3 file name to download: ")

        s3_manager.download_file(filename)  

    elif choice == "5":
        print("Invalid option. please choose a number from 1 to 5.")

