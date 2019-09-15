# Что тут может не работать?

lesson = 250834

## QUIZ

Студент писал программу для подсчета количества понедельников в месяце. В месяце может быть 28, 30 или 31 день.
Понедельник считается первым днем в неделе, вторник - 2, ..., воскресенье - 7.

```c
#include <stdio.h>

int main(){
	unsigned char nday; // число месяца первого понедельника
	unsigned char days; // количество дней в месяце
	unsigned char count; // количество дней недели в месяце

// получение данных с консоли (клавиатура)
	scanf("%hhd%hhd",&days, &nday);
// подсчет количества дней
	count = 1 + days - nday /7;
// вывод
	printf("%u\n", nday);
  return 0;
}
```
При тестированиии он получил такую таблицу:

|номер|days|nday|ожидаемый<br/> результат|получилось<br/> (result)| верно?<br/> да/нет|
|--|--|--|--|--|--|
|1|28|4|4|4|да
|2|31|1|5|1|нет
|3|30|7|4|7|нет

Для получения корректных результатов в таблице необходимо внести в программу изменения подсчета количества дней и вывода ответа:

A)
```cpp
count = (1 + days - nday) /7;
printf("%u\n", nday);

```
B)
```cpp
count = 1 + (days - nday) /7;
printf("%u\n", count);

```
C)   
```cpp
count = 1 + (days - nday) % 7;
printf("%u\n", count);

```
D)	
```cpp
count = (1 + days - nday) /7;
printf("%u\n", count);

```
E) Еще один вопрос:
```cpp
count = 1 + (days - nday) /7;
printf("%u\n", nday);

```
F)
```cpp
count = 1 + (days - nday) /7;
printf("%u\n", nday);
3-th code string
```

ANSWER B

## QUIZ 

Студент писал программу для подсчета количества понедельников в месяце. В месяце может быть 28, 30 или 31 день.
Понедельник считается первым днем в неделе, вторник - 2, ..., воскресенье - 7.
Он использовал переменные: **days** - количество дней в месяце, **nday** - дата первого понедельника и **count** - количество понедельников.


Какой тип переменных следует выбрать для корректной работы программы и максимальной экономии памяти (все переменные вместе должны занимать как можно меньшее количество байт)?

A) int
B) short int
C) unsigned short int
D) unsigned int
E) unsigned char

ANSWER E