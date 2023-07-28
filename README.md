# ML-Implemented-Mailing-Service
The application is basically a mailing service web-app. The user registers his/her interest through a web-app and the application queries this to the IEEE api after retrieving the information it then uses a ML(machine learning) model to classifiy whether the research paper belongs to any of the user registered preferences, if so, the paper is send to the user.
## Tech stacks to be used
- Django
- Celery
- React
- Redux
- Sqlite3
- JWT
- Docker
- Google, Facebook OAuth
- Google Cloud Platform (GCP)

## Screenshots

![Screenshot 2023-07-28 233840](https://github.com/kiranbaby14/ML-Implemented-Mailing-Service/assets/50899339/5ea42cb7-3762-4094-9224-c770e188a3a0)
![Screenshot 2023-07-28 233919](https://github.com/kiranbaby14/ML-Implemented-Mailing-Service/assets/50899339/14b8b7ce-a3f8-4c6c-a920-a042fa8d91f7)
![image](https://github.com/kiranbaby14/ML-Implemented-Mailing-Service/assets/50899339/0a581c02-1265-4509-a0bc-5175509665ed)

## RUN 
### Run the Django Server using docker
- cd into backend folder
  ```
  docker compose up
  ```

### Run the React frontend application
- cd into frontend folder
- install the dependencies
  ```
  npm install
  ```
- Start the application
  ```
  npm start
  ```
