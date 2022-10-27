from fastapi import APIRouter, Depends, HTTPException, Form
from starlette import status
from fastapi import  Request
from src.api.v1.schemas.users import UserCreate, UserLogin, UserUpdate
from src.services.user import get_user_service, UserService
from fastapi_jwt_auth import AuthJWT
from starlette.templating import Jinja2Templates

from webapp.loginform import LoginForm

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.post(
    path="/signup",
    summary="Регистрация пользователя",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
)
def user_signup(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service),
) -> dict:
    res = user_service.create_user(user=user)
    return res

@router.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post(
    path="/login",
    summary="Вход пользователя в систему",
    tags=["users"],
)
def user_login(
    request: Request,
    user: UserLogin,
    user_service: UserService = Depends(get_user_service),
    Authorize: AuthJWT = Depends(),
):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful :)")
            response = templates.TemplateResponse("login.html",
                                                  form.__dict__)
            user_service.login(Authorize, user=response)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("login.html", form.__dict__)
    return templates.TemplateResponse("login.html", form.__dict__)



@router.post(
    path="/refresh",
    summary="Обновление токена",
    tags=["users"],
)
def refresh(
    user_service: UserService = Depends(get_user_service),
    Authorize: AuthJWT = Depends(),
):
    return user_service.refresh(Authorize)


@router.get(
    path="/users/me",
    summary="Просмотр сведений о пользователе",
    tags=["users"],
)
def user_about(
    user_service: UserService = Depends(get_user_service),
    Authorize: AuthJWT = Depends(),
):
    return user_service.user_detail(Authorize)


@router.patch(
    path="/users/me",
    # response_model=UserModel,
    summary="Изменение сведений о пользователе",
    tags=["users"],
)
def user_change(
    user: UserUpdate,
    user_service: UserService = Depends(get_user_service),
    Authorize: AuthJWT = Depends(),
):
    return user_service.user_change(Authorize, user=user)


@router.post(
    path="/logout",
    # response_model=PostListResponse,
    summary="Выход с одного устройства",
    tags=["users"],
)
def user_logout(
    user_service: UserService = Depends(get_user_service),
    Authorize: AuthJWT = Depends(),
):
    return user_service.logout(Authorize)


@router.post(
    path="/logout_all",
    # response_model=PostListResponse,
    summary="Выход со всех устройств",
    tags=["users"],
)
def user_logout_all(
    user_service: UserService = Depends(get_user_service),
    Authorize: AuthJWT = Depends(),
):
    return user_service.logout_all(Authorize)
