# 🤖 recognition 

표에서 특정 행을 선택한 이미지를 보여주면 Tesseract OCR을 이용하여 해당 행의 맨 앞의 글자를 인식한 후 출력됩니다.

###사용예시

![example](https://user-images.githubusercontent.com/77109972/112179091-b7d4c380-8c3d-11eb-839d-43ffe973888c.gif)



***
참고사이트 : <https://github.com/kairess/license_plate_recognition/blob/master/main.ipynb>
위 사이트의 코드에서 tesseract 경로설정, 윤곽선 크기 조절, 변수 설정 등 수정
***

## 사용 방법과 원리
1. <https://github.com/UB-Mannheim/tesseract/wiki> tesseract를 설치합니다. 
2. module.py의 (226번째줄) pytesseract.pytesseract.tesseract_cmd=r'위에서 설치한 tesseract의 경로를 입력합니다'
3. 터미널에서 pip install tesseract 입력 후 오류가 없는지 확인합니다.
4. cam.py를 실행합니다.
5. 스페이스바를 눌러 빨간 사각형 안의 콘텐츠를 캡처합니다. (frame.jpg파일이 생성되는 것을 확인할 수 있습니다)
6. esc키를 2번 눌러 웹캠을 종료하면 결과가 출력됩니다.

***
웹캠의 화질과 사진 구도에 따라 성능이 달라집니다. 투표, 설문조사 등 다양한 분야에 활용해 보세요!

