import time


# 더미 센서 클래스 (가짜 센서 역할)
class DummySensor:

    # 객체 생성 시 초기 환경값 설정
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0,
            'mars_base_external_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,
            'mars_base_internal_oxygen': 0
        }

    # 센서값을 임의로 변경 (실제 센서 대신 값 변화)
    def set_env(self):
        self.env_values['mars_base_internal_temperature'] += 1
        self.env_values['mars_base_external_temperature'] -= 1
        self.env_values['mars_base_internal_humidity'] += 1
        self.env_values['mars_base_external_illuminance'] += 5
        self.env_values['mars_base_internal_co2'] += 1
        self.env_values['mars_base_internal_oxygen'] -= 1

    # 현재 환경값 반환
    def get_env(self):
        self.set_env()  # 값 갱신
        return self.env_values


# 미션 컴퓨터 클래스 (센서 데이터를 받아서 처리)
class MissionComputer:

    # 객체 생성 시 실행 (초기 설정)
    def __init__(self):

        # 현재 환경값 저장 공간
        self.env_values = {
            'mars_base_internal_temperature': 0,
            'mars_base_external_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,
            'mars_base_internal_oxygen': 0
        }

        # 센서 객체 생성 (센서 연결)
        self.ds = DummySensor()

        # 🔥 5분 평균 계산을 위한 데이터 저장소 (리스트)
        self.history = {
            'mars_base_internal_temperature': [],
            'mars_base_external_temperature': [],
            'mars_base_internal_humidity': [],
            'mars_base_external_illuminance': [],
            'mars_base_internal_co2': [],
            'mars_base_internal_oxygen': []
        }

    # 센서 데이터를 가져와서 출력하는 함수
    def get_sensor_data(self):

        count = 0  # 반복 횟수 (5초 기준 → 60번 = 5분)

        # 무한 반복 시작
        while True:

            # 🔥 사용자 입력으로 종료 기능
            user_input = input('종료하려면 q를 입력하세요: ')
            if user_input == 'q':
                print('Sytem stoped....')
                break

            # 1️⃣ 센서에서 최신 환경값 가져오기
            sensor_data = self.ds.get_env()

            # 2️⃣ 가져온 값을 미션 컴퓨터에 저장
            self.env_values = sensor_data

            # 3️⃣ 현재 환경값 출력 (JSON 형태처럼 보임)
            print(self.env_values)

            # 4️⃣ 평균 계산을 위해 값 누적 저장
            for key in self.env_values:
                self.history[key].append(self.env_values[key])

            count += 1  # 반복 횟수 증가

            # 5️⃣ 60번 반복 (5분) 시 평균 계산
            if count == 60:

                print('----- 5분 평균 값 -----')

                # 각 환경값 평균 계산 및 출력
                for key in self.history:
                    values = self.history[key]
                    avg = sum(values) / len(values)
                    print(key, ':', avg)

                # 평균 계산 후 초기화 (다음 5분을 위해)
                self.history = {
                    key: [] for key in self.history
                }

                count = 0  # 카운트 초기화

            # 6️⃣ 5초 대기 후 다시 반복
            time.sleep(5)


# 🔥 MissionComputer 객체 생성 (실제 컴퓨터)
RunComputer = MissionComputer()

# 🔥 센서 데이터 출력 기능 실행 (프로그램 시작)
RunComputer.get_sensor_data()