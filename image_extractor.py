import cv2

def save_frames_as_images(video_path, output_folder):
    # 동영상 파일 열기
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("동영상 파일을 열 수 없습니다.")
        return

    # 이미지 저장을 위한 폴더 생성
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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


video_name = '0416_10km'
folder_path = './dataset/'
# 동영상 파일 경로와 이미지를 저장할 폴더를 지정합니다.
video_path = folder_path + video_name + ".mp4"
output_folder = video_name

# 함수 호출
save_frames_as_images(video_path, output_folder)
