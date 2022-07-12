import sys

from PySide2.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QLabel, QPushButton, QDialog


# 회원정보 입력시 발생하는 이슈
# 아이디 없음
# 아이디 패스워드 일치 x
# 아이디 패스워드 일치
# 빈칸이 있는 상태로 등록 했을 때
# 동일한 아이디가 존재 했을때
# 외부에 저장된 아이디가 없을때 생기는 오류

# pickle lib 를 이용 해서 객체를 저장하여 끄고 다시 켜도 id가 존재함
# main과 dialog 클래스 나누기 패키지?? 모듈로 이용??
# 피클 사용하지 않고 읽고 쓰기로 구성해보기
# 모달 모달 리스 이해 하기


class MyApp(QWidget):
    privacy = ()
    privacy_list = []
    privacy_chunk = []

    def __init__(self):
        super().__init__()
        self.dialog = QDialog()
        self.initUI()

    def initUI(self):
        ID_QLabel = QLabel("ID", self)
        ID_QLabel.move(20, 35)
        PW_QLabel = QLabel("PW", self)
        PW_QLabel.move(20, 65)

        self.ID_Qline = QLineEdit(self)
        self.ID_Qline.move(60, 30)

        self.PW_Qline = QLineEdit(self)
        self.PW_Qline.move(60, 60)

        Login_BT = QPushButton('Login', self)
        Login_BT.setGeometry(220, 30, 50, 50)
        Login_BT.clicked.connect(self.Login_Event)  # 로그인 messagebox

        Sign_Up_BT = QPushButton('Sign up', self)
        Sign_Up_BT.move(20, 90)
        Sign_Up_BT.clicked.connect(self.dialog_open)  # 회원가입 dialog 출력

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def Login_Event(self):  # 로그인 이벤트
        txt = open("C:\woodonghun/id", 'r')  # 로그인 눌렀을 때 회원정보 가지고 옴
        self.privacy = txt.read()
        self.privacy_list = self.privacy.split(',')

        self.privacy_chunk = [self.privacy_list[i * 3:(i + 1) * 3] for i in
                              range((len(self.privacy_list) + 3 - 1) // 3)]
        print(self.privacy_chunk)
        if self.ID_Qline.text() != '' and self.PW_Qline.text() != '':   # Id Pw 빈칸이 없을때
            j = 0
            for i in range(len(self.privacy_chunk)):
                j += 1

                if self.ID_Qline.text() == self.privacy_chunk[i][0]:  # id가 있을떄
                    print(self.privacy_chunk[i][0])

                    if self.privacy_chunk[i][1] == self.PW_Qline.text():    # 비밀번호도 같을때
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
        ok = QPushButton('ok', self.dialog)
        ok.move(20, 120)
        ok.clicked.connect(self.signup)  # OK 버튼 눌렀을 때 회원가입

        cancel = QPushButton('cancel', self.dialog)
        cancel.move(100, 120)
        cancel.clicked.connect(self.dialog_close)

        ID_dialog_Label = QLabel("ID", self.dialog)
        ID_dialog_Label.move(20, 35)
        PW_dialog_Label = QLabel("PW", self.dialog)
        PW_dialog_Label.move(20, 65)
        name_dialog_Label = QLabel("name", self.dialog)
        name_dialog_Label.move(20, 95)

        self.ID_dialog_line = QLineEdit(self.dialog)
        self.ID_dialog_line.move(60, 30)

        self.PW_dialog_line = QLineEdit(self.dialog)
        self.PW_dialog_line.move(60, 60)

        self.name_dialog_line = QLineEdit(self.dialog)
        self.name_dialog_line.move(60, 90)

        self.dialog.exec()  # show 대신 exec 를 사용 하면 modal 로 동작

    def signup(self):  # 회원가입 OK 클릭
        txt = open("C:\woodonghun/id", 'r')  # 첫 화면 에서 txt 에 저장된 회원 정보 읽음
        self.privacy = txt.read()
        self.privacy_list = self.privacy.split(',')

        self.privacy_chunk = [self.privacy_list[i * 3:(i + 1) * 3] for i in
                              range((len(self.privacy_list) + 3 - 1) // 3)]

        # 리스트 분할 https://jsikim1.tistory.com/141 참고

        Id = self.ID_dialog_line.text()
        pw = self.PW_dialog_line.text()
        name = self.name_dialog_line.text()

        if Id != '' and pw != '' and name != '':  # 빈칸 없이 입력 했을떄
            j = 0
            for i in range(len(self.privacy_chunk)):
                j += 1
                if Id == self.privacy_chunk[i][0]:  # id 중복 되었을 때
                    self.signbox('중복 되는 id 입니다 다시 입력 하세요.')
                    break

            if j == len(self.privacy_chunk):    # for문에서 id중복을 찾지 못하였을때 j와 len 의 값을 비교해서 if문 들어감
                self.privacy = Id, pw, name
                txt = open("/id", 'a')
                txt.write(','.join(self.privacy)+',')  # txt 에 dict 로 id, pw, name 저장
                self.signbox('회원 가입이 완료 되었습니다.')
                self.dialog.close()

        elif Id != '' or pw != '' or name != '':  # 하나 라도 빈칸 있을때
            self.signbox('빈칸 없이 다시 입력 하세요.')

    def dialog_close(self):
        self.dialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())