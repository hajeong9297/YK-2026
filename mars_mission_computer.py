#문제에서 랜덤 값 생성하라고 함 → “랜덤 기능 가져오기”
# random: 이 모듈은 랜덤(무작위) 값을 만들 때 사용한다.
# 이번 과제에서는 더미 센서 값이 고정값이 아니라 실행할 때마다 조금씩 달라져야 하므로 사용했음.
import random

# DummySensor 클래스 정의
# → 실제 센서가 아니라, 테스트용 가짜 센서 역할
class DummySensor:

    # 객체가 생성될 때 자동으로 실행되는 초기화 함수
    def __init__(self):
            # __init__ 메소드는 객체가 생성될 때 자동으로 실행되는 메소드이다.
        self.env_values = {
            
        # def set_env(self):환경값을 설정하는 함수
        # env_values는 환경 값을 저장할 사전(dict) 객체이다.
        # key : 항목 이름, value : 값
        # 처음에는 아직 센서 값이 없으므로 0으로 초기화

            'mars_base_internal_temperature': 0,   # 화성 기지 내부 온도
            'mars_base_external_temperature': 0,   # 화성 기지 외부 온도
            'mars_base_internal_humidity': 0,      # 화성 기지 내부 습도
            'mars_base_external_illuminance': 0,   # 화성 기지 외부 광량
            'mars_base_internal_co2': 0,           # 화성 기지 내부 이산화탄소 농도
            'mars_base_internal_oxygen': 0         # 화성 기지 내부 산소 농도
        }

    # set_env 메소드는 환경 값을 랜덤으로 생성해서 env_values 사전에 저장하는 역할을 한다.
    # 실제 센서가 아직 없기 때문에 "센서가 측정한 것처럼 보이는 가짜 데이터"를 만들어 넣는 함수이다.
    #self.env_values['mars_base_internal_temperature'] = random.randint(18, 30) → 내부 온도 항목에 18~30 사이 숫자 하나 넣어라

    def set_env(self):
        # 화성 기지 내부 온도
        # 문제에서 범위는 18 ~ 30도이다.
        # randint(a, b)는 a 이상 b 이하의 정수를 랜덤으로 생성한다.
        self.env_values['mars_base_internal_temperature'] = random.randint(18, 30)

        # 화성 기지 외부 온도
        # 문제에서 범위는 0 ~ 21도이다.
        self.env_values['mars_base_external_temperature'] = random.randint(0, 21)

        # 화성 기지 내부 습도
        # 문제에서 범위는 50 ~ 60%이다.
        self.env_values['mars_base_internal_humidity'] = random.randint(50, 60)

        # 화성 기지 외부 광량
        # 문제에서 범위는 500 ~ 715 W/m2이다.
        self.env_values['mars_base_external_illuminance'] = random.randint(500, 715)

        # 화성 기지 내부 이산화탄소 농도
        # 문제에서 범위는 0.02 ~ 0.1%이다.
        # 이 값은 소수점이 필요하므로 uniform(a, b)를 사용한다.
        # uniform(a, b)는 a 이상 b 이하의 실수를 랜덤으로 생성한다.
        self.env_values['mars_base_internal_co2'] = random.uniform(0.02, 0.1)

        # 화성 기지 내부 산소 농도
        # 문제에서 범위는 4 ~ 7%이다.
        # 이 값도 소수점이 있을 수 있으므로 uniform을 사용한다.
        self.env_values['mars_base_internal_oxygen'] = random.uniform(4, 7)

    # get_env 메소드는 현재 저장되어 있는 env_values를 반환한다.
    # return은 함수 안의 값을 함수 밖으로 내보내는 역할을 한다.
    def get_env(self):
        # 현재 환경 값이 들어 있는 사전 전체를 그대로 반환한다.
        return self.env_values


# DummySensor 클래스를 이용해서 실제 객체(인스턴스)를 만든다.
# ds는 실제 만들어진 센서 객체.
ds = DummySensor()

# set_env 메소드를 호출한다.
# 그러면 env_values 안에 들어 있던 0들이
# 문제에서 요구한 범위의 랜덤 값으로 바뀌게 된다.
ds.set_env()

# get_env 메소드를 호출해서 현재 환경 값을 가져온다.
# 가져온 값은 env_data 변수에 저장한다.
env_data = ds.get_env()

# 최종적으로 환경 값을 출력한다.
# print를 사용하면 터미널(콘솔)에 값이 보인다.
print(env_data)


# =========================
# 실행 코드 (프로그램 시작)
# =========================

# DummySensor 객체 생성 (가짜 센서 생성)
ds = DummySensor()

# 랜덤 환경 값 생성 (센서가 측정한 것처럼 값 채움)
ds.set_env()

# 현재 환경 값 가져오기
env_data = ds.get_env()

# =========================
# 출력 (결과 확인)
# =========================

print('=== Mars Base Environment ===')

# 각 항목을 하나씩 출력
# → 사전에서 key를 이용해서 값 꺼냄
print('mars_base_internal_temperature :', env_data['mars_base_internal_temperature'])
print('mars_base_external_temperature :', env_data['mars_base_external_temperature'])
print('mars_base_internal_humidity :', env_data['mars_base_internal_humidity'])
print('mars_base_external_illuminance :', env_data['mars_base_external_illuminance'])
print('mars_base_internal_co2 :', env_data['mars_base_internal_co2'])
print('mars_base_internal_oxygen :', env_data['mars_base_internal_oxygen'])