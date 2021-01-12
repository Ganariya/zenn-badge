import pybadges

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .zenn import scrape_user
from .user import User
from .logo import LOGO

app = FastAPI()
BASE_COLOR: str = '#3FA8FF'


def make_badge(left_text: str, right_text: str) -> str:
    return pybadges.badge(left_text=left_text, right_text=right_text, right_color=BASE_COLOR, embed_logo=True, logo=LOGO)


@app.get("/")
def main() -> str:
    return "Zenn Budges"


@app.get("/{username}/liked", response_class=HTMLResponse)
def get_liked(username: str) -> str:
    user: User = scrape_user(username)
    badge = make_badge('Zenn liked', str(user.total_liked_count))
    return badge


@app.get("/{username}/articles", response_class=HTMLResponse)
def get_liked(username: str) -> str:
    user: User = scrape_user(username)
    badge = make_badge('Zenn articles', str(user.articles_count))
    return badge


@app.get("/{username}/followers", response_class=HTMLResponse)
def get_liked(username: str) -> str:
    user: User = scrape_user(username)
    badge = make_badge('Zenn followers', str(user.follower_count))
    return badge
