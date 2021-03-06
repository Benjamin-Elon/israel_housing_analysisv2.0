import random
import re
import sqlite3
import time
import requests
from bs4 import BeautifulSoup
import playsound
import pandas as pd
import Database.database as database
import Scrape.parse_listings as parse_listings
import Settings.settings_manager as settings_manager
import numpy as np


def set_random_agent():
    """
    Randomly rotates user agents - captcha avoidance
    Updates: global user_agent variable
    """
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36']

    rand_choice = np.random.randint(0, len(user_agents))
    user_agent = user_agents[rand_choice]
    globals()['user_agent'] = user_agent
    print(user_agent)

    return user_agent


user_agent = set_random_agent()


def search(first_page_url, max_pages):
    """Commences a search on a url"""
    max_pages = int(max_pages)
    # fetch first page to get number of pages of listings
    num_of_pages, cookies = get_number_of_pages(first_page_url)
    print(num_of_pages)
    # TODO build proper version and remove:
    if max_pages <= num_of_pages:
        num_of_pages = max_pages
    # # if you want to start from later page
    # if num_of_pages > 10:
    #     n = 10
    # else:
    #     n = num_of_pages
    for page_num in range(num_of_pages):
        page_num = page_num + 1
        print("Fetching page:", page_num, '/', num_of_pages)
        params = first_page_url.split('realestate/rent?')[1]
        part_1 = 'https://www.yad2.co.il/api/pre-load/getFeedIndex/realestate/rent?'
        part_2 = '&compact-req=1&forceLdLoad=true'
        if page_num == 1:
            url = part_1 + params + part_2
            response = get_next_page(url, cookies, first_page_url)
        else:
            url = part_1 + params + '&page=' + str(page_num) + part_2
            response = get_next_page(url, cookies, url)

        # get the next page
        # if page_num == 2:
        #     url_1 = first_page_url + '&page=2'
        #     response = get_next_page(url, cookies, url_1)

        print(url)

        # parse the listings
        listing_list = parse_listings.parse_feedlist(response)
        listing_list = get_more_details(cookies, listing_list)
        listing_list = database.filter_results(listing_list)
        database.add_listings(listing_list)

        # Sleep for a bit between calls
        x = random.randrange(2, 4)
        print('sleeping for', x, 'seconds...')
        time.sleep(x)


def get_number_of_pages(url):
    """
    Gets the number of pages from the first page of results
    Does not scrape listings. Data format is unfortunately different when requesting the first page
    """
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'he,en-US;q=0.9,en;q=0.8',
        'sec-gpc': '1',
    }

    # TODO improve cookie spoofing here
    response = requests.get(url, headers=headers)
    # print(response.text)
    soup = BeautifulSoup(''.join(response.text), 'html.parser')

    # no captcha
    if check_for_captcha(response) is False:
        cookies = get_cookie(response)

        if soup.find('button', {"class": "page-num"}) is None:
            total_pages = 1

        else:
            total_pages = int(soup.find('button', {"class": "page-num"}).contents[0].string)

    # captcha: re-fetch and refresh cookie
    else:
        total_pages, cookies = get_number_of_pages(url)

    return total_pages, cookies


def update_cookie(response):
    """
    Updates the cookie between requests
    Returns: cookies
    """
    cookie_params = response.headers['Set-Cookie']
    # print(cookie_params)

    cookies = {}
    cookie_attributes = {'uzma': '__uzma=', 'uzmb': '__uzmb=', 'uzmc': '__uzmc=', 'uzmd': '__uzmd=', 'uzme': '__uzme',
                         'favorites_userid': 'favorites_userid=', 'y2_cohort_2020': 'y2_cohort_2020=',
                         'leadSaleRentFree': 'leadSaleRentFree=', 'canary': 'canary=', 'abTestKey': 'abTestKey=',
                         'server_env': 'server_env=', 'use_elastic_search': 'use_elastic_search='}

    # extract parameters from cookie
    for param, string in cookie_attributes.items():
        try:
            # find end index
            end = re.search(string, cookie_params).end()
            value = cookie_params[end:].split(';', 1)[0]
            # only add values present in the cookie
            if value is not None:
                cookies[param] = value
        except AttributeError:
            pass

    return cookies


def check_for_captcha(response):
    """User intervention on captcha"""
    if "ShieldSquare Captcha" in response.text:
        print(response.url)
        # playsound.playsound('ship_bell.mp3')
        input("Stuck on captcha. Press enter when done (enter x2: Continue)\n")
        while True:
            x = input("Select action:\n"
                      "(1) Replace user agent\n"
                      "(2) Continue\n")

            # generate new random agent
            if x == '1':
                set_random_agent()
                print("New agent set\n")
            return True
    else:
        return False


def get_cookie(response):
    """Get an updated cookie"""
    cookies = update_cookie(response)
    return cookies


def get_next_page(url, cookies, url_1=None):
    """Fetches the next page in a scraping scan
    Returns: response
    """
    if url_1 is None:
        url_1 = url
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': user_agent,
        'DNT': '1',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': url_1,
        'Accept-Language': 'he,en-US;q=0.9,en;q=0.8',
        'sec-gpc': '1',
    }

    x = 0
    while True:
        try:
            response = requests.get(url, headers=headers, cookies=cookies)
            x += 1
            if x > 5:
                input("Problems loading page. fix and press enter...")
                x = 0
                continue
        except requests.exceptions.ConnectionError:
            print("Error: connection error (104)")
            time.sleep(5)
        else:
            # response timeout
            if response.text is None:
                print("Error: no response...")
                continue
            else:
                if check_for_captcha(response) is False:
                    break

                # captcha: re-fetch and refresh cookie
                else:
                    cookies = get_cookie(response)

    return response


def get_more_details(cookies, listing_list):
    """
    Depending of a set of conditions, gathers extra info on a listing (total_floors, descriptions, vaad_bayit)
    Returns: listing_list
    """
    listing_list_1 = []
    # vary the ratio of opened to unopened by page. Some pages open a lot some pages fewer
    rand_1 = random.normalvariate(10, .05)
    x = 1
    for listing in listing_list:

        result = database.check_extra_conditions(listing)
        # if we randomly want to get a few listings
        if result is False:
            # leave some listings out to avoid ban
            rand = random.random()
            if rand < rand_1:
                listing_list_1.append(listing)
                continue
            else:
                listing_list_1.append(listing)
                continue

        elif result is True:
            pass

        # print("Fetching extra info for listing:", listing.listing_id)

        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': user_agent,
            'DNT': '1',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.yad2.co.il/realestate/rent?price=1000-1500&squaremeter=50-100',
            'Accept-Language': 'he,en-US;q=0.9,en;q=0.8',
            'sec-gpc': '1',
        }

        try:
            response = requests.get('https://www.yad2.co.il/api/item/' + listing.listing_id, headers=headers,
                                    cookies=cookies)
        except requests.exceptions.ConnectionError:
            time.sleep(5)
            continue

        cookies = update_cookie(response)
        extra_info = response.text
        if '504 Gateway Time-out' in extra_info or '502 Bad Gateway' in extra_info:
            print("Timed out other error")
            continue

        # no captcha
        if check_for_captcha(response) is False:
            print("adding extra info for: " + listing.listing_id + " " + str(x) + '/' + str(len(listing_list)))
            # print(len(listing_list))
            listing = parse_listings.parse_extra_info(extra_info, listing)
            listing_list_1.append(listing)
            x += 1

        # captcha: re-fetch and refresh cookie
        else:
            continue

    return listing_list_1


con = sqlite3.connect(r"Database/yad2db.sqlite")
cur = con.cursor()


def select_areas_to_scan():
    """
    Displays a list of urls for areas from which to build a scan profile for scraping
    Returns: url_list
    """
    menu = []
    # scope_names = ['Top_areas', 'Areas', 'Cities', 'Neighborhoods', 'Streets']
    df = pd.read_sql('SELECT * FROM Areas', con)
    area_ids = df[['area_id', 'area_name']].drop_duplicates()
    for area_id, area_name in area_ids.values:
        if area_name != '':
            menu.append([area_id, area_name])
        # sort by menu alphabetically
        menu.sort(key=lambda tup: tup[1])

    menu = list(enumerate(menu))

    for num, [area_id, area_name] in menu:
        print(area_name, '(' + str(num) + ')')

    print("Select desired areas:\n"
          "When finished, press enter.\n"
          "Press enter to search all areas.")

    # area_ids = [x[1][0] for x in menu]
    # print(area_ids)

    # Select as many areas as you want
    selection = []
    while True:
        x = input()
        if x == '' and selection == []:
            for x in range(len(menu)):
                selection.append(menu[x][1][0])
            print(selection)
            break
        elif x == '':
            break
        else:
            try:
                x = int(x)
            except ValueError:
                print("invalid input")
                continue

        if x not in range(len(menu)):
            print("invalid selection")
            continue
        elif x in selection:
            print("already selected")
            continue
        else:
            selection.append(menu[x][1][0])

    # generate list of urls
    url_list = []
    for area_id in selection:
        url = 'https://www.yad2.co.il/realestate/rent?area=' + str(area_id) + '&price=1000-10000&squaremeter=0-500'
        url_list.append(url)

    x = input("Would you like to save this search profile? (y/n)")
    if x == 'y':
        settings_manager.save_settings(url_list, 'search_urls')
    # give the urls a quick shuffle
    random.shuffle(url_list)
    print(url_list)

    return url_list
