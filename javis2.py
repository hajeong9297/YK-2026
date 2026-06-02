import csv
import os
import speech_recognition as sr


def get_audio_file_list(folder_path):
    """
    지정한 폴더에서 wav 음성 파일 목록을 불러온다.
    """

    audio_files = []

    try:
        file_list = os.listdir(folder_path)

        for file_name in file_list:
            if file_name.endswith('.wav'):
                audio_files.append(file_name)

    except FileNotFoundError:
        print('녹음 파일 폴더를 찾을 수 없습니다.')

    except OSError:
        print('녹음 파일 목록을 불러오는 중 오류가 발생했습니다.')

    return audio_files


def convert_speech_to_text(audio_path):
    """
    음성 파일에서 텍스트를 추출한다.
    """

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)

        recognized_text = recognizer.recognize_google(
            audio_data,
            language='ko-KR'
        )

        return recognized_text

    except sr.UnknownValueError:
        print('음성을 인식할 수 없습니다.')

    except sr.RequestError:
        print('STT 서비스 연결에 실패했습니다.')

    except FileNotFoundError:
        print('음성 파일을 찾을 수 없습니다.')

    except OSError:
        print('음성 파일을 읽는 중 오류가 발생했습니다.')

    return ''


def create_csv_file_path(folder_path, audio_file_name):
    """
    음성 파일명과 같은 이름의 csv 파일 경로를 생성한다.
    """

    file_name_without_ext = os.path.splitext(audio_file_name)[0]
    csv_file_name = file_name_without_ext + '.csv'
    csv_file_path = os.path.join(folder_path, csv_file_name)

    return csv_file_path


def save_stt_result_to_csv(csv_file_path, recognized_text):
    """
    STT 결과를 csv 파일로 저장한다.
    """

    try:
        with open(
            csv_file_path,
            'w',
            newline='',
            encoding='utf-8-sig'
        ) as file:
            writer = csv.writer(file)

            writer.writerow(['음성 파일내에서의 시간', '인식된 텍스트'])
            writer.writerow(['0초', recognized_text])

        print('CSV 파일 저장 완료:', csv_file_path)

    except OSError:
        print('CSV 파일 저장 중 오류가 발생했습니다.')


def process_audio_files(folder_path):
    """
    음성 파일 목록을 불러오고 STT 처리 후 csv 파일로 저장한다.
    """

    audio_files = get_audio_file_list(folder_path)

    if len(audio_files) == 0:
        print('처리할 음성 파일이 없습니다.')
        return

    for audio_file_name in audio_files:
        audio_file_path = os.path.join(folder_path, audio_file_name)

        print('처리 중인 음성 파일:', audio_file_name)

        recognized_text = convert_speech_to_text(audio_file_path)

        if recognized_text == '':
            print('텍스트로 변환된 내용이 없어 CSV로 저장하지 않습니다.')
            continue

        print('인식된 텍스트:', recognized_text)

        csv_file_path = create_csv_file_path(
            folder_path,
            audio_file_name
        )

        save_stt_result_to_csv(csv_file_path, recognized_text)


def search_keyword_in_csv(folder_path, keyword):
    """
    저장된 csv 파일 안에서 특정 키워드를 검색한다.
    """

    try:
        file_list = os.listdir(folder_path)
        csv_files = []

        for file_name in file_list:
            if file_name.endswith('.csv'):
                csv_files.append(file_name)

        if len(csv_files) == 0:
            print('검색할 CSV 파일이 없습니다.')
            return

        found = False

        for csv_file_name in csv_files:
            csv_file_path = os.path.join(folder_path, csv_file_name)

            with open(
                csv_file_path,
                'r',
                encoding='utf-8-sig'
            ) as file:
                reader = csv.reader(file)

                next(reader, None)

                for row in reader:
                    if len(row) < 2:
                        continue

                    record_time = row[0]
                    recognized_text = row[1]

                    if keyword in recognized_text:
                        found = True

                        print('파일 이름:', csv_file_name)
                        print('시간:', record_time)
                        print('내용:', recognized_text)
                        print('-' * 30)

        if found is False:
            print('검색 결과가 없습니다.')

    except FileNotFoundError:
        print('CSV 파일 폴더를 찾을 수 없습니다.')

    except OSError:
        print('CSV 파일 검색 중 오류가 발생했습니다.')


def main():
    """
    프로그램의 전체 실행 흐름을 담당한다.
    """

    record_folder = 'records'

    print('음성 파일 STT 변환을 시작합니다.')
    process_audio_files(record_folder)

    keyword = input('검색할 키워드를 입력하세요: ')

    if keyword == '':
        print('검색어가 입력되지 않았습니다.')
        return

    search_keyword_in_csv(record_folder, keyword)


if __name__ == '__main__':
    main()