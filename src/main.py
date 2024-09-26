from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

chapters = [
    ["01장 파이썬이란 무엇인가?", "01-1 파이썬이란?", "01-2 파이썬의 특징", "01-3 파이썬으로 무엇을 할 수 있을까?", "01-4 파이썬 설치하기", "01-5 파이썬 둘러보기",
     "01-6 파이썬과 에디터"],
    ["02장 파이썬 프로그래밍의 기초, 자료형", "02-1 숫자형", "02-2 문자열 자료형", "02-3 리스트 자료형", "02-4 튜플 자료형"],
    ["1", "2", "3", "90asd0fa09sd7f0as7df0ad7fs0"]
]


# @app.exception_handler(Exception)
# async def general_exception_handler(request: Request, exc: Exception):
#     return RedirectResponse(url="/")
#
#
# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
#     RedirectResponse(url="/")
#
#
# @app.middleware("http")
# async def add_exception_handling_middleware(request: Request, call_next):
#     if not call_next:
#         return RedirectResponse(url="/")
#     try:
#         response = await call_next(request)
#     except:
#         return RedirectResponse(url="/")
#     if response.status_code == 404:
#         return RedirectResponse(url="/")
#     return response


@app.get("/", response_class=HTMLResponse)
async def render_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "chapters": chapters})


@app.get("/page/{id}")
async def render_page(request: Request, id: int):
    with open(f"pages/{id}.md", "r") as fp:
        page_data = fp.read()
    return templates.TemplateResponse(f"page.html", {"request": request, "chapters": chapters, "content": page_data})
