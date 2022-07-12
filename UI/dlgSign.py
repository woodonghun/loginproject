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
        self.privacy = self.privacy.replace('\n', ',')
        self.privacy_list = self.privacy.split(',')
        self.privacy_chunk = [self.privacy_list[i * 3:(i + 1) * 3] for i in range((len(self.privacy_list) + 3 - 1) // 3)]
        print(self.privacy_chunk)
        Id = self.ID_dialog_line.text()
        pw = self.PW_dialog_line.text()
        name = self.name_dialog_line.text()

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
