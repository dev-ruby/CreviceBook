from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.gzip import GZipMiddleware

app = FastAPI()
app.add_middleware(GZipMiddleware)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

chapters = [
    [
        "들어가기에 앞서",
        "0-1 서론, C 컴파일러 설치하기",
        "0-2 자연어의 모호성",
        "0-3 명령집합과 기계어"
    ],
    [
        "C언어 시작하기",
        "1-1 Hello, C!",
        "1-2 변수와 산술",
        "1-3 입출력",
        "1-4 조건문",
        "1-5 반복문",
        "1-6 블럭",
        "1-7 함수"
    ],
    [
        "한 걸음 더",
        "2-1 비트 연산자",
        "2-2 포인터",
        "2-3 형변환",
        "2-4 배열",
        "2-5 동적 할당",
        "2-6 복합 연산자",
        "2-7 증감 연산자",
        "2-8 문자열과 문자열 리터럴",
        "2-9 전처리문",
        "2-10 소스와 헤더",
    ],
    [
        "연습해보기",
        "3-1 직각삼각형",
        "3-1-2 직각삼각형 정답 코드",
        "3-2 소수 생성",
        "3-2-1 소수 생성 정답 코드",
    ]
]


@app.get("/", response_class=HTMLResponse)
async def render_main(request: Request):
    return await render_page(request, 0)


@app.get("/page/{id}")
async def render_page(request: Request, id: int):
    assert type(id) == int

    with open(f"pages/{id}.md", "r", encoding='utf-8') as fp:
        page_data = fp.read()
    return templates.TemplateResponse(
        f"page.html", {"request": request, "chapters": chapters, "content": page_data, "current_page": id}
    )
