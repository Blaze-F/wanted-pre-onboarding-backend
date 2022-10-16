# wanted-pre-onboarding-backend
### wanted-pre-onboarding-backend 지원

---
## 사용기술

* Django, SQLite

* view : bootstrap

* IDE : Pycharm
---

## 실행방법

python manage.py migrtate

python manage.py runserver

---
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
    
![image](https://user-images.githubusercontent.com/101803254/196051707-5509799c-b42d-450e-a831-589c9f93cf12.png)


--- 구현중인 사항 ---

6. **사용자는 채용공고에 지원합니다(선택사항 및 가산점요소).**
    
    <aside>
    ➡️ 사용자는 채용공고에 아래와 같이 지원합니다. (가점 요소이며, 필수 구현 요소가 아님)
    
    - 사용자는 1회만 지원 가능합니다.
    </aside>
    
- Unit Test 구현
- README 에 요구사항 분석 및 구현 과정을 작성
- Git commit 메시지 컨벤션


---

### Note


