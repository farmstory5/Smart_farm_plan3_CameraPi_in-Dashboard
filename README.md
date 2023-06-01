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
<p>
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/7657eb8a-e982-4374-927c-49e9fcd162f4">
</p>
아두이노 uno에 연결된 조도센서는 라즈베리파이에서는 값을 확인하지 못하게 되었습니다...<br/>
추후에 ADC컨버터 MCP3008을 사용하여 라즈베리파이 임베디드시스템에서 동작하도록 개선하겠습니다. <br/>

### 블록도
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan4_CDS_WaterLevel_Analog_signal_in-Dashboard/assets/130550405/624d6807-0975-41dd-b509-c55b96691fec">
</p>

### Node-red FLOW 흐름도
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/75ecb881-5f4d-4816-a327-afd1a332254f">
</p>
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/55c67a21-f192-4821-8f4d-518eb02c1138">
</p>

### dashboard
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/054453b0-7f45-44f0-be30-a252d549e84c">
</p>

### 사용한 재료들
라즈베리파이4 B .ver 임베디드시스템, DHT11 센서, LED 2개, Ras pi용 Camera<br/>
Arduino Uno, 조도센서

### GPIO 세팅 및 아두이노(임시)
Raspi 4<br/>
DHT11 - Vcc: 4_pin 5V / Data: 7_pin (GPIO_4) / Ground: 6_pin<br/>
LED_Yel - 11_pin (GPIO_17) / Ground: 9_pin<br/>
LED_Red - 12_pin (GPIO_18) / Ground: 14_pin<br/>
Camera - 카메라용 케이블 소켓<br/>
<br/>
Arduino Uno /dev/ttyACM0 (임시)<br/>
조도센서 - Vcc: Power 5V pin / Out: Analog 0 pin / Ground: Power GND pin
<br/>

### 사용한 SW요소들
Rasberry Pi OS Legacy, Nord-red 프레임워크 개발도구, dashboard 라이브러리<br/>
Arduino 보드- Uno 포트 - /dev/ttyACM0, StandardFirmata 라이브러리 (임시)
<br/>

### 구현 영상
<p align="center">
<img src="https://github.com/farmstory5/Smart_farm_plan2_Node-red_dashboard/assets/130550405/91432796-efce-4379-813d-2c7d676ca6e5">
</p>
https://www.youtube.com/watch?v=134TiywJLuI
