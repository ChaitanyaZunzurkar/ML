from pickle import TRUE
import pandas as pd
import requests
from bs4 import BeautifulSoup

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
page = 1

bookTitleList = []
prices = []
ratingsOfBooks = []

while TRUE:
   url = base_url.format(page)
   response = requests.get(url)

   if response.status_code != 200:
      break;

   soup = BeautifulSoup(response.text , 'html.parser')

   books = soup.find_all('h3')
   priceOfBooks = soup.find_all('p' , class_ = "price_color")
   for book in books:
      bookTitle = book.a["title"]
      bookTitleList.append(bookTitle)

   for price in priceOfBooks:
      priceOfBook = price.text
      priceOfBook = priceOfBook[1:-1]
      prices.append(priceOfBook)

   ratings = soup.find_all('p' , class_ = "star-rating")
   for rating in ratings:
      ratingOfBook = rating["class"][1]
      ratingsOfBooks.append(ratingOfBook)

   page = page + 1;

df = pd.DataFrame({
    "Title":bookTitleList,
    "Price":prices,
    "Rating": ratingsOfBooks
})

df.to_csv("books_data.csv" , index = False)

BooksDataFrame = pd.read_csv("books_data.csv")
BooksDataFrame.head()