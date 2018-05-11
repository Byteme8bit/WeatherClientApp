__author__ = "byteme8bit"
import requests
import bs4
import collections

weatherReport = collections.namedtuple('WeatherReport',
                                       ('cond', 'temp', 'scale', 'loc'))


def main():
    print_header()

    code = int(input('What zipcode do you want the weather for?: '))

    html = get_html(code)
    report = get_weather_from_html(html)

    print('The temp in {} is {} and {} {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))


def print_header():
    print('-------------------------------------------------')
    print('               Weather App                       ')
    print('-------------------------------------------------')
    print()


def get_html(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    print(url)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    # return condition, temp, scale, loc
    report = weatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def find_city_and_state_from_location(loc):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
