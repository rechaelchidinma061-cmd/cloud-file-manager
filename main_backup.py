import boto3

s3 = boto3.client("s3")

BUCKET_NAME = "chidinma-file-manager-2026-0811"

print("connected to Amazon s3!")


print("welcome to chidinma's cloud file manager!")

while True:
  print()
  print("1. create  a file")
  print("2.  view files")
  print("3. Delete a file")
  print("4. Download file from s3")
  print("5. Exit")

  choice = input("choose an option: ")

  if choice == "1":
      filename =input("Enter the filename:")

      with open(filename, "w") as file:
         file.write("This is a new file created by chidinma's cloud file manager.")

         print("file created successfully.")

         s3.upload_file(filename, BUCKET_NAME, filename)


      reponse = s3.list_objects_v2(Bucket=BUCKET_NAME)

      if "contents" in reponse:
          for items in reponse["contents"]:
              print("-", item["key"])
      else:
          print("your s3 bucket is empty.")

      import os

      files = os.listdir()
      print("Files in your cloud file manager:")

      for file in files:
          print("-", file)

  elif choice == "3":
      filename = input("Enter the filename to delete: ")

      try:
          s3.delete_object(
              Bucket=BUCKET_NAME,
                Key=filename
          )

          print("file deleted from Amazon S3 successfully.")

      except Exception as e:
          print("Error deleting file:", e)

      import os

      filename = input("Enter the filename to delete: ")

      if os.path.exists(filename): 
          os.remove(filename)

          print("file deleted successfully.")
      else:
          print("file not found.")

  elif choice == "4":
      filename = input("Enter the s3 file name to download: ")

      try:
          s3.download_file(BUCKET_NAME, filename, filename)

          print("file downloaded from Amazon S3 successfully.")

      except Exception as e:
          print("Error downloading file:", e)

      except Exception as e:
          print("Error downloading file:", e)

  elif choice == "5":
      print("Goodbye!")
      break

  else:
      print("Invalid choice. Please try again.")