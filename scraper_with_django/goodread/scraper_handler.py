import requests
from bs4 import BeautifulSoup

from django.conf import settings

from .models import Author, Genre, Book, BookGenre, Group, Keyword, SearchByKeyword, BookSearchByKeywordItem, \
    GroupSearchByKeywordItem


class ScraperHandler:
    def __init__(self, base_url, search_url):
        self.base_url = base_url
        self.search_url = search_url

    def request_to_target_url(self, url):
        print('URL:', url)
        return requests.get(url)

    def search_by_keyword(self, search_by_keyword_instance):
        search_items = list()

        for i in range(1, search_by_keyword_instance.page_count + 1):
            response = self.request_to_target_url(
                self.search_url.format(
                    query=search_by_keyword_instance.keyword,
                    page=i,
                    search_type=search_by_keyword_instance.search_type,
                    tab=search_by_keyword_instance.search_type
                )
            )

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                search_items += self.extract_search_items(
                    search_by_keyword=search_by_keyword_instance,
                    soup=soup
                )

        if search_by_keyword_instance.search_type == 'books':
            for i, search_item in enumerate(search_items, 1):
                book, genres = self.parse_book_detail(url=search_item.url)
                search_item.book = book
                search_item.is_scraped = True
                search_item.save()
                data = {
                    'title': book.title,
                    'author': book.author.fullname,
                    'description': book.description,
                    'thumbnail': book.thumbnail,
                    'genres': genres,
                }
                print(i, data)
        elif search_by_keyword_instance.search_type == 'groups':
            for i, search_item in enumerate(search_items, 1):
                group = self.parse_group_detail(url=search_item.url)
                search_item.group = group
                search_item.is_scraped = True
                search_item.save()
                data = {
                    'title': group.title,
                    'thumbnail': group.thumbnail,
                }
                print(i, data)
        return len(search_items)

    def extract_search_items(self, search_by_keyword, soup):
        search_items = list()

        search_result_item = soup.findAll(
            'a',
            attrs={'class': settings.GOOD_READS_ITEM_CLASS[search_by_keyword.search_type]}
        )

        for a in search_result_item:
            search_items.append(self.parse_search_item(search_by_keyword=search_by_keyword, a_tag=a))

        return search_items

    def parse_search_item(self, search_by_keyword, a_tag):
        if search_by_keyword.search_type == 'books':
            return BookSearchByKeywordItem.objects.create(
                search_by_keyword=search_by_keyword,
                title=a_tag.text.strip(),
                url=self.base_url + a_tag['href']
            )
        elif search_by_keyword.search_type == 'groups':
            return GroupSearchByKeywordItem.objects.create(
                search_by_keyword=search_by_keyword,
                title=a_tag.text.strip(),
                url=self.base_url + a_tag['href']
            )

    def parse_book_detail(self, url):
        response = self.request_to_target_url(url=url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1', attrs={'class': 'Text Text__title1'}).text
        description = soup.find('div', attrs={'class': 'DetailsLayoutRightParagraph__widthConstrained'}).find_next(
            'span').text
        thumbnail = soup.find('img', attrs={'class': 'ResponsiveImage', 'role': 'presentation'})['src']
        author, _ = self.parse_author(soup=soup)

        book, _ = Book.objects.get_or_create(
            author=author,
            title=title,
            description=description,
            thumbnail=thumbnail,
        )

        genres = self.parse_genre(soup=soup)

        for genre in genres:
            BookGenre.objects.get_or_create(book=book, genre=genre)

        return book, genres

    def parse_author(self, soup):
        fullname = soup.find('span', attrs={'class': 'ContributorLink__name'}).text
        return Author.objects.get_or_create(fullname=fullname)

    def parse_genre(self, soup):
        genres = list()
        genre_soup = soup.find('ul', attrs={'class': 'CollapsableList', 'aria-label': 'Top genres for this book'})
        for genre in genre_soup.findAll('span', attrs={'class': 'Button__labelItem'}):
            if genre.text != '...more':
                new_genre, _ = Genre.objects.get_or_create(title=genre.text)
                genres.append(new_genre)

        return genres

    def parse_group_detail(self, url):
        response = self.request_to_target_url(url=url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('div', attrs={'class': 'mainContentFloat'}).findNext('h1').text
        thumbnail = soup.find('a', attrs={'class': 'groupPicLink'}).find_next('img')['src']

        group = Group.objects.get_or_create(
            title=title,
            thumbnail=thumbnail,
        )

        return group
