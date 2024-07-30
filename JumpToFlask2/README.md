# 2장

## 플라스크 프로젝트 구조
플라스크에는 구조에 대한 규칙이 없으므로 구성할 때 고민을 좀 더 해야한다.

## 데이터 베이스 models.py
파이보 프로젝트는 ORM(object relational mapping)을 지원하는 파이썬 데이터베이스 도구인 SQLAlchemy를 사용한다. SQLAlchemy는 모델 기반으로 데이터베이스를 처리한다.

## 폼 처리 forms.py
파이보 프로젝트는 웹 브라우저에서 서버로 전송된 폼을 처리할 때 WTForms라는 라이브러리를 사용한다. WTForms 역시 모델 기반으로 폼을 처리한다. 그래서 폼 클래스를 정의할 forms.py 파일이 필요하다.

## 화면 구성 views
pybo.py 파일에 작성했던 hello_pybo 함수의 역할은 화면 구성이었다. views 디렉터리에는 바로 이런 함수들로 구성된 뷰 파일들을 저장한다. 파이보 프로젝트에는 기능에 따라 main_views.py, question_views.py, answer_views.py 등의 뷰 파일을 만들 것이다.

## CSS, JS, IMG 등 static
static 디렉터리는 파이보 프로젝트의 스타일시트(.css), 자바스크립트(.js) 그리고 이미지 파일(.jpg, .png) 등을 저장한다.

## HTML은 templates
templates 디렉터리에는 파이보의 질문 목록, 질문 상세 등의 HTML 파일을 저장한다. 파이보 프로젝트는 question_list.html, question_detail.html과 같은 템플릿 파일을 만들어 사용할 것이다.

## 프로젝트 설정 config.py
config.py 파일은 파이보 프로젝트의 환경을 설정한다. 파이보 프로젝트의 환경변수, 데이터베이스 등의 설정을 이 파일에 저장한다.