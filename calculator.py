import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # 창 설정
        self.setWindowTitle('Calculator')
        self.resize(320, 500)

        # -----------------------------
        # 출력창 생성
        # -----------------------------
        self.display = QLabel('0')
        self.display.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.display.setFixedHeight(100)

        # -----------------------------
        # 전체 레이아웃
        # -----------------------------
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)

        # 버튼 레이아웃 (그리드)
        button_layout = QGridLayout()

        # 버튼 구조 (아이폰 계산기 기준)
        buttons = [
            ['AC', '+/-', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
        ]

        # 일반 버튼 생성
        for row, button_row in enumerate(buttons):
            for col, text in enumerate(button_row):
                button = QPushButton(text)
                button.setFixedSize(70, 70)

                # 버튼 클릭 이벤트 연결
                button.clicked.connect(self.button_clicked)

                button_layout.addWidget(button, row, col)

        # -----------------------------
        # 0 버튼 (2칸)
        # -----------------------------
        zero_button = QPushButton('0')
        zero_button.setFixedHeight(70)
        zero_button.clicked.connect(self.button_clicked)
        button_layout.addWidget(zero_button, 4, 0, 1, 2)

        # . 버튼
        dot_button = QPushButton('.')
        dot_button.setFixedSize(70, 70)
        dot_button.clicked.connect(self.button_clicked)
        button_layout.addWidget(dot_button, 4, 2)

        # = 버튼
        equal_button = QPushButton('=')
        equal_button.setFixedSize(70, 70)
        equal_button.clicked.connect(self.button_clicked)
        button_layout.addWidget(equal_button, 4, 3)

        # 레이아웃 합치기
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    # -----------------------------
    # 버튼 클릭 이벤트 처리
    # -----------------------------
    def button_clicked(self):
        button = self.sender()          # 클릭된 버튼 객체
        text = button.text()            # 버튼 문자
        current_text = self.display.text()  # 현재 화면 값

        # AC → 초기화
        if text == 'AC':
            self.display.setText('0')

        # 숫자 입력
        elif text in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if current_text == '0':
                self.display.setText(text)
            else:
                self.display.setText(current_text + text)

        # 소수점 입력
        elif text == '.':
            if '.' not in current_text:
                self.display.setText(current_text + '.')

        # 연산 기호 입력 (계산은 안 함, 표시만)
        elif text in ['+', '-', '×', '÷', '%']:
            self.display.setText(current_text + ' ' + text + ' ')

        # = 버튼 (계산 안 하므로 표시만 유지)
        elif text == '=':
            pass

        # +/- 버튼 (이번 과제에서는 기능 생략)
        elif text == '+/-':
            pass


# -----------------------------
# 프로그램 실행
# -----------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())