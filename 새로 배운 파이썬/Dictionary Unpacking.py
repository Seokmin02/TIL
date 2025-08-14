def personal_info(name, age, address):
    print('이름:', name)
    print('나이:', age)
    print('주소:', address)
    
x = {'name': '전석민', 'age' : 30, 'address' : '부산광역시 수영구 남천동'}
personal_info(**x)
personal_info(**{'name': '전석민', 'age' : 30, 'address' : '부산광역시 수영구 남천동'}) 

# **를 두 번 사용하는 이유
personal_info(*x)
