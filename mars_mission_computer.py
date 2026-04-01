import time


# 더미 센서 클래스 (가짜 센서)
class DummySensor:

    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0,
            'mars_base_external_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,
            'mars_base_internal_oxygen': 0
        }

    # 값이 계속 변하도록 설정 (테스트용)
    def set_env(self):
        self.env_values['mars_base_internal_temperature'] += 1
        self.env_values['mars_base_external_temperature'] -= 1
        self.env_values['mars_base_internal_humidity'] += 1
        self.env_values['mars_base_external_illuminance'] += 5
        self.env_values['mars_base_internal_co2'] += 1
        self.env_values['mars_base_internal_oxygen'] -= 1

    # 현재 값 반환
    def get_env(self):
        self.set_env()
        return self.env_values


# 미션 컴퓨터 클래스
class MissionComputer:

    def __init__(self):

        # 현재 환경값 저장
        self.env_values = {
            'mars_base_internal_temperature': 0,
            'mars_base_external_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,
            'mars_base_internal_oxygen': 0
        }

        # 센서 연결
        self.ds = DummySensor()

        # 평균 계산용 데이터 저장
        self.history = {
            'mars_base_internal_temperature': [],
            'mars_base_external_temperature': [],
            'mars_base_internal_humidity': [],
            'mars_base_external_illuminance': [],
            'mars_base_internal_co2': [],
            'mars_base_internal_oxygen': []
        }

    def get_sensor_data(self):

        count = 0  # 반복 횟수 (5초 × 60 = 5분)

        while True:

            # 🔥 1. 센서값 먼저 출력 (이게 핵심 수정!)
            sensor_data = self.ds.get_env()
            self.env_values = sensor_data
            print(self.env_values)

            # 🔥 2. 평균 계산용 데이터 저장
            for key in self.env_values:
                self.history[key].append(self.env_values[key])

            count += 1

            # 🔥 3. 5분마다 평균 출력
            if count == 60:
                print('----- 5분 평균 값 -----')
                for key in self.history:
                    values = self.history[key]
                    avg = sum(values) / len(values)
                    print(key, ':', avg)

                # 초기화
                self.history = {key: [] for key in self.history}
                count = 0

            # 🔥 4. 종료 입력
            user_input = input('종료하려면 q 입력 (계속하려면 Enter): ')
            if user_input == 'q':
                print('Sytem stoped....')
                break

            # 🔥 5. 5초 대기
            time.sleep(5)


# 실행
RunComputer = MissionComputer()
RunComputer.get_sensor_data()