import csv
import re
from collections import Counter



def fireType():
    file = open('pokemonTrain.csv')
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    fireCnt = 0
    allCnt = 0

    for row in csvreader:
        rows.append(row)
    for i in rows:
        if i[4] == 'fire' and float(i[2]) >= 40.0:
            fireCnt += 1
    for i in rows:
        if i[4] == 'fire':
            allCnt += 1

    percentage = round((fireCnt / allCnt) * 100)

    text_file = open("pokemon1.txt", "w")
    text_file.write('Percentage of fire type pokemon at or above level 40 = ' + str(percentage))
    text_file.close()

def missingTypeFill():
    file = open('pokemonTrain.csv')
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    type_list = []
    for row in csvreader:
        rows.append(row)

    for i in rows:
        if i[4] != 'NaN' and i[4] not in type_list:
            type_list.append(i[4])

    type_to_weaknesses_dict = {}
    for t in type_list:
        weakness_list = []
        for i in rows:
            if i[4] == t and i[5] != 'NaN':
                weakness_list.append(i[5])
        type_to_weaknesses_dict[t] = weakness_list

    most_common_weakness_dict = {}
    for t in type_to_weaknesses_dict:
        occurrence_count = 0
        common_weakness = ''
        for w in type_to_weaknesses_dict[t]:
            weakness_count = type_to_weaknesses_dict[t].count(w)
            if weakness_count == occurrence_count:
                if w > common_weakness:
                    common_weakness = w
            elif weakness_count > occurrence_count:
                occurrence_count = weakness_count
                common_weakness = w
        most_common_weakness_dict[t] = common_weakness
    # now have dictionary of with format {type : most common weakness}
    return most_common_weakness_dict


def avgAtr40up():
    file = open('pokemonTrain.csv')
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    threshold = 40.0
    atkCnt = 0
    hpCnt = 0
    defCnt = 0
    atkSum = 0
    hpSum = 0
    defSum = 0

    for row in csvreader:
        rows.append(row)

    for i in rows:
        if float(i[2]) > threshold and i[6] != 'NaN':
            atkSum += float(i[6])
            atkCnt += 1
    for i in rows:
        if float(i[2]) > threshold and i[7] != 'NaN':
            defSum += float(i[7])
            defCnt += 1
    for i in rows:
        if float(i[2]) > threshold and i[8] != 'NaN':
            hpSum += float(i[8])
            hpCnt += 1

    avgAtk = round(atkSum / atkCnt)
    avgDef = round(defSum / defCnt)
    avgHp = round(hpSum / hpCnt)

    return avgAtk, avgDef, avgHp


def avgAtr40down():
    file = open('pokemonTrain.csv')
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    threshold = 40.0
    atkCnt = 0
    hpCnt = 0
    defCnt = 0

    atkSum = 0
    hpSum = 0
    defSum = 0

    for i in rows:
        if float(i[2]) < threshold and i[6] != 'NaN':
            atkSum += float(i[6])
            atkCnt += 1
    for i in rows:
        if float(i[2]) < threshold and i[7] != 'NaN':
            defSum += float(i[7])
            defCnt += 1
    for i in rows:
        if float(i[2]) < threshold and i[8] != 'NaN':
            hpSum += float(i[8])
            hpCnt += 1

    avgAtk = round(atkSum / atkCnt)
    avgDef = round(defSum / defCnt)
    avgHp = round(hpSum / hpCnt)

    return avgAtk, avgDef, avgHp


def fillAttr():
    file = open('pokemonTrain.csv')
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)

    avgAtk, avgDef, avgHp = avgAtr40up()
    avgAtkDown, avgDefDown, avgHpDown = avgAtr40down()

    for i in rows:
        if i[6] == 'NaN' and float(i[2]) > 40.0:
            i[6] = avgAtk
        if i[7] == 'NaN' and float(i[2]) > 40.0:
            i[7] = avgDef
        if i[8] == 'NaN' and float(i[2]) > 40.0:
            i[8] = avgHp

    for i in rows:
        if i[6] == 'NaN' and float(i[2]) <= 40.0:
            i[6] = avgAtkDown
        if i[7] == 'NaN' and float(i[2]) <= 40.0:
            i[7] = avgDefDown
        if i[8] == 'NaN' and float(i[2]) <= 40.0:
            i[8] = avgHpDown

    type_to_weakness_dict = missingTypeFill()
    for i in rows:
        if i[4] == 'NaN':
            for type in type_to_weakness_dict:
                if type_to_weakness_dict[type] == i[5]:
                    i[4] = type

    f = open('pokemonResult.csv', 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(header)
    for i in rows:
        writer.writerow(i)

    f.close()


# def fillType():
#     file = open('pokemonTrain.csv')
#     csvreader = csv.reader(file)
#
#     header = []
#     header = next(csvreader)
#
#     rows = []
#     for row in csvreader:
#         rows.append(row)
#     type_weakness_list = []
#     type_dict = {}
#
#     print(type_dict)
#     for i in rows:
#         type_weakness_list.append((i[4], i[5]))
#
#     type_weakness_dict = Counter(type_weakness_list)
#     print(type_weakness_dict)
#     weakness_map = {}
#     for i in rows:
#         if (i[4] == 'NaN'):
#             key = (i[4], i[5])
#
#     for key, value in type_weakness_dict:
#         print(max(type_weakness_dict))


def personalityDict():
    file = open('pokemonResult.csv')
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    perDict = dict()

    rows = []
    for row in csvreader:
        rows.append(row)

    for i in rows:
        type = i[4]
        personality = i[3]
        if type in perDict:
            perDict[type].append(personality)
        else:
            perDict[type] = [personality]

    f = open('pokemon4.txt', 'w')
    text_file = open("pokemon4.txt", "w")
    for key in perDict:
        text_file.write(key + ": ")
        s1 = str(perDict[key]).replace('[', '')
        s2 = s1.replace(']', '')
        s3 = s2.replace('\'', '')
        text_file.write(s3 + "\n")

    text_file.close()

    f.close()


def averageHP():
    file = open('pokemonResult.csv')
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)

    rows = []
    hpCnt = 0
    hpSum = 0

    for row in csvreader:
        rows.append(row)
    for i in rows:
        if float(i[9]) == 3.0:
            hpCnt += 1
            hpSum += float(i[8])

    Average = round((hpSum / hpCnt))

    text_file = open("pokemon5.txt", "w")
    text_file.write('Average hit point for pokemon of stage 3.0 = ' + str(Average))
    text_file.close()


def main():
    fireType()
    fillAttr()
    personalityDict()
    averageHP()
    pass


main()
