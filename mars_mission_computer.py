# 운영체제 및 시스템 정보를 가져오기 위한 모듈
import platform

# CPU 코어 수를 가져오기 위한 모듈
import os

# 데이터를 JSON 형식으로 출력하기 위한 모듈
import json

# 메모리, CPU 사용량 등 시스템 정보를 가져오기 위한 모듈
import psutil


# MissionComputer 클래스 정의 (미션 컴퓨터를 표현하는 클래스)
class MissionComputer:

    # 시스템 기본 정보를 가져오는 메소드
    def get_mission_computer_info(self):
        # 시스템 정보를 가져오는 과정에서 오류가 발생할 수 있으므로 예외 처리
        try:
            # 시스템 정보를 딕셔너리 형태로 저장
            computer_info = {
                # 현재 운영체제 이름 (예: Windows, Linux 등)
                'operating_system': platform.system(),

                # 운영체제 버전 정보
                'operating_system_version': platform.version(),

                # CPU 타입 정보
                'cpu_type': platform.processor(),

                # CPU 코어 개수 (예: 4, 8, 16 등)
                'cpu_core_count': os.cpu_count(),

                # 전체 메모리 크기를 GB 단위로 변환하고 소수점 2자리까지 표시
                'memory_size_gb': round(
                    psutil.virtual_memory().total / (1024 ** 3), 2
                )
            }

            # 위에서 만든 딕셔너리를 JSON 형식으로 변환하여 출력
            print(json.dumps(computer_info, indent = 4))

        # 오류 발생 시 실행되는 부분
        except Exception as e:
            print('시스템 정보를 가져오는 중 오류가 발생했습니다.')
            print(e)


    # 시스템 부하(CPU, 메모리 사용량)를 가져오는 메소드
    def get_mission_computer_load(self):
        # 시스템 부하 정보도 오류 가능성이 있으므로 예외 처리
        try:
            # CPU 및 메모리 사용량을 딕셔너리 형태로 저장
            computer_load = {
                # CPU 실시간 사용량 (%) - 1초 동안 측정된 평균값
                'cpu_usage_percent': psutil.cpu_percent(interval = 1),

                # 메모리 사용량 (%)
                'memory_usage_percent': psutil.virtual_memory().percent
            }

            # JSON 형식으로 변환하여 출력
            print(json.dumps(computer_load, indent = 4))

        # 오류 발생 시 실행
        except Exception as e:
            print('시스템 부하 정보를 가져오는 중 오류가 발생했습니다.')
            print(e)


# ---------------- 실행 부분 ----------------

# MissionComputer 클래스를 이용하여 객체 생성
runComputer = MissionComputer()

# 시스템 기본 정보 출력
runComputer.get_mission_computer_info()

# 시스템 부하 정보 출력
runComputer.get_mission_computer_load()