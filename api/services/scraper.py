from datetime import datetime

import requests
from bs4 import BeautifulSoup


def get_title(soup):
    title_div = soup.find("div", class_="BookPageTitleSection__title")
    if not title_div:
        return [None, None, None]

    series_link = title_div.find("a")
    title_h1 = title_div.find("h1", class_="Text Text__title1")
    title_text = title_h1.text.strip() if title_h1 else None

    series_name = None
    series_number = None
    if series_link:
        parts = series_link.text.strip().split(" #")
        series_name = parts[0]
        if len(parts) > 1:
            series_number = parts[1]

    return [series_name, series_number, title_text]


def get_authors(soup):
    authors = []
    author_divs = soup.find_all("div", class_="ContributorLinksList")
    for div in author_divs:
        names = div.find_all("span", class_="ContributorLink__name")
        for name in names:
            authors.append(name.text.strip())
    return authors


def get_book_details(soup):
    detail_elements = soup.find_all("div", class_="FeaturedDetails")[0]
    details = detail_elements.find_all("p")

    # pages and format
    pages_format = details[0].text.strip().split(", ")
    
    # Convert pages string to integer
    pages_str = pages_format[0]  # e.g., "234 pages"
    try:
        pages = int(''.join(filter(str.isdigit, pages_str)))
    except ValueError:
        pages = None  # fallback if conversion fails

    book_format = pages_format[1] if len(pages_format) > 1 else None

    # publication info
    publication_info = details[1].text.strip().split("First published ")[-1]
    published_date = datetime.strptime(publication_info, "%B %d, %Y").date()
    return pages, book_format, published_date


def get_book_genres(soup):
    genres = []
    genre_btns = soup.find_all("span", class_="BookPageMetadataSection__genreButton")
    for btn in genre_btns:
        label = btn.find("span", class_="Button__labelItem")
        if label:
            genres.append(label.text.strip())
    return genres


def get_book_summary(soup):
    summary_span = soup.find("span", class_="Formatted")
    return summary_span.text.strip() if summary_span else None


def get_cover_url(soup):
    cover_div = soup.find("div", class_="BookCover")
    if cover_div:
        img = cover_div.find("img", class_="ResponsiveImage")
        if img and img.has_attr("src"):
            return img["src"]
    return None


def get_gr_data(URL):
    """Scrape Goodreads book page and return structured data."""
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    title_info = get_title(soup)
    series_name, series_number, title = title_info

    authors = get_authors(soup)
    cover_img_url = get_cover_url(soup)
    summary = get_book_summary(soup)
    pages, book_format, published_date = get_book_details(soup)
    genres = get_book_genres(soup)

    book_data = {
        "title": title,
        "series_name": series_name,
        "series_number": series_number if series_number else 0,
        "author_names": authors,
        "cover_img_url": cover_img_url,
        "summary": summary,
        "pages": pages,
        "published_date": published_date,
        "format_type": book_format,
        "genre_names": genres,
    }

    return book_data