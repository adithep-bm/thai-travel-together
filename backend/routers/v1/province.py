from fastapi import APIRouter
from ...schemas import province_schema

router = APIRouter(prefix="/provinces", tags=["provinces"])


@router.get("/")
async def get_provinces() -> list[province_schema.Province]:
    return [
        province_schema.Province(id=1, name="Bangkok"),
        province_schema.Province(id=2, name="Chiang Mai"),
        province_schema.Province(id=3, name="Phuket"),
    ]


@router.get("/{province_id}")
async def get_province(province_id: int) -> province_schema.Province:
    return province_schema.Province(id=province_id, name="Sample Province")


@router.post("/")
async def create_province(
    province: province_schema.Province,
) -> province_schema.Province:
    return province


@router.put("/{province_id}")
async def update_province(
    province_id: int, province: province_schema.Province
) -> province_schema.Province:
    return province


@router.delete("/{province_id}")
async def delete_province(province_id: int) -> dict:
    return {"message": f"Province with ID {province_id} has been deleted."}
