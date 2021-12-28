# Spotify Top 100!
Gets Top 100 songs for a user-specified year-month-day, and builds a Spotify playlist.

This python script prompts the user to input the YYYY-MM-DD that would be used to generate a billboard link (https://www.billboard.com/charts/hot-100/{YYYY-MM-DD}). This link will be used with GET method with requests module to retrieve the raw HTML. Later the BeautifulSoup module is used to scrape the artist's name and song name that would be stored in a song dictionary.

![Alt text](/doc_images/Stage-1.jpg?raw=true "Step 1")

Spotify API setup for the account is required to retrieve the keys that are used to search for songs URI's using the artist:song dictionary. The script will prompt the user if the song/artist could not be found and will skip to the next one down the list. After the script has gone through the list, a spotify playlist will appear in the account.

![Alt text](/doc_images/Stage-2.jpg?raw=true "Step 2")
