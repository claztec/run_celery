# Celery 테스트
셀러리 샘플을 직접 돌려보는 프로젝트

https://tests4geeks.com/blog/python-celery-rabbitmq-tutorial/


## celery 실행
```shell script
(venv) (base) derek@Dereks-MacBook-Pro run_celery % celery -A test_celery.main worker -l info
 
 -------------- celery@Dereks-MacBook-Pro.local v4.4.2 (cliffs)
--- ***** ----- 
-- ******* ---- Darwin-19.4.0-x86_64-i386-64bit 2020-05-27 16:09:01
- *** --- * --- 
- ** ---------- [config]
- ** ---------- .> app:         test_celery:0x107acff10
- ** ---------- .> transport:   amqp://id:password@host:5672/vhost
- ** ---------- .> results:     rpc://
- *** --- * --- .> concurrency: 12 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** ----- 
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . test_celery.tasks.longtime_add

[2020-05-27 16:09:02,275: INFO/MainProcess] Connected to amqp://id:password@host:5672/vhost
[2020-05-27 16:09:02,666: INFO/MainProcess] mingle: searching for neighbors
[2020-05-27 16:09:04,202: INFO/MainProcess] mingle: all alone
[2020-05-27 16:09:04,440: INFO/MainProcess] celery@Dereks-MacBook-Pro.local ready.

```


## Task 실행
```shell script
(venv) (base) derek@Dereks-MacBook-Pro run_celery % python -m test_celery.run                             
Task finished?  False
Task result:  None
Task finished?  True
Task result:  3
(venv) (base) derek@Dereks-MacBook-Pro run_celery % 
```

## 결과 
```shell script
[2020-05-27 16:09:02,275: INFO/MainProcess] Connected to amqp://id:password@host:5672/vhost
[2020-05-27 16:09:02,666: INFO/MainProcess] mingle: searching for neighbors
[2020-05-27 16:09:04,202: INFO/MainProcess] mingle: all alone
[2020-05-27 16:09:04,440: INFO/MainProcess] celery@Dereks-MacBook-Pro.local ready.
[2020-05-27 16:11:46,360: INFO/MainProcess] Received task: test_celery.tasks.longtime_add[35f8dd6c-05bb-4949-b931-68c25fcfd8a2]  
[2020-05-27 16:11:46,363: WARNING/ForkPoolWorker-8] long time task begins
[2020-05-27 16:11:51,365: WARNING/ForkPoolWorker-8] long time task finished
[2020-05-27 16:11:51,440: INFO/ForkPoolWorker-8] Task test_celery.tasks.longtime_add[35f8dd6c-05bb-4949-b931-68c25fcfd8a2] succeeded in 5.077002180000022s: 3


```