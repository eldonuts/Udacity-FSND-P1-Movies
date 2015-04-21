# Udacity FSND - Project 1

#### Description
This project was created as part of the Udacity Full Stack Web Developer Nanodegree. It is a static site that is created using python scripts. Youtube and OMDB APIs are used to gather trailer and movie data respectively.

#### How to use
1. Ensure Python 2.7 is installed.
2. Clone the git repo to a local directory
3. Open Python and run **entertainment_center.py**. (Optional: open the file and alter the list of movies to your liking.)
4. Your default browser will open the static html page, enjoy!

#### What does each file do

**entertainment_center.py:** The main script where everything starts, this uses **media.py** to create instances of each movie, then calls **generate_html.py** to make the html page.
**media.py:** This is where the magic really happens, it contains the class **Movie** which is used to store all the important data like movie info and trailer path.
**generate_html.py:** This is where the html page is created, it uses styles from **style.css** and html within, to generate the page using the **Movie** instances called from **entertainment_center.py**.
**style.css:** This is where the css style for the page is kept.

#### APIs used

[OMDB](http://www.omdbapi.com)
[Youtube API v2](https://developers.google.com/youtube/2.0/developers_guide_protocol)
