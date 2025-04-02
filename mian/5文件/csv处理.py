import csv

with open('data.csv', mode="r", encoding="utf-8") as f:
    cf = csv.reader(f, delimiter=",")
    head = next(cf)  # 获取表头，之后在使用cf就会从下一行开始
    ages = []
    for row in cf:
        ages.append(int(row[2]))
        print(row, len(row))
    print(sum(ages))

# newline=""可以防止csv自动添加额外的空行
with open('data.csv', mode="a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["30", "tianqi", "12"])
    list = [["31", "tianqi", "12"], ["32", "tianqi", "12"], ["33", "tianqi", "12"]]
    writer.writerows(list)
