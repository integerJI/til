[출처 및 참고 ](https://cultivo-hy.github.io/docker/image/usage/2019/03/14/Docker%EC%A0%95%EB%A6%AC/#dockerfile-%EA%B8%B0%EB%B3%B8-%EB%AA%85%EB%A0%B9%EC%96%B4)

```
컨테이너 목록 확인하기 (ps)
docker ps [OPTIONS]
```
```
컨테이너 중지하기 (stop)
docker stop [OPTIONS] CONTAINER [CONTAINER...]
```
```
컨테이너 제거하기 (rm)
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```
```
이미지 목록 확인하기 (images)
docker images [OPTIONS] [REPOSITORY[:TAG]]
```
```
이미지 다운로드하기 (pull)
docker pull [OPTIONS] NAME[:TAG|@DIGEST]
```
```
이미지 삭제하기 (rmi)
docker rmi [OPTIONS] IMAGE [IMAGE...]
```
```
컨테이너 로그 보기 (logs)
docker logs [OPTIONS] CONTAINER
```
```
컨테이너 명령어 실행하기 (exec)
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```