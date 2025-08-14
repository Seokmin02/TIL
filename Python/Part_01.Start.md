# Window PowerShell에서 python 파일 실행하기

## Powershell 명령
- ls: 현재 디렉토리(폴더)의 내용을 확인하는 명령
- cd: powershell에서 현재 디렉토리(폴더)를 바꾸는 명령

#### Example : powershell에서 Hello world실행
1) powershell실행
2) ls 명령어를 통해 디렉토리 확인
3) 실행할 파일이 있는 위치로 디렉토리를 변경
    - cd C:\Users\smlab\SeokminWorkSpace\asdf\TeamLabStudy  
      => 결과 : PS C:\Users\smlab\SeokminWorkSpace\asdf\TeamLabStudy>
4) python 실행파일이름.py 입력 후 엔터
   - PS C:\Users\smlab\SeokminWorkSpace\asdf\TeamLabStudy> python Helloworld.py  
        Hello, World!