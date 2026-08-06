from fastapi import APIRouter, Depends

from app.core.security.roles import require_roles


router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get("/dashboard")
def admin_dashboard(
    user=Depends(require_roles("admin"))
):
    return {
        "message": "Welcome admin",
        "user": user.username,
    }