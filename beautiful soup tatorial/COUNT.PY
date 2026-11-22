from bs4 import BeautifulSoup

with open("sample.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

# --- Iske neeche aapka pehle se likha hua code ---
ultag = soup.new_tag("ul")
litag = soup.new_tag("li")
litag.string = "home"
ultag.append(litag)

litag = soup.new_tag("li")
litag.string = "about"
ultag.append(litag)

soup.html.body.insert(0, ultag)
with open("modified_sample.html", "w") as f:
    f.write(str(soup))
ultag = soup.new_tag("ul")
litag = soup.new_tag("li")
litag.string = "home"
ultag.append(litag)

litag = soup.new_tag("li")
litag.string = "about"
ultag.append(litag)

soup.html.body.insert(0, ultag)
with open("modified_sample.html", "w") as f:
    f.write(str(soup))