'''
Created on 2018/01/28

@author: nob0tate14
'''
import json
import requests


def get_data(span):

    req_url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/" \
        f"country/mavg/tas/{span}/jpn"

    r = requests.get(req_url)
    print(r.text)
    jd = json.loads(r.text)
    dl = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    dl[0].append("Year")
    dl[1].append("1")
    dl[2].append("2")
    dl[3].append("3")
    dl[4].append("4")
    dl[5].append("5")
    dl[6].append("6")
    dl[7].append("7")
    dl[8].append("8")
    dl[9].append("9")
    dl[10].append("10")
    dl[11].append("11")
    dl[12].append("12")

    for dc in jd:
        gcm = dc['gcm']
        dl[0].append(gcm)
        monthVals = dc['monthVals']
        dl[1].append(monthVals[0])
        dl[2].append(monthVals[1])
        dl[3].append(monthVals[2])
        dl[4].append(monthVals[3])
        dl[5].append(monthVals[4])
        dl[6].append(monthVals[5])
        dl[7].append(monthVals[6])
        dl[8].append(monthVals[7])
        dl[9].append(monthVals[8])
        dl[10].append(monthVals[9])
        dl[11].append(monthVals[10])
        dl[12].append(monthVals[11])

    return json.dumps(dl)


def get_data2(span):

    req_url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/" \
        f"country/annualavg/tas/{span}/jpn"

    r = requests.get(req_url)
    print(r.text)
    jd = json.loads(r.text)
    ret = ""
    for x in jd:
        print(x)
        gcm = x['gcm']
        annualData = x['annualData']
        print(annualData)
        ret += "['" + gcm + "', " + str(annualData[0]) + "],"

    return ret
