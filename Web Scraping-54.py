## 2. Web Page Structure ##

# Write your code here.

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

content = response.content

## 3. Retrieving Elements from a Page ##

from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document.
# Since we passed in the top level of the document to the parser, we need to pick a branch off of the root.
# With BeautifulSoup, we can access branches by using tag types as attributes.
title = parser.title
title_text = title.text

# Get the p tag from the body.
p = body.p

# Print the text inside the p tag.
# Text is a property that gets the inside text of a tag.
#print(title_text.text)

## 4. Using Find All ##

parser = BeautifulSoup(content, 'html.parser')

# Get a list of all occurrences of the body tag in the element.
body = parser.find_all("body")

# Get the paragraph tag.
p = body[0].find_all("p")

# Get the text.
print(p[0].text)

# Sacar uma lista de todas as ocurrencias q contêm a tag TITLE no doc content:

title = parser.find_all('title')
title_text = title[0].text

## 5. Element IDs ##

# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Pass in the ID attribute to only get the element with that specific ID.
second_paragraph = parser.find_all("p", id="second")[0]
second_paragraph_text = second_paragraph.text

print(second_paragraph_text)

## 6. Element Classes ##

# Get the website that contains classes.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Get the first inner paragraph.
# Find all the paragraph tags with the class inner-text.
# Then, take the first element in that list.
first_inner_paragraph = parser.find_all("p", class_="inner-text")[0]
print(first_inner_paragraph.text)

# Getting the second_inner_paragraph out of the doc:
second_inner_paragraph = parser.find_all('p', class_='inner-text')[1]
second_inner_paragraph_text = second_inner_paragraph.text
print(second_inner_paragraph_text)

# Getting the first_outer_paragraph out of the doc:
first_outer_paragraph = parser.find_all('p', class_='outer-text')[0]
first_outer_paragraph_text = first_outer_paragraph.text
print(first_outer_paragraph_text)

## 8. Using CSS Selectors ##

# Get the website that contains classes and IDs.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Select all of the elements that have the first-item class.
first_items = parser.select(".first-item")

# Print the text of the first paragraph (the first element with the first-item class).
print(first_items[0].text)


# Selecting all the elements with class outer-text:
outer_text = parser.select('.outer-text')
# Extracting the text from the first paragraph:
first_outer_text = outer_text[0].text
print(first_outer_text)

# Selecting all the elements with ID second:
id_second = parser.select('#second')
# Extracting the text:
second_text = id_second[0].text
print(second_text)

## 10. Using Nested CSS Selectors ##

# Get the Superbowl box score data.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")
content = response.content
parser = BeautifulSoup(content, 'html.parser')

# Find the number of turnovers the Seahawks committed.
turnovers = parser.select("#turnovers")[0]
seahawks_turnovers = turnovers.select("td")[1]
seahawks_turnovers_count = seahawks_turnovers.text
print(seahawks_turnovers_count)

teste_sea = parser.select('#turnovers td')[1].text
#teste_sea_text = teste_sea.text
print(teste_sea)

team_names = parser.select('.stats_table #team_stats #teams')

# Total Plays for the New England Patriots:
patriots_total_plays_count = parser.select('#total-plays td')[2].text

# Total Yards for the Seahawks:
seahawks_total_yards_count = parser.select('#total-yards td')[1].text