# 메세지박스

from PySide2.QtWidgets import QMessageBox


def SignBox(i):  # 로그인 박스 함수
    signBox = QMessageBox()
    signBox.setWindowTitle("Sign up")
    signBox.setText(i)

    signBox.setIcon(QMessageBox.Information)
    signBox.setStandardButtons(QMessageBox.Ok)
    signBox.exec_()