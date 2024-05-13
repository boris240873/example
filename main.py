per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму: '))
tkb = money * (per_cent.get('ТКБ')/100)
skb = money * (per_cent.get('СКБ')/100)
vtb = money * (per_cent.get('ВТБ')/100)
sber = money * (per_cent.get('СБЕР')/100)
print = ([round(tkb), round(skb), round(vtb),round(sber)])



