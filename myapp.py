# 메인

import sys
import UI.glob
import UI.dlgSign
import UI.login
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton


# 회원정보 입력시 발생하는 이슈
# 아이디 없음
# 아이디 패스워드 일치 x
# 아이디 패스워드 일치
# 빈칸이 있는 상태로 등록 했을 때
# 동일한 아이디가 존재 했을때
# 외부에 저장된 아이디가 없을때 생기는 오류

# pickle lib 를 이용 해서 객체를 저장하여 끄고 다시 켜도 id가 존재함
# main과 dialog 클래스 나누기
# 즉 모듈 또는 패키지로 구성하는 것. &&&& 클래스는 직접 호출이 불가능하다
# 피클 사용하지 않고 읽고 쓰기로 구성해보기
# 모달 모달 리스 이해 하기


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        sign = UI.dlgSign.DlgSign

        label_id = QLabel("ID", self)
        label_id.move(20, 35)
        label_pw = QLabel("PW", self)
        label_pw.move(20, 65)

        self.ID_Qline = QLineEdit(self)
        self.ID_Qline.move(60, 30)

        self.PW_Qline = QLineEdit(self)
        self.PW_Qline.move(60, 60)

        btn_login = QPushButton('Login', self)
        btn_login.setGeometry(220, 30, 50, 50)
        btn_login.clicked.connect(self.Log_Bt_Clicked)    # 로그인 이벤트

        btn_signup = QPushButton('Sign up', self)
        btn_signup.move(20, 90)
        btn_signup.clicked.connect(sign)  # 회원가입 dialog 출력

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def Log_Bt_Clicked(self):
        UI.login.Login.Login_Event(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
