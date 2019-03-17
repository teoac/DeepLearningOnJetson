* [Udacity dataset 다운로드](https://github.com/udacity/self-driving-car/blob/master/datasets/CH2/Ch2_001.tar.gz.torrent)
  * dataset을 다운로드 할 수 있는 torrent 파일이 공유되어 있다.
  * 이 파일을 실행시키면 우분투의 Transmission BitTorrent Client를 통해 원본파일을 다운로드할 수 있다.


* [Collision dataset 다운로드](http://rpg.ifi.uzh.ch/data/collision.zip)

* 두 파일을 적절하게 압출을 풀어둔다.
  * 예) Udacity dataset: `~/data/data_Udacity/driving`
  * 예) Collision dataset: `~/data/data_Udacity/collision`


* Udacity dataset 압축을 푼 곳에 `/center` 디렉토리가 있는지 확인한다.
* 해당 디렉토리에서 아래 명령어를 실행하여 디렉토리를 생성한다.
  ```
  mkdir m04 m03 m02 m01 000 p01 p02 p03 p04
  ```
* [convt_udacity_steering.py](https://github.com/teoac/DeepLearningOnJetson/blob/master/utils/convt_udacity_steering.py)를 다운로드 받고 터미널창에서 아래와 같이 실행한다.
  ```
  python3 convt_udacity_steering.py
  ```

* [MNIST DB 구축](https://github.com/teoac/DeepLearningOnJetson/wiki/DIGITS_MNIST_LeNet_DB)을 참고하여 DIGITS에서 Udacity dataset DB를 구축한다.
![](https://github.com/teoac/DeepLearningOnJetson/blob/master/wiki_images/DIGITS_UDACITY_DB01.png)
