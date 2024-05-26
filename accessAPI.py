import requests
import json

print("Welcome to the Book of Mormon Summary Tool!")
import requests

print("Welcome to the Book of Mormon Summary Tool!")
while True:
    book = input("Which book of the Book of Mormon would you like? ")
    chapter_str = input("Which chapter of %s are you interested in?" % book)
    
    try:
        chapter = int(chapter_str)
    except ValueError:
        print("Please enter a valid chapter number.")
        continue

    base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/%s/%s' % (book, chapter)
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        if 'chapter' in data and 'summary' in data['chapter']:
            print("Summary of %s chapter %s:" % (book, chapter))
            print(data['chapter']['summary'])
        else:
            print("Summary not found for %s chapter %s." % (book, chapter))
    else:
        print("Failed to retrieve data for %s chapter %s. Status code: %d" % (book, chapter, response.status_code))

    print(" ")
    another = input("Would you like to view another (Y/N)? ")

    if another.lower() != 'y':
        print("Thank you for using Book of Mormon Summary Tool!")
        break

