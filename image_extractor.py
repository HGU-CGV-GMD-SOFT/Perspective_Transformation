import cv2
import os
import argparse



class Extractor:

    def __init__(self, input_video_path):
        self._input_video_name = input_video_path.split('/')[-1]
        self._folder_path = input_video_path.split('/')[-2]
        self._output_folder_path = self._input_video_name.split('.')[0]

        print(self._input_video_name)
        print(self._folder_path)
        print(self._output_folder_path)


    def save_frames_as_images(self,):
        # 동영상 파일 열기
        cap = cv2.VideoCapture(self._video_path)
        if not cap.isOpened():
            print("동영상 파일을 열 수 없습니다.")
            return

        # 이미지 저장을 위한 폴더 생성
        
        if not os.path.exists(self.output_folder):
            os.makedirs(self._output_folder)

        # 이미지 저장
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # 이미지 파일명 생성 (프레임 번호를 시간으로 변환하여 사용)
            time_in_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
            time_in_sec = time_in_ms / 1000
            # image_name = f"{output_folder}/frame_{time_in_sec}.jpg"
            image_name = "%s/frame_%.2f.jpg" % (output_folder, time_in_sec)

            # 이미지 저장
            cv2.imwrite(image_name, frame)
            frame_count += 1
        
        # 작업 완료 후 해제
        cap.release()
        print(f"{frame_count}개의 이미지를 저장했습니다.")



extractor = Extractor('./dataset/0416_10km.mp4')

# 함수 호출
# extractor.save_frames_as_images()
