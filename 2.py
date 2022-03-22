h=float(input('Digite a quantidade de horas para conversão: '))
print('A conversão será nesta seguencia: Meses(30dias),semanas, minutos , segundos e milisegundos')
m=h/730
s = h / 168
min= h * 60
seg = h * 3600
mseg = h * 3600000
print('A conversão: {};{};{};{};{}'.format(m,s,min,seg,mseg))