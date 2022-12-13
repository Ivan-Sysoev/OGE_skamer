import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def first_try(id, first_exersize, last_exersize):
    """Функция принимает 3 аргумента (ID варианта ОГЭ, номер первого задания, номер последнего задания) и возращает ответы"""
    answers = []
    url = f"https://rus-oge.sdamgia.ru/test?id={id}"
    response = requests.get(url, headers={"User-Agent": UserAgent().chrome})
    soup = BeautifulSoup(response.text, "lxml")
    exersize_id = []
    for a in soup.find_all("a"):
        try:
            b = int(a.text)
            exersize_id.append(b)
        except:
            None
    for ex_id in exersize_id[first_exersize - 1:last_exersize]:
        ex_url = f"https://rus-oge.sdamgia.ru/problem?id={ex_id}"
        response = requests.get(ex_url, headers={"User-Agent": UserAgent().chrome})
        soup = BeautifulSoup(response.text, "lxml")
        result = soup.find_all("p")[-1].text
        answers.append(result)
    return answers
print(first_try(10025650, 2, 5))