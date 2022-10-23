import enum
from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from starlette import status

from src.api.v1.schemas.materials import MaterialListResponse, MaterialModel, \
    MaterialCreate
from src.services.material import MaterialService, get_material_service
from src.services.user import UserService, get_user_service

router = APIRouter()


class EnumStrMixin(enum.Enum):
    def __str__(self) -> str:
        return self.value


class FilterMonth(EnumStrMixin):
    january = "January"
    february = "February"
    march = "March"
    april = "April"
    may = "May"
    june = "June"
    july = "July"
    august = "August"
    september = "September"
    october = "October"
    november = "November"
    december = "December"


@router.get(
    path="/",
    response_model=MaterialListResponse,
    summary="Список показателей",
    tags=["Materials"],
)
def material_list(
        material_service: MaterialService = Depends(get_material_service),
        filter: Optional[FilterMonth] = None,
) -> MaterialListResponse:
    if not filter:
        filter = ""
    else:
        filter = filter.value
    materials: dict = material_service.get_material_list(filter)
    if not materials:
        # Если показатели не найдены, отдаём 404 статус
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Materials not found")
    return MaterialListResponse(**materials)


@router.get(
    path="/{Material_id}",
    response_model=MaterialModel,
    summary="Получить определенный показатель",
    tags=["Materials"],
)
def material_detail(
        material_id: int,
        material_service: MaterialService = Depends(get_material_service),
) -> MaterialModel:
    material: Optional[dict] = material_service.get_material_detail(item_id=material_id)
    if not material:
        # Если запись не найдена, отдаём 404 статус
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Material not found")
    return MaterialModel(**material)


@router.post(
    path="/",
    response_model=MaterialModel,
    summary="Создать показатель",
    tags=["Materials"],
    status_code=status.HTTP_201_CREATED,
)
def material_create(
    material: MaterialCreate,
    Authorize: AuthJWT = Depends(),
    material_service: MaterialService = Depends(get_material_service),
    user_service: UserService = Depends(get_user_service)
) -> MaterialModel:
    user = user_service.get_user_by_access_token(Authorize)
    if user:
        material: dict = material_service.create_material(material=material)
        return MaterialModel(**material)
    else:
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED, detail="Unauthorized user")
