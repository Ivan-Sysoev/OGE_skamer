import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def first_try(id, first_exersize, last_exersize):
    """Функция принимает 3 аргумента (ID варианта ОГЭ, номер первого задания, номер последнего задания) и возращает ответы"""
    answers = {}
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
    k = first_exersize
    for ex_id in exersize_id[first_exersize - 1:last_exersize]:
        ex_url = f"https://rus-oge.sdamgia.ru/problem?id={ex_id}"
        response = requests.get(ex_url, headers={"User-Agent": UserAgent().chrome})
        soup = BeautifulSoup(response.text, "lxml")
        result = soup.find_all("p")[-1].text
        answers[f"Задание №{k}"] = result[7 :-1]
        k = k + 1
    return answers

result = first_try(input(), int(input()), int(input()))
for elem in result:
    print(f"{elem}  =====> {result[elem]}")

print("\n" + "-" * 41)
print(" " * 10 + "press enter to exit")
print("-" * 41)
a = input()