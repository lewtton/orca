import openpyxl, os, psycopg2
conn = psycopg2.connect(database="djdb", user="django", password="django1sM01", host="217.163.11.235", port="5888")
print("Opened database successfully")
cur = conn.cursor()
MYPATH = os.getcwd()+'\stocks.xlsx'
# print(MYPATH)
WB = openpyxl.load_workbook(MYPATH)
SHT = WB.get_sheet_by_name('上市公司列表')
for row in SHT.rows:
    data = []
    for cell in row:
        data.append(cell.value)
    if (data[6]==""):
        data[6]="1900-01-01"
    print(data[0], '\t', data[2], '\t', data[6])
    cur.execute("INSERT INTO stocks_stocklist(id, code, name, fullname, intename, address, starttime, location, province, city, industry, www) \
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11]))
conn.commit()
conn.close()