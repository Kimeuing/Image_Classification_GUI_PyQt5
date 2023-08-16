# Image_Classification_GUI_PyQt5
이미지 분류 모델을 활용한 이미지 분류 자동화 프로그램

# 🖥프로젝트 소개
딥러닝 모델 중 하나인 Resnet을 이용하여 만든 이미지 분류 모델(정확도:99.76%)을 Pyqt5에 적용시켜 사용자 친화적인 GUI를 구성했습니다.

# 🔎프로그램 기능 소개
<img width="448" alt="스크린샷 2023-08-16 151239" src="https://github.com/Kimeuing/Image_Classification_GUI_PyQt5/assets/109636260/a595245a-dca9-4209-9170-978e85002ecd">

* 제품 선택
  * 두 가지 제품을 선택하여 그에 맞는 이미지 분류가 가능합니다.
  * <img width="96" alt="스크린샷 2023-08-16 152452" src="https://github.com/Kimeuing/Image_Classification_GUI_PyQt5/assets/109636260/42ea6b43-9859-4931-af82-61cf416ddc45">

* 폴더 저장
  * 검사가 끝난 결과 파일(csv)을 저장할 장소를 선택할 수 있습니다.
  * 기본값은 C드라이브 하위 폴더로 설정돼있습니다.
  * 경로 변경 시 왼쪽 하단에 저장되는 경로가 표기됩니다.
  * <img width="434" alt="스크린샷 2023-08-16 152629" src="https://github.com/Kimeuing/Image_Classification_GUI_PyQt5/assets/109636260/36501f78-f2ec-4a1c-8349-c8829c33b779">

* 이미지 폴더 선택
  * 분류를 진행할 이미지 폴더를 불러옵니다.
  * 선택을 마치면 오른쪽에 경로가 표기됩니다.
  * <img width="434" alt="스크린샷 2023-08-16 153101" src="https://github.com/Kimeuing/Image_Classification_GUI_PyQt5/assets/109636260/338a2bdf-e839-4a30-ad0d-854c3f2d29fa">
  
* 분류 시작
  * 버튼을 누르면 예상 소요 시간을 출력하고 분류를 시작합니다.
  * 검사를 마치면 무슨 오류인지, 개수 등을 출력합니다.
  * 이미지 열을 더블 클릭하면 NG 파일 개수 하단에 그 이미지를 크게 출력합니다.
  * <img width="434" alt="스크린샷 2023-08-16 153509" src="https://github.com/Kimeuing/Image_Classification_GUI_PyQt5/assets/109636260/7646e9e4-3989-45fb-a045-9c4170ec9e19">
* 검사 종료
  * 새로 검사를 하기 앞서 진행한 것들을 초기화 시킵니다. 
