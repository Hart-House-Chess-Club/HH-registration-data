import requests
from bs4 import BeautifulSoup

link = "https://www.harthouseregistration.ca/Program/GetProgramDetails?courseId=825cd713-6a9a-45c6-b9fc-a79b731789c9&semesterId=6d2f494c-d1e4-49e1-8939-419be66165a0"
starting_number = 200

response = requests.get(link)

# print(response.text) # entire page

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)


def calculate_number_registrants() -> int:
    """
    Returns the number of registrants on the HH Registration page
    """

    numbers = soup.findAll('p', attrs={"class": "car-text"})
    print(numbers)

    total_registrants = 0
    for value in numbers:
        string_remain = value.text
        remaining = string_remain.split()[0]
        print(remaining)
        total_registrants += (starting_number - int(remaining))

    return total_registrants


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    registrations = calculate_number_registrants()
    print("Total number of registrants: ", registrations)
    # print(4+14+16+14+9+7)
