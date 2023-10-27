from fastapi import APIRouter, Request

router = APIRouter(prefix="/todo")


@router.get("/")
async def root(request: Request):
    return {"message": str(request.cookies)}