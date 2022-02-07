로드 밸런싱(load balancing)

로드 밸런싱은 컴퓨터 기술의 일종으로 중앙처리장치 같은 컴퓨터 자원들에게 작업을 나누는 것을 의미한다.

로드 밸런서의 종류
 - 운영체제 로드밸런서
 - 네트워크 로드밸런서

네트워크 로드 밸런서의 종류
 - L2(Data Link Layer)
   Mac Address Load Balancing
   장점으로는 구조가 간단, 신뢰성이 높다.
   단점으로는 Broadcast 패킷에 의해 성능 저하가 발생될 수 있으며 라우팅 등 상위 레이어 프로토콜 기반 스위칭이 불가능하다

 - L3(Net Work Layer)
   IP Address Load Balancing
   장점 : Broadcast 트래픽으로 전체 성능 저하 방지 및 트레픽 체크 가능
   단점 : 특정 프로콜을 이용해야 스위칭이 가능 하다

 - L4(Transport Layer) **
   Transport Layer(IP+Port) Load Balancing
   장점 : Port 기반 스위칭을 지원하며 VIP를 이용하여 여러대를 한대로 묶어 부하 분산, [Round Robin ](https://github.com/integerJI/Today_I_Learned/blob/main/DevOps/round_robin.md) 방식 사용

 - L7(Application Layer)
   Application Layer(사용자 Request) Load Balancing

현재 회사에서는 L4를 사용하고 있으며 대표적인 L4 로드 밸런싱이다.



참고 사이트 : https://pakss328.medium.com/%EB%A1%9C%EB%93%9C%EB%B0%B8%EB%9F%B0%EC%84%9C%EB%9E%80-l4-l7-501fd904cf05