# 5조 팜스토리 스마트팜 Node-red
# Smart_farm_plan3_CameraPi_in-Dashboard
## 구성원: 오상우, 윤현호, 박세린, 이병현, 권용만

### 개요
<p>
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/610cb3b4-8e1d-4591-8b4d-9f1889a98376">
</p>
Node-red 대시보드 ui에 화면 캡처기능을 추가하였습니다.
<br/><br/>
<p>
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/4a7953f9-9a6f-44f1-96bf-2a42aca8bb24">
</p>
Node-red 대시보드 ui에 조도센서측정기능을 추가하였습니다.(오류)<br/>
라즈베리파이와 아두이노 연동시 아두이노 UNO의 포트인 /dev/ttyACM0 이 라즈비안OS 리눅스환경에서 권한이 거부되었습니다.<br/>
추후에 다시 확인하고 고치도록 하겠습니다.<br/>

### 블록도
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/41e9c8b8-eeb3-45cc-9340-8c62cedcd87c">
</p>

### Node-red FLOW 흐름도
<p align="center">
<img src="https://user-images.githubusercontent.com/61779129/235959572-30756b3b-6056-413c-b176-6aad7734f763.png">
</p>
<p align="center">
<img src="https://user-images.githubusercontent.com/61779129/235959690-a8030e35-1838-498f-bc4b-d45c5ab8cb8b.png">
</p>

### dashboard
<p align="center">
<img src="https://user-images.githubusercontent.com/61779129/235959820-9291b854-b35f-4ffe-a581-942bbe68a50d.png">
</p>

### 사용한 재료들
라즈베리파이4 B .ver 임베디드시스템, DHT11 센서, LED 2개

### GPIO 세팅
DHT11 - Vcc: 4_pin 5V / Data: 7_pin (GPIO_4) / Ground: 6_pin<br/>
LED_Yel - 11_pin (GPIO_17) / Ground: 9_pin<br/>
LED_Red - 12_pin (GPIO_18) / Ground: 14_pin
<br/>

### 사용한 SW요소들
Rasberry Pi OS Legacy, Nord-red 프레임워크 개발도구, dashboard 라이브러리
<br/>

### 구현 영상
<p align="center">
<img src="https://user-images.githubusercontent.com/130550405/235965250-1beb52b4-8975-4a53-9055-efadaace2668.jpg">
</p>
https://youtu.be/clq28k0lrsg
