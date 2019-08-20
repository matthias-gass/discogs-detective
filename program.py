import requests
import bs4
import emailer
import csv


def main():
    # get release codes from csv
    release_codes = [c for code in read_csv(r'data/release_codes.csv') for c in code]
    # create urls for web scraping
    urls = ['https://www.discogs.com/de/sell/release/{}?ev=rb'.format(r) for r in release_codes]
    # web scraping
    current_offers = list(get_offers_from_dicogs(urls))
    # get last offers from csv
    last_offers = read_csv(r'data/offers.csv')
    # compare results from web scraping (current offers) with last offers
    # and only send mail if there are any changes
    if not current_offers == last_offers:
        mail_string = '\n\n'.join([' '.join(offer) for offer in current_offers])
        emailer.send_mail(mail_string)
        write_csv(current_offers)


def get_offers_from_dicogs(urls):
    for url in urls:
        req = requests.get(url)
        req.raise_for_status()

        soup = bs4.BeautifulSoup(req.content, 'html.parser')
        soup_offers = soup.find_all('tr', {'class': 'shortcut_navigable'})

        for item in soup_offers:
            title = item.find('a', {'class': 'item_description_title'}).string
            condition = item.find('i', {'class': 'icon icon-info-circle muted media-condition-tooltip'})\
                .previous_sibling.string.strip()
            location = item.find(string='Versand aus:').next_element.string
            price = item.find('span', {'class': 'price'}).string.replace('\xa0', '')
            yield [title, condition, location, price]


def read_csv(file, delim='|'):
    try:
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=delim)
            return [line for line in reader]
    except FileNotFoundError:
        return []


def write_csv(offers):
    with open(r'data/offers.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='|')
        writer.writerows(offers)
                   
           
if __name__ == '__main__':
    main()
