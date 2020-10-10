Програма пошуку трамвайних маршрутів.

Дані у файлах X_tram.txt (X - 1,2,3,4,6,7,8,9) записані у форматі: value\n ... \n---Зворотний\n ... value\n
Основний сепаратор - Enter (\n), слово 'Зворотний' використовується для позначення рядка файлу, після якого записані зупинки трамваю у зворотньому маршруті.

Меню:
1) find route between start_stop and end_stop - Знайти маршрут між start_stop i end_stop.
Результатом може бути як і прямий маршрут (direct route), так і маршрут, який потребує зміни трамваю (need change tram route).

Приклад 1:
	Enter start stop: вул. Пасічна
	Enter end stop: вул. Руська
Результат:
	Direct route
	Tram №1 [Залізничний вокзал]
	Start from вул. Пасічна drive 6 stops and get of on вул. Руська
	
Приклад 2:
	Enter start stop: вул. Пасічна
	Enter end stop: вул. Підвальна
Результат:
	Need change tram route
	Start from вул. Пасічна - tram №1 [Залізничний вокзал].
	Drive 3 stops and hop off on Медичний університет.
	Change tram to №7 [вул. Татарбунарська].
	Drive 3 stops and hop off on вул. Підвальна.

2) find if there is direct tram between start_stop and end_stop - Знайти, чи є прямий трамвай між start_stop та end_stop місто.

Приклад 1:
	Enter start stop: вул. Пасічна
	Enter end stop: пл. Митна
Результат:
	Is there a direct route between вул. Пасічна and пл. Митна?
	Yes
	Tram №1 [Залізничний вокзал]
	Start from вул. Пасічна drive 5 stops and get of on пл. Митна

Приклад 2:
	Enter start stop: Погулянка
	Enter end stop: вул. Київська
Результат:
	Is there a direct route between вул. Пасічна and пл. Митна?
	No

3) find trams which has stop X - Знайти номери трамваїв, які мають зупинку X.

Приклад 1:
	Enter stop: Медичний університет
Результат:
	Tram № 1, 2, 7

4) close program - Закінчити виконання програми.
