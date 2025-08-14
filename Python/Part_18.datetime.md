# datetime

```
import datetime
datetime.datetime.now()
```
결과 : datetime.datetime(2025, 7, 16, 17, 17, 59, 810882)
<br><br>

```
start_time = datetime.datetime.now()
type(start_time)
```
결과 : `<class 'datetime.datetime'>`
<br><br>
```
start_time.replace(year = 2025, month = 7, day = 19)
```
- 변경하는 값에 해당하는 새로운 datetime class를 만들어서 return
<br><br>
- start_time을 바꾸기 위해서는
```
start_time = start_time.replace(")
```
<br><br>
```
start_time = datetime.datetime(2026,2,1)
start_time
```
결과: datetime.datetime(2026, 2, 1, 0, 0)

#### 지금부터 2월 1일까지 시간이 얼마나 남아있는지 알기 위해서는?
=> 빼기 연산 지원

```
how_long = start_time - datetime.datetime.now()
type(how_long)
```
결과 : class 'datetime.timedelta'
<br><br>
```
how_long.days
```
결과 : 9 
<br><br>
```
how_long.seconds
```
결과 : 33639
<br><br>
```
"2월 1일까지는 {}일 {}시간이 남았습니다.".format(how_long.days, how_long.seconds//3600)
```
결과: '2월 1일까지는 9일 9시간이 남았습니다.'

<br><br>
# timedelta

```
hundred = datetime.timedelta(days = 100)
datetime.datetime.now() + hundred
```
결과 : datetime.datetime(2016, 5, 2, 22, 4, 38, 874884)
<br><br>
```
type(datetime.datetime.now())
```
결과 : class 'datetime.datetime' => 다른 type끼리 연산 가능
<br><br>

```
hundred_before = datetime.timedelta(days = -100)
datetime.datetime.now() + hundred_before
```
결과 : datetime.datetime(2015, 10, 15, 22, 5, 27, 58908)
<br><br>

```
datetime.datetime.now() - hundred
```
결과 : 위와 동일 => hundred 자체를 더하거나 빼 줄 수 있음
<br><br>
```
tomorrow = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + datetime.timedelta(days=1)
```
결과 : datetime.datetime(2016, 1, 24, 9, 0, 0, 347017)  