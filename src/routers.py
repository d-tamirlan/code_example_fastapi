from fastapi import Request, Depends, Form, APIRouter
from starlette import status
from starlette.responses import RedirectResponse

from src.models import user_db, User, FileLinks
from src.conf.conf import templates, fastapi_users


router = APIRouter()


@router.get("/")
async def index(request: Request):
    """ Главная страница """

    return templates.TemplateResponse('index.html', {'request': request})


@router.get("/users/register")
async def register(request: Request):
    """ Страница регистарции """

    return templates.TemplateResponse('register.html', {'request': request})


@router.get("/users/login")
async def register(request: Request):
    """ Страница логина """

    return templates.TemplateResponse('login.html', {'request': request})


@router.post("/users/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user: User = Depends(fastapi_users.get_current_active_user)):
    """ Роут для удаления аккаунта """

    await user_db.delete(user)

    url = router.url_path_for("index")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@router.get("/users/links")
async def files_links(request: Request, user: User = Depends(fastapi_users.get_current_active_user)):
    """ Страница со списком ссылок текущего пользователя """

    file_links = await FileLinks.filter(user_id=user.id)

    return templates.TemplateResponse('links.html', {'request': request, 'user': user, 'file_links': file_links})


@router.post("/users/links/add")
async def files_links_add(
        link: str = Form('link'),
        user: User = Depends(fastapi_users.get_current_active_user)
):
    """ Роут для добавления ссылок """

    await FileLinks.create(user_id=user.id, link=link)

    url = router.url_path_for("files_links")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@router.post("/users/links/delete/{link_id}")
async def files_links_delete(
        link_id: int,
        user: User = Depends(fastapi_users.get_current_active_user)
):
    """ Роут для удаления ссылок """

    await FileLinks.filter(id=link_id, user_id=user.id).delete()

    url = router.url_path_for("files_links")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
