# 10_api

### 목표

- RESTful API 서버 구축



### 환경

- Python Web Framework
  - Django v.2.1.5
  - Python v.3.6.7
  - C9.io



#### 1. 데이터베이스 설계

  - Genre

    | 필드명 | 자료형      | 설명        |
    | ------ | ----------- | ----------- |
    | id     | Integer     | Primary Key |
    | name   | String (20) | 장르 구분   |

  - Movie

    | 필드명      | 자료형       | 설명                        |
    | ----------- | ------------ | --------------------------- |
    | id          | Integer      | Primary Key                 |
    | title       | String (30)  | 영화명                      |
    | audience    | Integer      | 누적 관객수                 |
    | poster_url  | String (140) | 포스터 이미지 URL           |
    | description | Text         | 영화 소개                   |
    | genre_id    | Integer      | Genre의 Primary Key (id 값) |

  - Score

    | 필드명   | 자료형       | 설명                        |
    | -------- | ------------ | --------------------------- |
    | id       | Integer      | Primary Key                 |
    | content  | String (140) | 한줄평 (평가 내용)          |
    | value    | Integer      | 평점                        |
    | movie_id | Integer      | Movie의 Primary Key (id 값) |



#### 2. Seed Data 반영

- 주어진 movie.json과 genre.json 파일을 movies/fixtures/ 경로에 옮긴 후
- 다음 명령어를 통해 반영함

```bash
$ python manage.py loaddata genre.json
$ python manage.py loaddata movie.json
```



#### 3. `movies` API

- 10_api.PNG 이미지 파일 참조
- 없는 경로 변수로 접근시, 404 Not Found 에러를 보여줌
- 기본 경로로 접근시 django-rest-swagger를 통한 페이지를 보여줌

- 장르 목록 
  - URL : `GET /api/v1/genres/`
- 특정 장르와 그 장르에 속해있는 영화 목록 보여주는 페이지 
  - URL : `GET /api/v1/genres/{genre_id}/`
- 영화 목록을 보여주는 페이지 
  - URL : `GET /api/v1/movies/`
- 특정 영화의 정보만을 보여주는 페이지 
  - URL : `GET /api/v1/movies/{movie_id}/`
- 특정 영화에 평점을 등록하는 요청을 보내는 
  - URL : `POST /api/v1/movies/{movie_id}/scores/`
- 평점에 관한 URL 
  - GET 방식일때, 특정 평점의 정보를 보여주는 URL : `GET /api/v1/scores/{score_id}/`
  - PUT 방식일때, 평점을 등록하는 요청을 보내는 URL : `PUT /api/v1/scores/{score_id}/`
  - DELETE 방식일때, 특정 평점의 삭제를 요청을 보내는 URL : `DELETE /api/v1/scores/{score_id}/`

