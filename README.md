# CreateMyDraft

The aim of this project is to help users generate drafts for essential clinical trial documents, specifically Lay Clinical Trial Documents (LayCTDs) and Informed Consent Forms (ICFs). Using ChatGPT-4 via LangChain, it generates drafts to different needs such as simple language, technical details, or in-depth explanations. The app also allows users to view and track previous drafts, simplifying document management and supporting clear communication in clinical trials.

## Roadmap

- Screenshot

- App Overview

- Prerequisites

- Getting Started

- Author

## Screenshot

![Screenshot](Screenshot.png)

## App Overview

### Features

- **Draft Generation**: Generate drafts for clinical trial documentation.
- **Previous Drafts**: Access and view past drafts.

### Draft Generation 
#### Document Types and Input Details

The app supports two main document types, each with specific fields:

**Lay Clinical Trial Document (LayCTD)**
   - **Trial Purpose**: Brief description of the clinical trial's main goal.
   - **Patient Demographics**: Key details about the participants, such as age range and medical condition.
   - **Expected Outcomes**: Summary of anticipated results or potential benefits from the trial.

**Informed Consent Form (ICF)**
   - **Participant Information**: Overview of participant eligibility criteria and trial context.
   - **Study Risks**: Information about any potential risks involved in the study.
   - **Study Benefits**: Description of possible benefits for participants.
   - **Study Duration**: Expected length of the study (e.g., 6 months).


## Prerequisites

- Python 3
- OpenAI
- LangChain
- Streamlit
- SQLite
- Docker

## Getting Started

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Initialization
```bash
cd config && python3 init_db.py
```

### Set Up API Key:
```bash
echo "your_api_key_here" > open_api_key.txt
```

### Start the Application
```bash
streamlit run main.py 
```

### Alternative: Docker Hub

Pull the Docker Image:
```bash
docker pull agnir/createmydraft
```

Start the Container:
```bash
docker run -d -p 8501:8501 agnir/createmydraft
```

Access the Container:
```bash
docker exec -it container_id /bin/bash
```

Set Up Your API Key:
```bash
echo "your_api_key_here" > open_api_key.txt

```
## Author

- [Agni Ramadani](https://github.com/agniramadani)
