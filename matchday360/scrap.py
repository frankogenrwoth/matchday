from bs4 import BeautifulSoup
from selenium import webdriver
from matchday360.models import Team, Match, Matchday, Competition
import datetime


def uploadData(dict_):
    teams = dict_["title"].split("vs")

    home_team = teams[0].strip()
    away_team = teams[1].strip()
    competition = dict_["competition"]
    match_overview = dict_["content"]["match_preview"]
    match_prediction = dict_["content"]["match_prediction"]
    home_team_news = dict_["content"]["info1"]
    away_team_news = dict_["content"]["info2"]
    matchday_date = dict_["matchday_date"]
    matchday_time = dict_["matchday_time"]

    try:
        home_team_ = Team.objects.get(team_name=home_team)
    except:
        home_team_ = Team.objects.create(team_name=home_team)
    try:
        away_team_ = Team.objects.get(team_name=away_team)
    except:
        away_team_ = Team.objects.create(team_name=away_team)

    try:
        competition_ = Competition.objects.get(competition_name=competition)
    except:
        competition_ = Competition.objects.create(competition_name=competition)

    date_objs = matchday_date.split(".")
    date_ = date_objs[0]
    month_ = date_objs[1]
    year_ = datetime.date.today().year

    match_ = Match.objects.create(
        home_team=home_team_,
        away_team=away_team_,
        competition=competition_,
        matchday_date=datetime.date(int(year_), int(month_), int(date_)),
        matchday_time=matchday_time,
    )

    matchday = Matchday.objects.create(
        match=match_,
        match_overview=match_overview,
        match_prediction=match_prediction,
        home_team_news=home_team_news,
        away_team_news=away_team_news,
    )
    print(f"[+] uploaded {dict_['title']} successfully")


def concat(list_):
    full_text = ""
    for item in list_:
        if item != None:
            if full_text == "":
                full_text = full_text + item
            else:
                full_text = full_text + "\n" + item
        else:
            pass
    return full_text


def cleanData(dict_, driver, league_list):
    # The link is passed through the dict_ object which contains the name and the target link
    matchday = dict_["match"].strip()
    target = dict_["link"]
    code = int(dict_["league_code"])
    league = league_list[code]
    matchday_date = dict_["timestamps"][0]
    matchday_time = dict_["timestamps"][1]

    # Set the driver to use the chrome interface and the parse the html to a soup object
    driver.get(target)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Fetch the main paragraphs of the document which contains the data about the game
    souply_ = soup.main
    obj_ = souply_.find_all("section")[1]

    datum = []
    for para in obj_.find_all("p"):
        datum.append(para.string)

    overview = datum[0:2]
    pred = datum[3:]

    match_preview = concat(overview)
    match_prediction = concat(pred)

    # filter the part of the document which has the team news
    dt_news = soup.find("section", id="team1-news")
    team_info = []

    for news in dt_news.find_all("section"):
        dt = []
        for team_news in news.find_all("p"):
            if team_news.string != None:
                dt.append(team_news.string)
            else:
                pass
        full_text = ""
        for line in dt[0:2]:
            if full_text != "":
                full_text = full_text + " " + line
            else:
                full_text = full_text + line
        team_info.append(full_text)

    info1 = team_info[0]
    info2 = team_info[1]

    context = {
        "match_preview": match_preview,
        "match_prediction": match_prediction,
        "info1": info1,
        "info2": info2,
    }

    # Return a dictionary in the desired form which can be added to a list and then written to a json file ready for upload
    return {
        "title": matchday.strip(),
        "competition": league,
        "content": context,
        "matchday_date": matchday_date,
        "matchday_time": matchday_time,
    }


def runit():
    driver = webdriver.Edge()

    # target holds the value of the target link
    target = "https://www.mightytips.com/"

    driver.get(target)

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    main = soup.find("section")

    league_list = []
    for images in main.find_all("img"):
        league_name = images["alt"]
        league_list.append(league_name)

    count = 0
    match_link = []
    for leagues in main.find_all("table"):
        for match in leagues.find_all("tr"):
            timestamps = []
            for time in match.find_all("time"):
                timestamps.append(time.string)
            td = match.find("a")
            match_link.append(
                {
                    "match": td.string,
                    "link": td["href"],
                    "league_code": count,
                    "timestamps": timestamps,
                }
            )
        count = count + 1

    print("\n\n[?] uploaded all match links \n\n")

    for match in match_link:
        dict_obj = cleanData(dict_=match, driver=driver, league_list=league_list)
        uploadData(dict_obj)
