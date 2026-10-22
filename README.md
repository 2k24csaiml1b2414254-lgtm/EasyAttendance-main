# EasyAttendance — AI-Powered Attendance Management System

EasyAttendance is an attendance management application built with Python and Streamlit. It organizes teacher and student workflows and includes a modular architecture for attendance management, database operations, and face-recognition-related processing.

## Overview

The project aims to simplify attendance management through a digital interface for teachers and students.

The application uses Streamlit for its user interface and separates screens, reusable components, database functionality, and processing pipelines into dedicated modules.

## Features

- Teacher and student interfaces
- Separate home, student, and teacher screens
- Session-based navigation using Streamlit
- Join-code-based student enrollment flow
- Modular application structure
- Database-related functionality
- Face-recognition-related processing components
- Configuration and dependency management through Python files and `requirements.txt`

*Feature availability depends on the current implementation and configured database/services.*

## Tech Stack

- **Language:** Python
- **Frontend/UI:** Streamlit
- **Computer Vision:** Face-recognition-related libraries
- **Database:** See the database modules and application configuration
- **Application Architecture:** Modular Python packages

## Project Structure

```text
EasyAttendance-main/
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   ├── ui/
│   └── __init__.py
├── app.py
├── requirements.txt
├── .gitignore
├── bcrypt.jpg
├── dlib-bin.jpg
├── face_recog.jpg
└── supabase.jpg
```

## Application Architecture

The application entry point is `app.py`. It configures the Streamlit page and directs users to the appropriate screen according to the current session state.

```text
                    app.py
                      |
                      v
                Session State
                      |
           +----------+----------+
           |          |          |
           v          v          v
       Home Screen  Student    Teacher
                    Screen     Screen
           |
           v
      Components
           |
           v
   Database / Pipelines
```

This diagram illustrates the module organization; the exact runtime call flow depends on the implementation of each module.

## How It Works

1. The application starts through Streamlit.
2. The home screen provides the initial application flow.
3. Session state determines whether the teacher or student screen should be displayed.
4. The application includes a join-code flow for student enrollment.
5. Components, database modules, and pipelines support the application's functionality.

## Getting Started

### Prerequisites

- Python installed on your system
- Git
- Required native dependencies for any computer-vision libraries used by the project
- Valid database and service configuration, if required

### 1. Clone the Repository

```bash
git clone https://github.com/2k24csaiml1b2414254-lgtm/EasyAttendance-main.git
cd EasyAttendance-main
```

### 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Some computer-vision dependencies may require additional system setup depending on your operating system.

### 3. Configure the Application

Review the database and application configuration before running the project.

If the application uses API keys or database credentials, keep them in environment variables or an untracked `.env` file. Never commit secrets to GitHub.

### 4. Run the Application

```bash
streamlit run app.py
```

Streamlit will display the local application URL in the terminal, usually:

```text
http://localhost:8501
```

## Repository

GitHub: https://github.com/2k24csaiml1b2414254-lgtm/EasyAttendance-main

## Future Improvements

- Improve attendance reporting and analytics
- Strengthen authentication and role-based access control
- Improve database security and access policies
- Add robust error handling and audit logs
- Improve face-recognition reliability under different lighting conditions
- Add automated tests and deployment documentation
- Add attendance export and reporting features

## Learning Outcomes

- Developing interactive applications with Streamlit
- Organizing Python projects into reusable modules
- Managing teacher and student application flows
- Working with database integration
- Exploring computer-vision and face-recognition pipelines
- Handling session state and application navigation

## License

Add an appropriate license to specify how this project may be used and distributed.
