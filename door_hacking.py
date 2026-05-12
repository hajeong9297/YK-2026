import time
import zipfile
import zlib


def number_to_password(number, chars):
    """
    숫자를 6자리 암호 문자열로 변환하는 함수
    """

    password = ''

    for _ in range(6):
        password = chars[number % len(chars)] + password
        number = number // len(chars)

    return password


def save_password(password):
    """
    찾은 암호를 password.txt 파일에 저장하는 함수
    """

    try:
        password_file = open('password.txt', 'w')

        password_file.write(password)

        password_file.close()

        print('암호를 password.txt 파일에 저장했습니다.')

    except FileNotFoundError:
        print('파일을 찾을 수 없습니다.')

    except PermissionError:
        print('파일 저장 권한이 없습니다.')

    except OSError:
        print('파일 저장 중 오류가 발생했습니다.')


def unlock_zip():
    """
    emergency_storage_key.zip 파일의 암호를 찾는 함수

    암호 조건
    - 숫자 + 소문자
    - 6자리
    """

    zip_file_name = 'emergency_storage_key.zip'

    # 암호에 사용할 문자 목록
    chars = '0123456789abcdefghijklmnopqrstuvwxyz'

    # 전체 가능한 경우의 수 계산
    total_count = len(chars) ** 6

    # 현재 시도 횟수
    count = 0

    # 시작 시간 저장
    start_time = time.time()

    print('암호 해제를 시작합니다.')
    print('시작 시간:', time.ctime(start_time))
    print('전체 시도 가능 횟수:', total_count)

    try:
        zip_file = zipfile.ZipFile(zip_file_name)

    except FileNotFoundError:
        print('emergency_storage_key.zip 파일을 찾을 수 없습니다.')
        return None

    except zipfile.BadZipFile:
        print('올바른 zip 파일이 아닙니다.')
        return None

    try:
        # 가능한 모든 암호를 하나씩 시도
        for number in range(total_count):

            # 숫자를 암호 문자열로 변환
            password = number_to_password(number, chars)

            count = count + 1

            try:
                # 암호 설정
                zip_file.setpassword(password.encode('utf-8'))

                # 압축 테스트
                if zip_file.testzip() is None:

                    # 암호가 맞으면 압축 해제
                    zip_file.extractall(
                        pwd=password.encode('utf-8')
                    )

                    elapsed_time = time.time() - start_time

                    print('암호 해제 성공')
                    print('암호:', password)
                    print('반복 횟수:', count)
                    print('진행 시간: %.2f초' % elapsed_time)

                    # 암호 저장
                    save_password(password)

                    zip_file.close()

                    return password

            except (RuntimeError, zlib.error):
                # 암호가 틀린 경우 다음 암호 시도
                pass

            # 너무 자주 출력하면 속도가 느려지므로
            # 100000번마다 진행 상황 출력
            if count % 100000 == 0:

                elapsed_time = time.time() - start_time

                print('반복 횟수:', count)
                print('진행 시간: %.2f초' % elapsed_time)

        zip_file.close()

        print('암호를 찾지 못했습니다.')

        return None

    except OSError:
        print('zip 파일 처리 중 오류가 발생했습니다.')

        return None


unlock_zip()