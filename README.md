This program is aimed to assist game users' experience when playing a 5v5 game (league of legends)


Using pyautogui, it captures image of usernames and detects what team the user is in by using OpenCV.
The user's name is in yellow font whereas other players' names are white.

The program also scans 10 images in which each image contains a name of the
character each of the 10 users are playing.

Using pytesseract, those 10 images are converted to 10 corresponding texts

The name of the character shown in the loading screen may vary although
it is the same character because of the game modifiers.

To solve this, combination of all possible names of a character and its actual name is
scraped from a website using requests and BeautifulSoup. These data is then saved into
a SQLite database under resources folder. Since the game is constantly updating, if
name of a character doesn't exist in the preexisting database, it automatically
adds new additions using the same method.

Using the database now, the program converts the previous 10 names to its actual names.

With these actual names, this program collects useful statistical data from another website.
This is done using Selenium and BeautifulSoup, to scrape from a dynamic website.

Then those obtained data are presented to the user to provide to assist the user.


Used: pyautogui, requests, SQLite, pytesseract, selenium, beautifulsoup, cv2
