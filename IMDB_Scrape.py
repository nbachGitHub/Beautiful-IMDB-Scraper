import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.imdb.com/search/title/?genres=documentary&sort=user_rating,desc&title_type=tv_series,mini_series&num_votes=5000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f85d9bf4-1542-48d1-a7f9-48ac82dd85e7&pf_rd_r=5PJS3V6Q58Q4NKFMV0GF&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_gnr_7"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')


movies = soup.find_all("div", class_= "lister-item-content")
#Usd div because that was infront of the class


with open('C:\\Users\\test\\github\\test_repo\\IMDB-csv.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Name & Rank", "Rating, Genre, & Length", "Rating Stars"])
  for movie in movies:
    movie_header = movie.find("h3", class_= "lister-item-header").text
    #Usd h3 because that was infront of the class

    movie_info = movie.find("p", class_= "text-muted").text
    #Usd p because that was infront of the class

    movie_stars = movie.find("div", class_= "ratings-imdb-rating").text
    #Usd div because that was infront of the class

    compiled_movie_info = [movie_header, movie_info, movie_stars]
    writer.writerow(compiled_movie_info)
