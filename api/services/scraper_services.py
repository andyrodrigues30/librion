import requests
from bs4 import BeautifulSoup


def get_title(soup):
	title_elements = soup.find_all("div", class_="BookPageTitleSection__title")[0]
	book_series_element = title_elements.find("a")
	print("ELEMENT: ", book_series_element)
	if (book_series_element != None):
		book_series = book_series_element.text.strip().split(" #")
		series_name = book_series[0]
		series_number = book_series[1]
		book_title = title_elements.find("h1", class_="Text Text__title1")
		return [series_name, series_number, book_title]
	else:
		book_title = title_elements.find("h1", class_="Text Text__title1")
		return [book_title.text.strip()]
	

def get_author(soup):
	author_elements = soup.find_all("div", class_="ContributorLinksList")[0]
	author = author_elements.find_all("span", class_="ContributorLink__name")[0].text.strip()
	return author


def get_book_details(soup):
	detail_elements = soup.find_all("div", class_="FeaturedDetails")[0]
	details = detail_elements.find_all("p")

	pages_format = details[0].text.strip().split(", ")
	pages = pages_format[0]
	book_format = pages_format[1]

	publication_info = details[1].text.strip().split("First published ")[-1]

	return [pages, book_format, publication_info]


def get_book_genres(soup):
	genre_btns = soup.find_all("span", class_="BookPageMetadataSection__genreButton")
	genre = []
	for genre_btn in genre_btns:
		genre.append(genre_btn.find_all("span", class_="Button__labelItem")[0].text.strip())
	return genre


def get_book_summary(soup):
	content = soup.find_all("span", class_="Formatted")
	summary = content[0].text.strip()
	return summary


def get_cover_url(soup):
	book_cover_elements = soup.find_all("div", class_="BookCover")
	cover_div = book_cover_elements[0]
	cover_img = cover_div.find("img", class_="ResponsiveImage")["src"]
	return cover_img


def get_book_data(URL):
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")

	author = get_author(soup)
	cover_img_url = get_cover_url(soup)
	book_summary = get_book_summary(soup)
	book_details = get_book_details(soup)
	pages = book_details[0]
	book_format = book_details[1]
	publication_info = book_details[2]
	genres = get_book_genres(soup)

	title_info = get_title(soup)
	print(title_info)
	
	if (len(title_info) == 3):
		series_name = title_info[0]
		series_number = title_info[1]
		title = title_info[2]
		book_data = {
			"title": title,
			"series": {
				"name": series_name,
				"number":series_number
			},
			"author": author,
			"goodreads-cover": cover_img_url,
			"summary": book_summary,
			"pages": pages,
			"format": book_format,
			"published": publication_info,
			"genres": genres
		}
	else:
		title = title_info[0]
		book_data = {
			"title": title,
			"author": author,
			"goodreads-cover": cover_img_url,
			"summary": book_summary,
			"pages": pages,
			"format": book_format,
			"published": publication_info,
			"genres": genres
		}
		
	return book_data

# URL = "https://www.goodreads.com/book/show/17470674-fahrenheit-451"
# get_book_data(URL)