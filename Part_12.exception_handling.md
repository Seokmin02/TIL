# try except

### 예외 처리
```
try:
    number = int(text)  # 에러가 발생할 가능성이 있는 코드
except: ValueError  # 에러 종류
    print('{}는 숫자가 아닙니다.'.format(text))     # 에러가 발생 했을 경우 처리할 코드
```

### 예외의 이름을 모를 때

```
try :
    list = [] # 에러가 발생할 가능성이 있는 코드
    print(list[0]) 

    text = 'abc'
    number = int(text)
except Exception as ex: # 에러 종류
    print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 함수
```

### 예외 발생 시키기

```
try:
        ...
    raise 에러종류      # 에러 발생 시킬 위치
        ...
exception 에러종류:
    처리할 코드
```

- 많이 사용하면 코드를 읽기 어려워짐

