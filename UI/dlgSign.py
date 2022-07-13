# 회원가입 다이얼로그

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
        btn_ok = QPushButton('ok', self.dialog)
        btn_ok.move(20, 120)
        btn_ok.clicked.connect(self.signup)  # OK 버튼 눌렀을 때 회원가입

        btn_cancel = QPushButton('cancel', self.dialog)
        btn_cancel.move(100, 120)
        btn_cancel.clicked.connect(self.dialog_close)

        label_id_dialog = QLabel("ID", self.dialog)
        label_id_dialog.move(20, 35)
        label_pw_dialog = QLabel("PW", self.dialog)
        label_pw_dialog.move(20, 65)
        label_name_dialog = QLabel("name", self.dialog)
        label_name_dialog.move(20, 95)

        self.edt_id_dialog = QLineEdit(self.dialog)
        self.edt_id_dialog.move(60, 30)

        self.edt_pw_dialog = QLineEdit(self.dialog)
        self.edt_pw_dialog.move(60, 60)

        self.edt_name_dialog = QLineEdit(self.dialog)
        self.edt_name_dialog.move(60, 90)

        self.dialog.exec()  ####### show 대신 exec 를 사용 하면 modal 로 동작 #######

    def signup(self):  # 회원가입 OK 클릭
        MsgBox = UI.signBox.SignBox
        txt = open("C:\woodonghun/id", 'r')  # 첫 화면 에서 txt 에 저장된 회원 정보 읽음
        self.privacy = txt.read()
        self.privacy = self.privacy.replace('\n', ',')
        self.privacy_list = self.privacy.split(',')
        self.privacy_chunk = [self.privacy_list[i * 3:(i + 1) * 3] for i in range((len(self.privacy_list) + 3 - 1) // 3)]
        # 리스트 분할 https://jsikim1.tistory.com/141 참고

        Id = self.edt_id_dialog.text()
        pw = self.edt_pw_dialog.text()
        name = self.edt_name_dialog.text()

        if Id != '' and pw != '' and name != '':  # 빈칸 없이 입력 했을떄
            j = 0
            for i in range(len(self.privacy_chunk)):
                j += 1
                if Id == self.privacy_chunk[i][0]:  # id 중복 되었을 때
                    MsgBox('중복 되는 id 입니다 다시 입력 하세요.')
                    break

            if j == len(self.privacy_chunk):    # for문에서 id중복을 찾지 못하였을때 j와 len 의 값을 비교해서 if문 들어감
                self.privacy = Id, pw, name
                txt = open("C:\woodonghun/id", 'a')
                txt.write(','.join(self.privacy)+'\n')
                MsgBox('회원 가입이 완료 되었습니다.')
                self.dialog_close()

        else:  # 하나 라도 빈칸 있을때
            MsgBox('빈칸 없이 다시 입력 하세요.')

    def dialog_close(self):
        self.dialog.close()
