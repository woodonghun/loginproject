#회원가입 다이얼로그

from PySide2.QtWidgets import QPushButton, QLabel, QLineEdit, QDialog, QWidget

import UI.glob
import UI.signBox


class DlgSign(QWidget):
    def __init__(self):  # 회원가입 dialog 사용
        super().__init__()
        self.dialog = QDialog()
        self.sign()
        self.dialog_close()

    def sign(self):
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

        self.edt_Id_Dialog = QLineEdit(self.dialog)
        self.edt_Id_Dialog.move(60, 30)

        self.edt_Pw_Dialog = QLineEdit(self.dialog)
        self.edt_Pw_Dialog.move(60, 60)

        self.edt_Name_Dialog = QLineEdit(self.dialog)
        self.edt_Name_Dialog.move(60, 90)

        self.dialog.exec()  # show 대신 exec 를 사용 하면 modal 로 동작

    def signup(self):  # 회원가입 OK 클릭
        txt = open("C:\woodonghun/id", 'r')  # 첫 화면 에서 txt 에 저장된 회원 정보 읽음
        self.privacy = txt.read()
        self.privacy = self.privacy.replace('\n', ',')
        self.privacy_list = self.privacy.split(',')
        self.privacy_chunk = [self.privacy_list[i * 3:(i + 1) * 3] for i in range((len(self.privacy_list) + 3 - 1) // 3)]
        # 리스트 분할 https://jsikim1.tistory.com/141 참고

        Id = self.edt_Id_Dialog.text()
        pw = self.edt_Pw_Dialog.text()
        name = self.edt_Name_Dialog.text()

        if Id != '' and pw != '' and name != '':  # 빈칸 없이 입력 했을떄
            j = 0
            for i in range(len(self.privacy_chunk)):
                j += 1
                if Id == self.privacy_chunk[i][0]:  # id 중복 되었을 때
                    UI.signBox.SignBox('중복 되는 id 입니다 다시 입력 하세요.')
                    break

            if j == len(self.privacy_chunk):
                self.privacy = Id, pw, name
                txt = open("C:\woodonghun/id", 'a')
                txt.write(','.join(self.privacy))
                txt.write("\n")
                UI.signBox.SignBox('회원 가입이 완료 되었습니다.')
                self.dialog_close()

        elif Id != '' or pw != '' or name != '':  # 하나 라도 빈칸 있을때
            UI.signBox.SignBox('빈칸 없이 다시 입력 하세요.')

    def dialog_close(self):
        self.dialog.close()
