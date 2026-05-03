import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QVBoxLayout
)


class Calculator:
    '''
    계산기의 실제 동작을 담당하는 클래스
    숫자 입력, 소수점 입력, 사칙연산, 초기화, 부호 변경, 퍼센트, 결과 계산 기능을 처리한다.
    '''

    def __init__(self):
        '''
        계산기에 필요한 기본 상태를 초기화한다.

        current_value:
            현재 화면에 표시되는 값
        first_operand:
            첫 번째 숫자
        operator:
            선택된 연산자
        waiting_for_second_operand:
            연산자 입력 후 다음 숫자를 새로 받을 준비 상태인지 여부
        '''
        self.current_value = '0'
        self.first_operand = None
        self.operator = None
        self.waiting_for_second_operand = False

    def reset(self):
        '''
        계산기 상태를 모두 초기화한다.
        AC 버튼과 연결되는 기능이다.
        '''
        self.current_value = '0'
        self.first_operand = None
        self.operator = None
        self.waiting_for_second_operand = False
        return self.current_value

    def add(self, a, b):
        '''
        두 수를 더한 결과를 반환한다.
        '''
        return a + b

    def subtract(self, a, b):
        '''
        두 수를 뺀 결과를 반환한다.
        '''
        return a - b

    def multiply(self, a, b):
        '''
        두 수를 곱한 결과를 반환한다.
        '''
        return a * b

    def divide(self, a, b):
        '''
        두 수를 나눈 결과를 반환한다.
        0으로 나누는 경우는 Error를 반환한다.
        '''
        if b == 0:
            return 'Error'
        return a / b

    def negative_positive(self):
        '''
        현재 화면에 있는 숫자의 부호를 반대로 바꾼다.
        예: 5 -> -5, -5 -> 5
        '''
        if self.current_value == 'Error':
            return self.current_value

        if self.current_value != '0':
            if self.current_value.startswith('-'):
                self.current_value = self.current_value[1:]
            else:
                self.current_value = '-' + self.current_value

        return self.current_value

    def percent(self):
        '''
        현재 화면의 값을 100으로 나누어 퍼센트 값으로 변환한다.
        예: 50 -> 0.5
        '''
        if self.current_value == 'Error':
            return self.current_value

        try:
            value = float(self.current_value)
            value = value / 100
            self.current_value = self.format_number(value)
        except ValueError:
            self.current_value = 'Error'

        return self.current_value

    def input_number(self, num):
        '''
        숫자 버튼 입력을 처리한다.
        숫자 키를 누를 때마다 화면에 숫자가 누적되도록 구현한다.
        '''
        if self.current_value == 'Error':
            self.current_value = '0'

        # 연산자 입력 직후라면 새로운 숫자를 입력해야 하므로 기존 값을 덮어쓴다.
        if self.waiting_for_second_operand:
            self.current_value = str(num)
            self.waiting_for_second_operand = False
        # 현재 화면이 0이면 새 숫자로 교체한다.
        elif self.current_value == '0':
            self.current_value = str(num)
        # 그 외에는 뒤에 숫자를 이어붙인다.
        else:
            self.current_value += str(num)

        return self.current_value

    def input_decimal(self):
        '''
        소수점 버튼 입력을 처리한다.
        이미 소수점이 있는 경우에는 추가 입력되지 않도록 한다.
        '''
        if self.current_value == 'Error':
            self.current_value = '0'

        # 연산자 입력 직후 바로 소수점을 누르면 0.부터 시작하게 한다.
        if self.waiting_for_second_operand:
            self.current_value = '0.'
            self.waiting_for_second_operand = False
            return self.current_value

        # 현재 값에 소수점이 없을 때만 추가한다.
        if '.' not in self.current_value:
            self.current_value += '.'

        return self.current_value

    def set_operator(self, op):
        '''
        연산자 버튼 입력을 처리한다.
        현재 화면 값을 첫 번째 숫자로 저장하고,
        어떤 연산을 할지 operator에 기록한다.
        '''
        if self.current_value == 'Error':
            return self.current_value

        try:
            current = float(self.current_value)
        except ValueError:
            self.current_value = 'Error'
            return self.current_value

        # 첫 번째 연산이면 첫 번째 숫자를 저장한다.
        if self.first_operand is None:
            self.first_operand = current
        # 이미 연산 중인데 두 번째 숫자까지 입력된 상태라면
        # 먼저 현재까지의 결과를 계산한 뒤 연산을 이어간다.
        elif self.operator is not None and not self.waiting_for_second_operand:
            result = self.equal()
            if result == 'Error':
                return result
            self.first_operand = float(self.current_value)

        self.operator = op
        self.waiting_for_second_operand = True
        return self.current_value

    def equal(self):
        '''
        현재 저장된 첫 번째 숫자, 연산자, 현재 화면의 두 번째 숫자를 이용해
        최종 계산 결과를 반환한다.
        '''
        if self.operator is None or self.first_operand is None:
            return self.current_value

        if self.current_value == 'Error':
            return self.current_value

        try:
            second_operand = float(self.current_value)
        except ValueError:
            self.current_value = 'Error'
            return self.current_value

        if self.operator == '+':
            result = self.add(self.first_operand, second_operand)
        elif self.operator == '-':
            result = self.subtract(self.first_operand, second_operand)
        elif self.operator == '×':
            result = self.multiply(self.first_operand, second_operand)
        elif self.operator == '÷':
            result = self.divide(self.first_operand, second_operand)
        else:
            self.current_value = 'Error'
            return self.current_value

        if result == 'Error':
            self.current_value = 'Error'
        else:
            self.current_value = self.format_number(result)

        # 계산이 끝났으므로 연산 상태를 초기화한다.
        self.first_operand = None
        self.operator = None
        self.waiting_for_second_operand = False

        return self.current_value

    def format_number(self, num):
        '''
        계산 결과를 화면에 보기 좋게 표시하기 위해 문자열 형태로 변환한다.
        - 정수면 소수점 없이 출력
        - 실수면 소수점 6자리 이하로 반올림
        - 불필요한 0 제거
        '''
        if isinstance(num, str):
            return num

        # 정수 형태이면 예: 5.0 -> 5
        if num.is_integer():
            return str(int(num))

        rounded_num = round(num, 6)
        text = str(rounded_num)

        # 예: 3.140000 -> 3.14 / 2.000000 -> 2
        if '.' in text:
            text = text.rstrip('0').rstrip('.')

        return text


class CalculatorUI(QWidget):
    '''
    계산기의 UI를 담당하는 클래스
    버튼 화면 구성, 버튼 클릭 이벤트, 결과 화면 표시를 처리한다.
    '''

    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.init_ui()

    def init_ui(self):
        '''
        계산기 화면을 구성한다.
        디스플레이와 버튼들을 배치한다.
        '''
        self.setWindowTitle('Calculator')
        self.setFixedSize(360, 540)

        main_layout = QVBoxLayout()
        grid_layout = QGridLayout()

        # 계산 결과를 보여주는 화면
        self.display = QLineEdit()
        self.display.setText('0')
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(100)
        self.display.setFont(QFont('Arial', 28))

        # 버튼 목록
        buttons = [
            ['AC', '+/-', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]

        # 버튼 위치
        positions = {
            'AC': (0, 0),
            '+/-': (0, 1),
            '%': (0, 2),
            '÷': (0, 3),
            '7': (1, 0),
            '8': (1, 1),
            '9': (1, 2),
            '×': (1, 3),
            '4': (2, 0),
            '5': (2, 1),
            '6': (2, 2),
            '-': (2, 3),
            '1': (3, 0),
            '2': (3, 1),
            '3': (3, 2),
            '+': (3, 3),
            '0': (4, 0),
            '.': (4, 2),
            '=': (4, 3)
        }

        # 버튼 생성 및 클릭 이벤트 연결
        for row in buttons:
            for button_text in row:
                button = QPushButton(button_text)
                button.setFixedSize(80, 80)
                button.setFont(QFont('Arial', 18))
                button.clicked.connect(self.on_button_clicked)

                # 0 버튼은 가로로 길게 배치
                if button_text == '0':
                    grid_layout.addWidget(button, 4, 0, 1, 2)
                    button.setFixedSize(170, 80)
                else:
                    row_pos, col_pos = positions[button_text]
                    grid_layout.addWidget(button, row_pos, col_pos)

        main_layout.addWidget(self.display)
        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    def on_button_clicked(self):
        '''
        버튼이 클릭될 때 어떤 버튼인지 확인하고,
        해당 기능에 맞는 Calculator 메소드를 호출한다.
        '''
        button = self.sender()
        text = button.text()

        if text.isdigit():
            result = self.calculator.input_number(text)
        elif text == '.':
            result = self.calculator.input_decimal()
        elif text in ['+', '-', '×', '÷']:
            result = self.calculator.set_operator(text)
        elif text == '=':
            result = self.calculator.equal()
        elif text == 'AC':
            result = self.calculator.reset()
        elif text == '+/-':
            result = self.calculator.negative_positive()
        elif text == '%':
            result = self.calculator.percent()
        else:
            result = 'Error'

        self.display.setText(result)
        self.adjust_font_size()

    def adjust_font_size(self):
        '''
        보너스 과제:
        결과값 길이에 따라 폰트 크기를 조절하여
        화면에 한 번에 보일 수 있도록 한다.
        '''
        text_length = len(self.display.text())

        if text_length <= 8:
            font_size = 28
        elif text_length <= 12:
            font_size = 22
        elif text_length <= 16:
            font_size = 18
        else:
            font_size = 14

        self.display.setFont(QFont('Arial', font_size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorUI()
    window.show()
    sys.exit(app.exec_())