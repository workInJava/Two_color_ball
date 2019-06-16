"""
    sql select * from
    draw chart

"""
from db_mysql import db_mysql_detail
import matplotlib.pyplot as plt
import datetime

dbconn = db_mysql_detail('python')

def getData():
    queryData_sql = "select * from py_two_blue_ball"

    datas = dbconn.selectAll(queryData_sql)

    day = []
    y_one, y_two, y_three, y_four, y_five, y_six, y_seven, y_eight, y_nine, y_ten, y_eleven, y_twelve,  y_thirteen, y_fourteen, y_fifteen, y_sixteen \
        = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

    for data in datas:
        day.append(data[0])
        y_one.append(data[1])
        y_two.append(data[2])
        y_three.append(data[3])
        y_four.append(data[4])
        y_five.append(data[5])
        y_six.append(data[6])
        y_seven.append(data[7])
        y_eight.append(data[8])
        y_nine.append(data[9])
        y_ten.append(data[10])
        y_eleven.append(data[11])
        y_twelve.append(data[12])
        y_thirteen.append(data[13])
        y_fourteen.append(data[14])
        y_fifteen.append(data[15])
        y_sixteen.append(data[16])


    data = {"x": day, "y_one": y_one, "y_two": y_two, "y_three": y_three, "y_four": y_four, "y_five": y_five, "y_six": y_six, "y_seven": y_seven, "y_eight": y_eight,
            "y_nine": y_nine, "y_ten": y_ten, "y_eleven": y_eleven, "y_twelve": y_twelve,  "y_thirteen": y_thirteen, "y_fourteen": y_fourteen, "y_fifteen": y_fifteen, "y_sixteen": y_sixteen}
    return data



def draw_chart(data):


    ys = ["y_one", "y_two", "y_three", "y_four", "y_five", "y_six", "y_seven", "y_eight","y_nine", "y_ten", "y_eleven", "y_twelve",
          "y_thirteen", "y_fourteen", "y_fifteen","y_sixteen"]
    for y in ys:
        plt.plot(data["x"], data[y], label=y)


    plt.axis([datetime.date(2019, 5, 1), datetime.date.today(), 120, 180])
    plt.xlabel('count')
    plt.ylabel('day')
    plt.title("blue ball count")
    plt.legend()
    plt.show()



def main():
    data = getData()
    draw_chart(data)


if __name__ == '__main__':
        main()