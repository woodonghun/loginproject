import sys

from PySide2.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QLabel, QPushButton, QDialog


# 예외 처리
# 아이디 없음
# 아이디 패스워드 일치 x
# 아이디 패스워드 일치
# 빈칸이 있는 상태로 등록 했을 때
# 동일한 아이디가 존재 했을때
# 외부에 저장된 아이디가 없을때 생기는 오류

# pickle lib 를 이용 해서 객체를 저장하여 끄고 다시 켜도 id가 존재함
# main과 dialog 클래스 나누기 패키지?? 모듈로 이용??
# 다른 라이브러리 (피클,csv) 사용하지 않고 id 등록을 읽고 쓰기로 구성해보기
# 모달 모달 리스 이해 하기
# 총 실습 기간 3일 22/7/8 ~ 22/7/11

class All(QWidget):
    privacy = ()
    privacy_list = []
    privacy_chunk = []

    def __init__(self):
        super().__init__()
        self.dialog = QDialog()
        self.initUI()

    def initUI(self):
        label_id = QLabel("ID", self)
        label_id.move(20, 35)
        label_pw = QLabel("PW", self)
        label_pw.move(20, 65)

        self.edt_id = QLineEdit(self)
        self.edt_id.move(60, 30)

        self.edt_pw = QLineEdit(self)
        self.edt_pw.move(60, 60)

        btn_login = QPushButton('Login', self)
        btn_login.setGeometry(220, 30, 50, 50)
        btn_login.clicked.connect(self.Login_Event)  # 로그인 messagebox

        btn_signUp = QPushButton('Sign up', self)
        btn_signUp.move(20, 90)
        btn_signUp.clicked.connect(self.dialog_open)  # 회원가입 dialog 출력

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def Login_Event(self):  # 로그인 이벤트
        txt = open("C:\woodonghun/id", 'r')  # 로그인 눌렀을 때 회원정보 가지고 옴
        self.privacy = txt.read()
        self.privacy = self.privacy.replace('\n', ',')
        self.privacy_list = self.privacy.split(',')
        self.privacy_chunk = [self.privacy_list[i * 3:(i + 1) * 3] for i in
                              range((len(self.privacy_list) + 3 - 1) // 3)]

        if self.edt_id.text() != '' and self.edt_pw.text() != '':   # Id Pw 빈칸이 없을때
            j = 0
            for i in range(len(self.privacy_chunk)):
                j += 1

                if self.edt_id.text() == self.privacy_chunk[i][0]:  # id가 있을떄

                    if self.privacy_chunk[i][1] == self.edt_pw.text():    # 비밀번호도 같을때
                        self.signbox("{}님 환영합니다.".format(self.privacy_chunk[i][2]))
                        break

                    else:  # dict 에 id가 없을때         # 비밀번호 다를때
                        self.signbox("비밀번호가 다릅니다.")
                        break

                elif j == len(self.privacy_chunk):      # 회원 정보가 없을때 for문 / 탈출하는 동안 id가 없으면 j = len 이용하여 확인
                    self.signbox("회원정보가 없습니다.")
                    break

        else:  # id, pw에 빈칸이 있을때
            self.signbox("빈칸 없이 다시 입력 하세요.")

    def signbox(self, i):  # 로그인 박스 함수
        signBox = QMessageBox()
        signBox.setWindowTitle("Sign up")
        signBox.setText(i)

        signBox.setIcon(QMessageBox.Information)
        signBox.setStandardButtons(QMessageBox.Ok)
        signBox.exec_()

    def dialog_open(self):  # 회원가입 dialog 사용
        btn_Ok = QPushButton('ok', self.dialog)
        btn_Ok.move(20, 120)
        btn_Ok.clicked.connect(self.signup)  # OK 버튼 눌렀을 때 회원가입

        btn_Cancel = QPushButton('cancel', self.dialog)
        btn_Cancel.move(100, 120)
        btn_Cancel.clicked.connect(self.dialog_close)

        label_Id_Dialog = QLabel("ID", self.dialog)
        label_Id_Dialog.move(20, 35)
        label_Pw_Dialog = QLabel("PW", self.dialog)
        label_Pw_Dialog.move(20, 65)
        label_Name_Dialog = QLabel("name", self.dialog)
        label_Name_Dialog.move(20, 95)

        self.edt_id_dialog = QLineEdit(self.dialog)
        self.edt_id_dialog.move(60, 30)

        self.edt_pw_dialog = QLineEdit(self.dialog)
        self.edt_pw_dialog.move(60, 60)

        self.edt_name_dialog = QLineEdit(self.dialog)
        self.edt_name_dialog.move(60, 90)

        self.dialog.exec()  # show 대신 exec 를 사용 하면 modal 로 동작

    def signup(self):  # 회원가입 OK 클릭
        txt = open("C:\woodonghun/id", 'r')  # 첫 화면 에서 txt 에 저장된 회원 정보 읽음
        self.privacy = txt.read()
        self.privacy = self.privacy.replace('\n', ',')
        self.privacy_list = self.privacy.split(',')
        self.privacy_chunk = [self.privacy_list[i * 3:(i + 1) * 3] for i in
                              range((len(self.privacy_list) + 3 - 1) // 3)]

        # 리스트 분할 https://jsikim1.tistory.com/141 참고

        Id = self.edt_id_dialog.text()
        pw = self.edt_pw_dialog.text()
        name = self.edt_name_dialog.text()

        if Id != '' and pw != '' and name != '':  # 빈칸 없이 입력 했을떄
            j = 0
            for i in range(len(self.privacy_chunk)):
                j += 1
                if Id == self.privacy_chunk[i][0]:  # id 중복 되었을 때
                    self.signbox('중복 되는 id 입니다 다시 입력 하세요.')
                    break

            if j == len(self.privacy_chunk):    # for문에서 id중복을 찾지 못하였을때 j와 len 의 값을 비교해서 if문 들어감
                self.privacy = Id, pw, name
                txt = open("C:\woodonghun/id", 'a')
                txt.write(','.join(self.privacy)+'\n')  # txt 에 dict 로 id, pw, name 저장
                self.signbox('회원 가입이 완료 되었습니다.')
                self.dialog.close()

        elif Id != '' or pw != '' or name != '':  # 하나 라도 빈칸 있을때
            self.signbox('빈칸 없이 다시 입력 하세요.')

    def dialog_close(self):
        self.dialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = All()
    sys.exit(app.exec_())