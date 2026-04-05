# stud-reg-flask-app

#  Flask-Based Student Registration Web Application

##  Project Overview
This project is a Flask-based web application that allows users to register student details through a web form. The application stores the data in a MySQL database and provides a feature to view all registered students.

The project also demonstrates CI/CD using Jenkins for automated deployment.

##  Features
- Student Registration Form.

- Data stored in MySQL database.

- View all registered students.

- Jenkins CI/CD integration.

- Deployed on AWS EC2 (optional).

##  Technology Stack

- Frontend: HTML, CSS  

- Backend: Python (Flask) 

- Database: MySQL  

- Version Control: Git & GitHub 

- CI/CD Tool: Jenkins  

- Deployment: AWS EC2  

##  Setup Instructions

###  1. Clone Repository

    git clone https://github.com/Sharayu1707/stud-reg-flask-app.git
    cd stud-reg-flask-app

 2. Create Virtual Environment

        python3 -m venv venv
        source venv/bin/activate  

🔹 3. Install Dependencies

      pip install -r requirements.txt

🔹 4. Setup MySQL Database

Login to MySQL:

    sudo mysql -u root -p

    Create database and table:

    CREATE DATABASE student_db;

    USE student_db;

    CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    course VARCHAR(50),
    address TEXT
    );

🔹 5. Run Application

    python3 app.py

Open browser:

    http://localhost:5000

### Jenkins CI/CD Setup

    Install Jenkins
    Create Pipeline Job
    Connect GitHub repository
    Add jenkinsfile
    Run Build

![Architecture](images/Screenshot%20(294).png)


🖼️ 1. Registration Form

![Architecture](images/Screenshot%20(296).png)

🖼️ 2. Success Page

![Architecture](images/Screenshot%20(297).png)


🖼️ 3. Jenkins Build Success

![Architecture](images/Screenshot%20(295).png)


## Deployment

The application can be deployed on AWS EC2 and accessed via:

    http://15.168.239.96:5000

## Conclusion

Web development using Flask.

Database integration with MySQL.

CI/CD pipeline using Jenkins.

Deployment on cloud environment
