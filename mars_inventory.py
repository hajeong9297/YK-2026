# Mars_Base_Inventory_List.csv 파일을 읽어서
# 인화성 기준으로 정렬하고, 0.7 이상 데이터를 CSV로 저장하는 프로그램

inventory_list = []

try:
    # 파일 열기 (읽기 모드)
    file = open('Mars_Base_Inventory_List.csv', 'r', encoding = 'utf-8')

    # 파일 한 줄씩 읽기
    for line in file:
        line = line.strip()  # 줄바꿈 제거

        # 빈 줄은 건너뛰기
        if line == '':
            continue

        # CSV 데이터를 콤마 기준으로 나누어 리스트로 변환
        data = line.split(',')

        # 전체 리스트에 추가
        inventory_list.append(data)

    # 파일 닫기
    file.close()

    # 첫 번째 줄(헤더) 분리
    header = inventory_list[0]

    # 실제 데이터만 따로 저장
    data_list = inventory_list[1:]

    # 인화성(Flammability, 5번째 컬럼)을 기준으로 내림차순 정렬
    # float()을 사용하여 문자열을 숫자로 변환 후 비교
    # float(x[4]): 문자열 → 숫자로 변환
    # lambda x: 정렬 기준을 정하는 함수
    data_list.sort(key = lambda x: float(x[4]), reverse = True)

    # 인화성 지수가 0.7 이상인 데이터만 저장할 리스트 생성
    danger_list = []

    # 조건에 맞는 데이터 필터링
    for item in data_list:
        if float(item[4]) >= 0.7:
            danger_list.append(item)

    # 결과를 CSV 파일로 저장
    try:
        out_file = open('Mars_Base_Inventory_danger.csv', 'w', encoding = 'utf-8')

        # 헤더 먼저 저장
        out_file.write(','.join(header) + '\n')

        # 필터링된 데이터 저장
        for item in danger_list:
            # 리스트를 CSV 형식 문자열로 변환 후 저장
            out_file.write(','.join(item) + '\n')

        # 파일 닫기
        out_file.close()

        print('저장 완료: Mars_Base_Inventory_danger.csv')

    except Exception as e:
        print('파일 저장 중 오류 발생:', e)

except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')

except Exception as e:
    print('오류 발생:', e)
