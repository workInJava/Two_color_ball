"""
    作者：
    日期：
    功能：爬虫获取双色球 保存mysql
    版本：
"""
import requests
from db_mysql import db_mysql_detail
from bs4 import BeautifulSoup
import datetime


dbconn = db_mysql_detail('python')


def insert_Opr(data):

    if data:
        add_sql = ("INSERT INTO py_two_color_ball "
                   "(stage, first, second, third, fourth, fifth, sixth, blue, day)"
                   "VALUES (%(stage)s, %(first)s, %(second)s, %(third)s, %(fourth)s, %(fifth)s, %(sixth)s, %(blue)s, %(day)s)")

        batch_data = []
        for o in data:
            add_data = {
                'stage': o[0],
                'first': o[1],
                'second': o[2],
                'third': o[3],
                'fourth': o[4],
                'fifth': o[5],
                'sixth': o[6],
                'blue': o[7],
                'day': o[8]
            }
            batch_data.append(add_data)
        print(batch_data)
        dbconn.insertBatch(add_sql, batch_data)

def getStage():

    select_sql = "select * from py_two_color_ball order by day desc limit 1"
    data = dbconn.selectOne(select_sql)
    if data == None:
        return {'start': '03001', 'end': '19100'}
    else:
        lastest_date = data[8]
    now_date = datetime.date.today()
    delta = (now_date - lastest_date).days
    delta = int(delta / 2)
    if delta == 0:
        return
    start = str(int(data[0]) + 1)
    end = str(int(data[0]) + delta)
    return {'start': start, 'end': end}



def get_all_stages():
    """
        获取所有双色球开奖信息
    """
    stage = getStage()
    stages = []
    if stage:
        url = 'http://datachart.500.com/ssq/history/newinc/history.php?start='+stage['start']+'&end='+stage['end']
        r = requests.get(url, timeout=30)
        soup = BeautifulSoup(r.text, 'lxml')
        trs = soup.find_all('tr', {'class': 't_tr1'})
        for tr in trs:
            tds = tr.find_all('td')
            stages.append((tds[0].text, tds[1].text, tds[2].text, tds[3].text,
                           tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[15].text))

        print(stages)
    return stages


def getData():
    queryMaxDay_sql = "select max(day) from py_two_color_ball"
    sql = "select blue,count(1) from py_two_color_ball where day <= %s group by blue"
    days = dbconn.selectAll(queryMaxDay_sql)
    if days[0][0] == None:
        queryDay_sql = "select day from py_two_color_ball"
        days = dbconn.selectAll(queryDay_sql)

    insert_blue = ("INSERT IGNORE INTO py_two_blue_ball (day, one, two, three, four, five, six, seven, eight, nine, ten, "
                   "eleven, twelve, thirteen, fourteen, fifteen, sixteen)"
                   "VALUES (%(day)s, %(one)s, %(two)s, %(three)s, %(four)s, %(five)s, %(six)s, %(seven)s, %(eight)s, "
                   "%(nine)s, %(ten)s, %(eleven)s, %(twelve)s, %(thirteen)s, %(fourteen)s, %(fifteen)s, %(sixteen)s)")
    datas = []
    dict = {}
    for day in days:

        os = dbconn.selectAll(sql, day)
        for o in os:
            dict[o[0]] = o[1]

        add_data = {
            'day': str(day[0]),
            'one': dict.get(1, 0),
            'two': dict.get(2, 0),
            'three': dict.get(3, 0),
            'four': dict.get(4, 0),
            'five': dict.get(5, 0),
            'six': dict.get(6, 0),
            'seven': dict.get(7, 0),
            'eight': dict.get(8, 0),
            'nine': dict.get(9, 0),
            'ten': dict.get(10, 0),
            'eleven': dict.get(11, 0),
            'twelve': dict.get(12, 0),
            'thirteen': dict.get(13, 0),
            'fourteen': dict.get(14, 0),
            'fifteen': dict.get(15, 0),
            'sixteen': dict.get(16, 0)
        }
        datas.append(add_data)
        dict.clear()

    print(datas)
    dbconn.insertBatch(insert_blue, datas)

    # smpe = {'day': '2003-2-23', 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0, 'six': 0,
    #         'seven': 0, 'eight': 0, 'nine': 0, 'ten': 0, 'eleven': 1, 'twelve': 0, 'thirteen': 0, 'fourteen': 0,
    #         'fifteen': 0, 'sixteen': 0}
    # dbconn.insertOne(insert_blue, smpe)

def main():
    """
        main函数
    """
    insert_Opr(get_all_stages())
    getData()

if __name__ == '__main__':
    main()