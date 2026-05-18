import os
from datetime import datetime

from scipy.io.wavfile import write

import sounddevice as sd


def create_records_folder():
    """records 폴더를 생성한다."""

    folder_name = 'records'

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    return folder_name


def make_record_file_name():
    """현재 날짜와 시간을 기준으로 파일 이름 생성"""

    now = datetime.now()

    file_name = now.strftime('%Y%m%d-%H%M%S') + '.wav'

    return file_name


def record_voice(record_seconds=5):
    """시스템 마이크를 사용하여 음성을 녹음한다."""

    rate = 44100

    records_folder = create_records_folder()

    file_name = make_record_file_name()

    file_path = os.path.join(records_folder, file_name)

    print('녹음을 시작합니다.')

    recording = sd.rec(
        int(record_seconds * rate),
        samplerate=rate,
        channels=1
    )

    sd.wait()

    write(file_path, rate, recording)

    print('녹음이 완료되었습니다.')
    print('저장된 파일 :', file_path)


def show_record_files_by_date(start_date, end_date):
    """특정 날짜 범위의 녹음 파일 목록 출력"""

    folder_name = 'records'

    if not os.path.exists(folder_name):
        print('records 폴더가 존재하지 않습니다.')
        return

    file_names = os.listdir(folder_name)

    print()
    print(start_date, '부터', end_date, '까지의 녹음 파일')

    for file_name in file_names:
        if not file_name.endswith('.wav'):
            continue

        record_date = file_name[:8]

        if start_date <= record_date <= end_date:
            print(file_name)


if __name__ == '__main__':
    record_voice(5)

    print()

    show_record_files_by_date(
        '20260501',
        '20260518'
    )