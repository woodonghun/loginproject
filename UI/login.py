# 로그인

from PySide2.QtWidgets import QWidget

import UI.glob
import UI.signBox


class Login(QWidget):
    def Login_Event(self):  # 로그인 이벤트
        MsgBox = UI.signBox.SignBox
        txt = open("C:\woodonghun/id", 'r')  # 로그인 눌렀을 때 회원정보 가지고 옴
        self.privacy = txt.read()
        self.privacy = self.privacy.replace('\n', ',')
        self.privacy_list = self.privacy.split(',')
        self.privacy_chunk = [self.privacy_list[i * 3:(i + 1) * 3] for i in
                              range((len(self.privacy_list) + 3 - 1) // 3)]

        if self.edt_Id.text() != '' and self.edt_Pw.text() != '':   # Id Pw 빈칸이 없을때
            j = 0
            for i in range(len(self.privacy_chunk)):
                j += 1

                if self.edt_Id.text() == self.privacy_chunk[i][0]:  # id가 있을떄

                    if self.privacy_chunk[i][1] == self.edt_Pw.text():    # 비밀번호도 같을때

                        MsgBox("{}님 환영합니다.".format(self.privacy_chunk[i][2]))
                        break

                    else:      # 비밀번호 다를때
                        MsgBox("비밀번호가 다릅니다.")
                        break

                elif j == len(self.privacy_chunk) and self.edt_Id.text() != self.privacy_chunk[i][0]:  # dict 에 id가 없을때
                    MsgBox("회원정보가 없습니다.")
                    break

        else:  # id, pw에 빈칸이 있을때
            MsgBox("빈칸 없이 다시 입력 하세요.")
