import pinyin
import xlrd

target_file = open('stocks.csv', 'wt', encoding='gbk')
i = 0
with open('shanghai.csv', 'rt', encoding='gb2312') as f:
    f.readline()
    for line in f:
        cols = line.split()
        ch = cols[1].replace('*', '')
        ch = ch.replace('ST', '')
        py = pinyin.get_mutil_cn_first_letter(ch)
        target_file.write('\t'.join(cols[0:2] + [py]) + '\n')
        i = i + 1
    print('total:', i)

workbook = xlrd.open_workbook('shenzheng.xlsx')
sheet = workbook.sheet_by_index(0)
for i in range(1, sheet.nrows):
    row_values = sheet.row_values(i)
    code = row_values[5]
    name = row_values[6].replace(' ', '')
    ch = name.replace('*', '')
    ch = ch.replace('ST', '')
    py = pinyin.get_mutil_cn_first_letter(ch)
    target_file.write(code + '\t' + name + '\t' + py + '\n')
print('total:', sheet.nrows - 1)

        
target_file.close()
