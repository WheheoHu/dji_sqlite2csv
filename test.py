from dji_sqlite2csv import dji_csv_export

print(zip(range(1,5),range(5,10)))
for idx,value in enumerate(zip(range(1,5),range(5,10))):
    iter_1,iter_2=value
    print(idx,iter_1,iter_2)
#dji_csv_export('./DB_file/L2D-20c.db',combine_export=True,only_combine=True,is_mavic=True)