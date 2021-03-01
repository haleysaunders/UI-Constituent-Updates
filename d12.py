#Written by Haley Saunders, 2021 General Assembly Session intern for Senator Lam's office
#Please contact me at 310-912-4680 or haleysaunders17@gmail.com with questions regarding this program.
#DO NOT USE WITHOUT PERMISSION. LICENSING REQUIRED. THIS SOURCE CODE IS INTENDED FOR INTERNAL USE WITH SEN LAM'S D12 OFFICE.

import csv
with open("d12_tracker.csv","r") as d12_tracker, \
    open("feb26_update.csv","r") as recent_update, \
    open("feb17_sorted.csv","r") as feb17_sorted, \
    open("feb26_sorted.txt",'a') as feb26_sorted:
    read_recent_update = csv.reader(recent_update, delimiter = ',')
    read_d12_tracker = csv.reader(d12_tracker,delimiter = ',')
    read_feb17_sorted = csv.reader(feb17_sorted,delimiter = ',')
    d12_list = list(read_d12_tracker)
    update_list = list(read_recent_update)
    feb17_list = list(read_feb17_sorted)
    print(feb17_list)
    for line in feb17_list:
        for i in update_list:
            try:
                if line[0] in i[1]:
                    if line[1] == 'Closed':
                        if i[3] == 'Closed':
                            del i
            except:
                IndexError

    
    for row in d12_list:
        for i in update_list:
                if row[0] in i[1]:
                    if row[1] in i[1]:
                        feb26_sorted.write(i[1]+','+i[3]+','+row[10]+'\n')


d12_tracker.close()
recent_update.close()
feb17_sorted.close()
feb26_sorted.close()
