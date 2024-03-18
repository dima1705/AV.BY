import uvicorn
from fastapi import FastAPI
from admin.views import UserAdmin, AutoAdmin, TGUserAdmin, BrandAdmin, ModelAdmin, GenerationAdmin

from routers.auto_router import router as auto_router
from routers.b_m_g_router import router as b_m_g_router
from routers.photo_router import router as photo_router
from routers.user_router import router as user_router

from fastapi.middleware.cors import CORSMiddleware
from db import sync_engin
from sqladmin import Admin


app = FastAPI(title="AV_API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auto_router)
app.include_router(b_m_g_router)
app.include_router(photo_router)
app.include_router(user_router)

admin = Admin(app, sync_engin)

admin.add_view(UserAdmin)
admin.add_view(AutoAdmin)
admin.add_view(TGUserAdmin)
admin.add_view(BrandAdmin)
admin.add_view(ModelAdmin)
admin.add_view(GenerationAdmin)

if __name__ == '__main__':
    uvicorn.run(
        "av:app",
        host='127.0.0.1',
        port=8000,
        reload=True,
    )
