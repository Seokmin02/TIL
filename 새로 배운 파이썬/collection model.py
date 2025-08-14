# 예제1 count하기
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

# 위 리스트에 IBM과 GOOG가 두개씩 있는데 종목별로 합산해보자.
# 해법 : counter 사용

from collections import Counter
total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares

print(total_shares['IBM'])      # 150
print(total_shares['AA'])       # 50

# 예제2 : 일대다 (One-Many) 매핑
# 하나의 키를 여러 개의 값에 매핑하려고 함
# 해법 : defaultdict 사용

from collections import defaultdict
holdings = defaultdict(list)
for name, share, price in portfolio:
    holdings[name].append((shares, price))

print(holdings['IBM']) # [(50, 91.1), (50, 45.23)]
print(holdings['GOOG']) # [(50, 490.1), (50, 572.45)]
# defaultdict을 사용하면 키에 액세스할 때마다 기본값을 얻는다.


# 예제3. tuple() vs namedtuple()

# tuple()
a = ('John', 24, '남')
b = ('Sally', 28, '여')

for name, age, gender in [a,b]:
    print("{}은(는) {}세 {}성 입니다.".format(name, age, gender))

'''
결과:
John은(는) 24세 남성입니다.
Sally은(는) 28세 여성입니다.
'''

import collections

# namedtuple()
Person = collections.namedtuple("Person","name age gender")

P1 = Person(name = 'John', age = 24, gender = '남')
P2 = Person(name = 'Sally', age = 28, gender = '여')

for name, age, gender in [P1, P2]:
    print("{}은(는) {}세 {}성 입니다.")

'''
결과:
John은(는) 24세 남성입니다.
Sally은(는) 28세 여성입니다.
'''

print(P1.name, P1.age, P1.gender)
print(P2.name, P2.age, P2.gender)