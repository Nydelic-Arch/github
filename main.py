from side import quick_get
from side import has_chinese

url = "https://yhdm.one/"
soup = quick_get(url)

lbls = soup.find("div", class_="col-md-8").find_all("section")

print("=" * 50)
for lbl in lbls:
    try:
        print(lbl.find(class_="title pb-0").text)
        animes = lbl.find_all("li", class_="col-3 mb-3")
        for anime in animes:
            try:
                year = anime.find("span").text
                if has_chinese(year):
                    year = "連載中"
                title = anime.find("div", class_="small text-truncate").text
                link = "https://yhdm.one" + anime.find("a")["href"]

                print(year, title, "  ", link)
            except:
                continue
        print("=" * 50)
    except:
        continue
