from bs4 import BeautifulSoup
from urllib.request import urlopen
import numpy as np

def url_open(link):
    return str(urlopen(link).read())

def sort_dict(sdict):
    sdict = np.array(sdict[:26])
    return write_down(str(sdict.reshape(26, 1)))

def parse(url):
    soup = BeautifulSoup(url_open(url), "html.parser")
    table = soup.find("table", id = "scoreboard") #find the table of scoreboard
    rows_head = table.find_all("tr")[:1] #find all tr tags in the thead
    rows_body = table.find_all("tr")[1:] #find all tr tags in the tbody
    dict = []
    for one_tr in rows_head:
        cols_h = one_tr.find_all("td")
        text_head = ""
        t = 0
        for one_td in cols_h:
            tag_b = one_td.find_all("b")
            for i in tag_b: #take the fucking word out from the tag b
                for j in i:
                    if t == 0:
                        text_head += " " + str(j)
                        t += 1
                    elif t == 1:
                        text_head += "             " + str(j)
                        t += 1
                    elif t == 2:
                        text_head += "                      " + str(j)
    dict.append("%s" % text_head)

    for one_tr in rows_body:
        cols = one_tr.find_all("td") #find all td tags in our one tr
        text_body = ""
        i = 0
        for one_td in cols:
            if i == 0:
                text_body += "---" + one_td.get_text()
                i += 1
            elif i == 1:
                if len(one_td.get_text()) > 14:
                    text_body += "-----------" + one_td.get_text()
                    i += 1
                else:
                    text_body += "-------------" + one_td.get_text() + "----------"
                    i += 1
            elif i == 2:
                text_body += "-----------" + one_td.get_text() + "---"
        dict.append("%s" % text_body)

    return sort_dict(dict)

def write_down(itog_table):
    with open("/home/chinababka/GitHub/CHINA-s/Practiсe4/parser_text.txt", "w") as file:
        file.write(itog_table)
    return "Nice job! The process has been successfully done."

def main():
    url = "http://zss-courses.cf/scoreboard"
    print(parse(url))

if __name__ == "__main__":
    main()
