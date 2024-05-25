import requests
import json

print("Welcome to the Book of Mormon Summary Tool!")
while True:
    book = input("Which book of the Book of Mormon would you like? ")
    chapter = int(input("Which chapter of %s are you interested in?" % book))
    print("Summary of %s chapter %s:" %(book,chapter))
    base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/%s/%s' %(book,chapter)
    content = requests.get(base_url)
    data = content.json()

    print(data['chapter']['summary'])
    print(" ")
    another = input("Would you like to view another (Y/N)? ")

    if another == 'y' or another == 'Y':
      break
    elif another == 'n' or another == 'N':
      print("Thank you for using Book of Mormon Summary Tool!")
    else:
      print("Invalid input")
