from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path
app = FastAPI(
    title="EduGenie",
    description="An AI-powered learning assistant",
    version="1.0.0",
)
from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path


app = FastAPI(
    title="EduGenie",
    description="An AI-powered learning assistant",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextRequest(BaseModel):
    text: str = Field(min_length=1, max_length=12000)


class QuizRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=500)
    number_of_questions: int = Field(default=5, ge=1, le=10)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@app.get("/health")
def health_check():
    return {"status": "EduGenie is running"}


@app.post("/qa")
def question_answer(request: TextRequest):
    try:
        result = answer_question(request.text)
        return {"answer": result}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.post("/explain")
def explain(request: TextRequest):
    try:
        result = explain_concept(request.text)
        return {"explanation": result}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.post("/quiz")
def quiz(request: QuizRequest):
    try:
        result = generate_quiz(
            topic=request.topic,
            number_of_questions=request.number_of_questions,
        )
        return {"quiz": result}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.post("/summarize")
def summarize(request: TextRequest):
    try:
        result = summarize_text(request.text)
        return {"summary": result}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.post("/learn/recommendations")
def learning_recommendations(request: TextRequest):
    try:
        result = recommend_learning_path(request.text)
        return {"recommendations": result}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))