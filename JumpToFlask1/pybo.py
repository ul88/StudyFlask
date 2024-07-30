from flask import Flask

app = Flask(__name__) # 플라스크 애플리케이션을 생성하는 코드 __name__에 모듈명이 담긴다.
                      # 즉, 이 코드를 실행하면 __name__에 pybo라는 문자열이 담기게 된다.

# 데코레이터 : 기존 함수를 변경하지 않고 추가 기능을 덧붙일 수 있도록 해주는 함수
@app.route('/') # URL과 플라스크 코드를 매핑하는 데코레이터
def hello_pybo():
    return "Hello, Pybo!"

if __name__ == "__main__":
    app.run(debug=True)