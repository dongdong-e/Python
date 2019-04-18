
# **파이썬으로 데이터 주무르기(작성중)**
<br></br>
## **1장. 서울시 구별 CCTV 현황 분석**
**1장에서는 서울시의 구별 CCTV 현황을 분석합니다. CCTV가 서울시 어느 지역에 많은지 파악한 후, 구별 인구대비 비율을 확인하는 것까지 진행합니다. 특히, 인구 현황 데이터를 정리하여 구별 인구 현황에 대해서도 분석합니다. 또한, Matplotlib으로 구별 CCTV 현황을 시각화합니다.**
<br></br>
* 링크: https://github.com/dongdong-e/Python/blob/master/Data_Analytics/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A3%BC%EB%AC%B4%EB%A5%B4%EA%B8%B0/1_%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EA%B5%AC%EB%B3%84%20CCTV%20%ED%98%84%ED%99%A9%20%EB%B6%84%EC%84%9D.md
* Matplotlib: https://matplotlib.org/index.html
<br></br>

## **2장. 서울시 범죄 현황 분석**
**2장에서는 강남3구의 '체감안전도'가 높다는 기사를 검증합니다. 방법은 서울시 구별 범죄 발생과 그 검거율을 지표로 사용합니다. 그리고 시각화까지 진행합니다.**
<br></br>
* 링크: https://github.com/dongdong-e/Python/blob/master/Data_Analytics/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A3%BC%EB%AC%B4%EB%A5%B4%EA%B8%B0/2_%EC%84%9C%EC%9A%B8%EC%8B%9C_%EB%B2%94%EC%A3%84%ED%98%84%ED%99%A9_%EB%B6%84%EC%84%9D.ipynb
<br></br>

## **3장. 시카고 샌드위치 맛집 분석**
**3장에서는 데이터를 인터넷에서 직접 얻는 과정을 다룹니다. 이는 전문 용어로 '웹 스크래핑(Web Scraping)'이라고 합니다. 1장, 2장과 달리 이번 장에서는 주어진 자료가 아니라 'Beautiful Soup' 모듈의 기초를 익히고, 시카고 샌드위치 맛집 리스트를 정리합니다.**
<br></br>
* 링크: https://github.com/dongdong-e/Python/blob/master/Data_Analytics/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A3%BC%EB%AC%B4%EB%A5%B4%EA%B8%B0/3_%EC%8B%9C%EC%B9%B4%EA%B3%A0_%EC%83%8C%EB%93%9C%EC%9C%84%EC%B9%98_%EB%A7%9B%EC%A7%91_%EB%B6%84%EC%84%9D.ipynb
* Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
<br></br>

## **4장. 셀프 주유소는 정말 저렴할까**
**3장에서 사용한 'Beautiful Soup'으로 웹에 있는 많은 정보를 불러올 수 있습니다. 그러나, 분명히 Beautiful Soup으로 접근할수 없는 인터넷 정보도 많이 존재합니다. 특히, 웹 페이지에서 페이지 이동을 할 때마다 주소가 바뀌지 않는 경우에는 'Beautiful Soup'으로 데이터를 수집하는데 한계가 있습니다. 따라서 이번에는 'Selenium' 모듈을 사용합니다. 'Selenium'을 이용하면 'Beautiful Soup'의 부족한 부분을 보완하여 데이터를 수집할 수 있습니다.**
<br></br>
* 링크: https://github.com/dongdong-e/Python/blob/master/Data_Analytics/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A3%BC%EB%AC%B4%EB%A5%B4%EA%B8%B0/4_%EC%85%80%ED%94%84%20%EC%A3%BC%EC%9C%A0%EC%86%8C%EB%8A%94%20%EC%A0%95%EB%A7%90%20%EC%A0%80%EB%A0%B4%ED%95%A0%EA%B9%8C.ipynb
* Selenium: https://selenium-python.readthedocs.io/
<br></br>

## **5장. 우리나라 인구 소멸 위기 지역 분석**
**5장에서는 우리나라의 인구 소멸 위기 지역에 대해 조사합니다. 인구 소멸 위기 지역을 시각화하는 것이 목적입니다. 이전에 했던 서울시 지도가 아니라 대한민국 지도가 필요합니다. 따라서 이번에는 대한민국 지도를 그리고 그 위에 인구 소멸 위기 지역을 시각화하는 것을 목표로 합니다.**
**인구 소멸 지역: 65세 이상 노인 인구와 20~39세 여성 인구를 비교해서 젊은 여성 인구가 노인 인구의 절반에 미달할 경우 인구 소멸 위험 지역으로 분류합니다.**
<br></br>
* 링크: https://github.com/dongdong-e/Python/blob/master/Data_Analytics/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A3%BC%EB%AC%B4%EB%A5%B4%EA%B8%B0/5_%EC%9A%B0%EB%A6%AC%EB%82%98%EB%9D%BC%20%EC%9D%B8%EA%B5%AC%20%EC%86%8C%EB%A9%B8%20%EC%9C%84%EA%B8%B0%20%EC%A7%80%EC%97%AD%20%EB%B6%84%EC%84%9D.ipynb
