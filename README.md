# B2Tech 근태 관리 프로그램(backend)🚀️
## 1. 프로젝트 소개
### 프로젝트 일정✨️
- 2021.06.07 ~ ~07.02
### 🌈️프로젝트 팀원
- frontend
  - 김유림🤩️
  - 안정현😚️
- backend
  - 최우석🧐️

### 프로젝트 설명
사용자들의 근태 관리를 위한 프로그램\
사용자는 직원, 관리자로 구분

### 구현된 기능
- **직원**\
출/퇴근 기록\
로그인(JWT)\
마이 페이지 : 개인 정보 및 최근 1주일간 근태 기록 확인\
휴가 및 근무제도 기안 신청
- **관리자**\
모든 직원의 일정 관리\
모든 직원의 개인 정보 관리

### 🛠Stack
**Server**\
`Django`:3.2.4\
`Python`:3.9\
**Database**\
`Mysql`\
**Front**\
`react` `javascript`


## 프로젝트 사용 방법(API)
- miniconda site에서 스크립트 링크 설치(linux 기준)
- `wget 스크립트 링크` miniconda 설치
- `chmod +x 미니콘다 파일명` 실행 권한 부여
- `./미니콘다 파일명` 실행
- `source ./bashrc`
- `sudo apt-get update` `sudo apt-get upgrade`
- `sudo apt-get install gcc` gcc 설치
- `sudo apt-get libmysqlclient-deb` mysql client 설치
- `conda create -n schedule python=3.9` 콘다로 schedule 프로젝트 환경 생성
- `conda activate schedule` schedule 환경으로 셋팅 
- 프로젝트 repository clone 실행
- manage.py가 있는 디렉토리에 my_settings.py를 아래와 같이 작성
```python
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB 이름',
        'USER': 'root로 설정',
        'PASSWORD': '비밀번호',
        'HOST': 'DB의 엔드포인트 주소(RDS)',
        'PORT': '3306',
    }
}
SECRET = 'settings에 있는 SECRET_KEY값'
KEY = '32자리 문자열'
```
- `pip install -r requirements.txt` 패키지 설치
- `python manage.py runserver 0.0.0.0:8000` 으로 서버 실행
### API(업데이트 예정)
**출퇴근 등록**
> POST http://{{IP}}:{{PORT}}/users/20210005/schedules

권한: 사번이 있는 모든 유저\
Request.body : None
```json
# 만약 아직 출근을 하지 않았다면 schedule 데이터 생성
{
  "user":"20210005",
  "work_type":"정상근무",
  "created_at":"현재 날짜와 시간",
  "updated_at":None,
  "get_in_time":"직원의 출근 시간",
  "get_off_time":"직원의 퇴근 시간"
}
# 출근을 했다면
{
  "user":"20210005",
  ...
  "updated_at":"현재 날짜와 시간",
  ...
}
```
**로그인**
> POST http://{{IP}}:{{PORT}}/users/login

권한: 사번이 있는 모든 유저\
Request.body : 
```json
{
  "employee_number":"20210005",
  "password":"5555555"
}
```
Response.header :
```json
{
  "Authorization":{# jwt 토큰 payload
    "employee_number":"20210005",
    "permissions":"허용 api",
    "iat":"유효기간(현재 시간및 날짜를 초로 환산)"
  }
}
```
**마이페이지**
> GET http://{{IP}}:{{PORT}}/users/20210005/mypage?monday=2021-6-21&sunday=2021-6-27\
Params : monday, sunday\

권한: 유효한 토큰을 가진 유저\
Request.header :
```json
{
  "Authorization": "jwt 토큰"
}
```
Response.data :
```json
{
    "name": "이름",
    "employee_number": "20210003",
    "roles": {
        "부서": "개발",
        "직책": "사원"
    },
    "work_in": "오늘 출근 시간",
    "work_out": "오늘 퇴근 시간",
    "work_time_list": "params에 적힌 기간 동안 일한 시간 리스트",
    "total_work_in_week": "총 일한 시간"
}
```
**ME**
> http://{{IP}}:{{PORT}}/users/me


