# 로그 파일 읽어서 출력하는 코드

try:
    with open("mission_computer_main.log", "r", encoding="utf-8") as file:
        
        # 파일 한 줄씩 읽기
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

except Exception as e:
    print("오류 발생:", e)