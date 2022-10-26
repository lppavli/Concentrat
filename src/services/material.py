import json
from functools import lru_cache
from typing import Optional

from fastapi import Depends
from sqlmodel import Session

from src.api.v1.schemas import MaterialCreate, MaterialModel
from src.db import AbstractCache, get_cache, get_session
from src.models import Material
from src.services import ServiceMixin

__all__ = ("MaterialService", "get_material_service")


class MaterialService(ServiceMixin):
    def get_material_list(self, filt: str) -> dict:
        """Получить список показателей."""
        if filt:
            materials = self.session.query(Material).filter(
                Material.month == filt).all()
        else:
            materials = self.session.query(Material).all()
        return {"Materials": [MaterialModel(**material.dict()) for material in
                              materials]}

    def get_material_list_for_report(self, filt: str) -> dict:
        """Получить список показателей для отчета."""
        materials = self.session.query(Material).filter(
            Material.month == filt).all()
        m = {"iron_amount": [item.iron_amount for item in materials],
             "silicon_amount": [item.silicon_amount for item in materials],
             "aluminum_amount": [item.aluminum_amount for item in materials],
             "sodium_amount": [item.sodium_amount for item in materials],
             "sulfur_amount": [item.sulfur_amount for item in materials]}
        reports = []
        for key, value in m.items():
            reports.append(
                {"value": key,
                 "min_value": min(value),
                 "max_value": max(value)}
            )
        return {"Materials": [report for report in
                              reports]}


    def get_material_detail(self, item_id: int) -> Optional[dict]:
        """Получить детальную информацию показателя."""
        if cached_Material := self.cache.get(key=f"{item_id}"):
            return json.loads(cached_Material)

        material = self.session.query(Material).filter(
            Material.id == item_id).first()
        if material:
            self.cache.set(key=f"{material.id}", value=material.json())
        return material.dict() if material else None

    def create_material(self, material: MaterialCreate) -> dict:
        """Создать показатель."""
        new_material = Material(
            name=material.name,
            iron_amount=material.iron_amount,
            silicon_amount=material.silicon_amount,
            aluminum_amount=material.aluminum_amount,
            sodium_amount=material.sodium_amount,
            sulfur_amount=material.sulfur_amount,
            month=material.month
        )
        self.session.add(new_material)
        self.session.commit()
        self.session.refresh(new_material)
        return new_material.dict()


@lru_cache()
def get_material_service(
        cache: AbstractCache = Depends(get_cache),
        session: Session = Depends(get_session),
) -> MaterialService:
    return MaterialService(cache=cache, session=session)
