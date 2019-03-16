import pandas as pd

my_data = pd.read_csv('dump.csv', sep=',', header=0)                #читаем данные из csv

result_df = my_data.groupby(['Source','Protocol'])['No.'].count()   #делаем группировку

result_df = pd.DataFrame(result_df)                                 #Преобразуем обьект Series в DataFrames

result_df = result_df.rename(columns={'No.': 'Using count'})        #Меняем название столбца

print (result_df)                                                   #Выводим результат в консоль

result_df.to_csv('result.csv')                                      #Сохраняем результат в csv
