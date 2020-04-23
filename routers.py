from fastapi import Request, Depends, Form, APIRouter
from starlette import status
from starlette.responses import RedirectResponse

from models import user_db, User
from conf.conf import templates, fastapi_users
import crud


router = APIRouter()


@router.get("/users/register")
async def register(request: Request):
    return templates.TemplateResponse('register.html', {'request': request})


@router.get("/users/login")
async def register(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})


@router.delete("/users/delete", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user: User = Depends(fastapi_users.get_current_active_user)):
    await user_db.delete(user)


@router.get("/users/links")
async def files_links(request: Request, user: User = Depends(fastapi_users.get_current_active_user)):
    file_links = crud.get_links(user)
    return templates.TemplateResponse('links.html', {'request': request, 'file_links': file_links})


@router.post("/users/links/add")
async def files_links_add(
        link: str = Form('link'),
        user: User = Depends(fastapi_users.get_current_active_user)
):
    crud.create_link(user, link)

    url = router.url_path_for("files_links")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)


@router.post("/users/links/delete/{link_id}")
async def files_links_delete(
        link_id: int,
        user: User = Depends(fastapi_users.get_current_active_user)
):
    crud.delete_link(user, link_id)

    url = router.url_path_for("files_links")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)
