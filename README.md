# College Essay Agent

An AI-powered application that helps students generate compelling college admission essays using LLMs.

## Features

- Generate structured college essays
- Uses Groq LLM for fast and high-quality output
- Backend built with FastAPI
- Frontend built with Streamlit
- Export essays as `.docx` files

---

## Tech Stack

- FastAPI (Backend API)
- Streamlit (Frontend UI)
- Groq (LLM)
- Python-docx (File export)

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/TejasVijaya74/essay-agent.git
cd essay-agent
````

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run the App

### Start Backend

```bash
uvicorn backend.main:app --reload
```

### Start Frontend

```bash
streamlit run app/app.py
```

---

## API Endpoint

* `POST /api/generate-essay`

---

## Output

* Generates essay text
* Downloadable `.docx` file

---

## Future Improvements

* Multi-step essay refinement
* University-specific prompts
* Essay scoring system
