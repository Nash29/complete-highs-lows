# pagina 455 info sobre datas important

# importa csv
import csv
from datetime import datetime

from matplotlib import pyplot as plt


# armazena em filename
filename = 'death_valley_2014.csv'

# Abre o arquivo
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader) # next -> devolve a próxima linha do arquivo
	
	'''
	# Exibindo cabeçalho e suas posições
	for index, column_header in enumerate(header_row):
		print(index, column_header)
	'''
	
	# Obtém as datas e as temperaturas maximas e minimas do arquivo
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], '%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date, 'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
		
	print(highs)
	
	
# Faz a plotagem dos dados
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)# alpha 1 mt escuro, 0 mt claro
plt.plot(dates, lows, c='blue', alpha=0.5)
# Coloca cor entre as linhas vermelho e o azul
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


# Formata o grafico
title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
fig.autofmt_xdate()# desenha as datas em diagonal
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()










