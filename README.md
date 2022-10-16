# wanted-pre-onboarding-backend
### wanted-pre-onboarding-backend 지원


## 사용기술

* Django, SQLite

* view : bootstrap

* IDE : Pycharm


## 실행방법

python manage.py migrtate

python manage.py runserver


## 구현 요소 

채용공고를 등록합니다. 채용공고를 수정합니다.

![image](https://user-images.githubusercontent.com/101803254/196050125-18f5fe4f-98e8-4590-a4b5-234cd1b27a2f.png)

### - 기업정보와 채용공고는 서로 다른 테이블에 저장됩니다.

채용공고를 삭제합니다.
![image](https://user-images.githubusercontent.com/101803254/196041678-a2758ea5-0e04-449f-95c1-af65b334eae9.png)


**채용공고 목록을 가져옵니다.**
    
    <aside>
    ➡️ 4-1. 사용자는 채용공고 목록을 아래와 같이 확인할 수 있습니다.
    
    </aside>

![image](https://user-images.githubusercontent.com/101803254/196041744-6721d2a4-7efd-4254-af62-456f9d7ca8ab.png)

4-2. 채용공고 검색 기능 구현.

![image](https://user-images.githubusercontent.com/101803254/196041773-8e84493a-bd45-4e3d-a265-759fb16383f3.png)

![image](https://user-images.githubusercontent.com/101803254/196041787-d2d68e82-5c37-4555-b995-5a94462c2429.png)


5. **채용 상세 페이지를 가져옵니다.**
    
    <aside>
    ➡️ 사용자는 채용상세 페이지를 아래와 같이 확인할 수 있습니다.
    
    - “채용내용”이 추가적으로 담겨있음.
    - 해당 회사가 올린 다른 채용공고 가 추가적으로 포함됩니다**(선택사항 및 가산점요소).**
    </aside>
    
![image](https://user-images.githubusercontent.com/101803254/196059803-d377b02d-4b54-4f8b-9d96-0fc09dfd72d3.png)



6. **사용자는 채용공고에 지원합니다(선택사항 및 가산점요소).**
    
    <aside>
    ➡️ 사용자는 채용공고에 아래와 같이 지원합니다. (가점 요소이며, 필수 구현 요소가 아님)
    
    - 사용자는 1회만 지원 가능합니다.
    </aside>
    
![image](https://user-images.githubusercontent.com/101803254/196059160-120ed713-7448-48c0-b8ce-dfc329949586.png)

* ERD (사용한 테이블만)
![preonboard_](https://user-images.githubusercontent.com/101803254/196062301-899e13f8-09ba-4929-bd74-fdf7ccadd54b.png)

* Not yet

- Unit Test 구현
- README 에 요구사항 분석 및 구현 과정을 작성
- Git commit 메시지 컨벤션


---

### Note

요구사항 분석 중에 Company 모델을 따로 정의하도록 되어있어서 로그인 이후 모집공고를 작성하면서 동시에 기업 정보도 작성해서 
폼 두개를 Submit 한번에 처리하도록 구현하였습니다. 

모집공고에 대한 CRUD는 작성, 
Company 모델의 경우 get_or_create() 를 사용, 모든 필드명이 같을경우엔 동일 모델, 하나의 필드라도 다른경우엔 생성하도록 구현하였습니다.

- 해당 회사가 올린 다른 채용공고 기준은 "이름이 동일할 경우" 를 기준으로 구현하였습니다.

후기 : 파이썬은 알고리즘 풀이에만 사용하고, Django로는 처음 만들어보는데, 체감상 소문대로 생산성이 좋은것 같습니다. 
