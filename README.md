# SpotifyTop100
Gets Top 100 songs for a user-specified year-month-day, and builds a Spotify playlist.

This python script prompts the user to input the YYYY-MM-DD that would be used to generate a billboard link (https://www.billboard.com/charts/hot-100/{YYYY-MM-DD}). This link will be used with GET method with requests module to retrieve the raw HTML. Latter, the BeautifulSoup module is used to scrape the artist name and song name that would be stored in a song dictionary.

![Alt text](/spotify-top100-playlist-by-date/doc_images/Stage-1.jpg?raw=true "Step 1")

