# password.txt 파일 읽기
try:
    # password.txt 파일 열기
    with open('password.txt', 'r') as file:

        # 파일 내용 읽기
        password_text = file.read()

except FileNotFoundError:
    print('password.txt 파일을 찾을 수 없습니다.')
    exit()

except Exception as error:
    print('파일 읽기 중 오류가 발생했습니다.')
    print(error)
    exit()


# 카이사르 암호 해독 함수
def caesar_cipher_decode(target_text):

    # 해독 결과 저장 리스트
    decoded_results = []

    # 보너스 과제용 텍스트 사전
    word_dictionary = [
        'the',
        'password',
        'mars',
        'door',
        'emergency',
        'storage'
    ]

    # 알파벳 개수(26)만큼 반복
    for shift in range(26):

        # 현재 자리수 해독 결과 저장 변수
        decoded_text = ''

        # 문자열 한 글자씩 반복
        for character in target_text:

            # 현재 문자가 알파벳인지 확인
            if character.isalpha():

                # 소문자인 경우
                if character.islower():

                    # 알파벳 위치 계산
                    alphabet_index = ord(character) - ord('a')

                    # 자리수만큼 반대로 이동
                    decoded_index = (
                        alphabet_index - shift
                    ) % 26

                    # 숫자를 문자로 변환
                    decoded_character = chr(
                        decoded_index + ord('a')
                    )

                # 대문자인 경우
                else:

                    # 알파벳 위치 계산
                    alphabet_index = ord(character) - ord('A')

                    # 자리수만큼 반대로 이동
                    decoded_index = (
                        alphabet_index - shift
                    ) % 26

                    # 숫자를 문자로 변환
                    decoded_character = chr(
                        decoded_index + ord('A')
                    )

                # 해독 결과 저장
                decoded_text += decoded_character

            else:
                # 알파벳이 아니면 그대로 저장
                decoded_text += character

        # 현재 결과 저장
        decoded_results.append(decoded_text)

        # 현재 자리수 출력
        print('자리수 :', shift)

        # 해독 결과 출력
        print('해독 결과 :', decoded_text)

        # 결과 구분용 공백
        print()

        # 소문자로 변환 후 비교
        lower_decoded_text = decoded_text.lower()

        # 사전 단어 검사
        for word in word_dictionary:

            # 사전 단어가 포함되어 있는지 확인
            if word in lower_decoded_text:

                print('사전 단어 발견 :', word)
                print('자동으로 반복을 중단합니다.')

                # result.txt 저장
                try:
                    with open('result.txt', 'w') as file:
                        file.write(decoded_text)

                    print('result.txt 저장 완료')

                except Exception as error:
                    print('result.txt 저장 중 오류 발생')
                    print(error)

                return

    # 사용자가 직접 자리수 입력
    selected_shift = int(
        input('정답이라고 생각하는 자리수를 입력하세요 : ')
    )

    # 선택한 결과 가져오기
    final_result = decoded_results[selected_shift]

    # result.txt 저장
    try:
        with open('result.txt', 'w') as file:
            file.write(final_result)

        print('result.txt 저장 완료')

    except Exception as error:
        print('result.txt 저장 중 오류 발생')
        print(error)


# 함수 실행
caesar_cipher_decode(password_text)