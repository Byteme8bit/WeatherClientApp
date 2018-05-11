__author__ = "byteme8bit"


def main():
    # print header
    print_header()

    # get zip code from user
    code = int(input('What zipcode do you want the weather for?: '))

    # get html from web
    # https://www.wunderground.com/weather/us/ca/alhambra
    get_html(code)

    # parse the html
    # display for the forecast


def print_header():
    print('-------------------------------------------------')
    print('               Weather App                       ')
    print('-------------------------------------------------')
    print()


def get_html(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    print(url)
    requests


if __name__ == '__main__':
    main()
