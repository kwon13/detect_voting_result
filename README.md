# CatDogClassification :cat::dog:

표에서 특정 행을 선택한 이미지를 보여주면 Tesseract OCR을 이용하여 해당 행의 맨 앞의 글자를 인식한 후 출력됩니다.

***
사용예시![5](https://user-images.githubusercontent.com/77109972/112175229-6d057c80-8c3a-11eb-954f-ba23903fe2f0.jpg)

https://user-images.githubusercontent.com/77109972/112175071-45161900-8c3a-11eb-8c85-9187ed0ee258.mp4



***
참고사이트 : <https://github.com/kairess/license_plate_recognition/blob/master/main.ipynb>
위 사이트의 코드에서 tesseract 경로설정, 윤곽선 크기 조절, 변수 설정, 웹캠 인
***

## 사용 방법과 원리
1. <https://github.com/UB-Mannheim/tesseract/wiki> tesseract를 설치합니다. 
2. module.py의 (226번째줄) pytesseract.pytesseract.tesseract_cmd=r'위에서 설치한 tesseract의 경로를 입력합니다'
3. 터미널에서 pip install tesseract 입력 후 오류가 없는지 확인합니다.
4. 
kaggle Dogs vs. Cats Dataset
<https://www.kaggle.com/c/dogs-vs-cats/data>
