import flet as ft
from constants import PRIMARY, DARK

def ServiceDetailView(title, description, image_url, on_back_click, on_order_click):
    return ft.Container(
        padding=20,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                # زر العودة
                ft.IconButton(ft.icons.ARROW_BACK_IOS_NEW_ROUNDED, on_click=on_back_click),
                
                # صورة الخدمة
                ft.Container(
                    height=200,
                    border_radius=20,
                    image_src=image_url,
                    image_fit=ft.ImageFit.COVER,
                ),
                
                ft.Text(title, size=28, weight="bold", color=DARK),
                ft.Text(description, size=16, color="grey"),
                
                ft.Divider(height=40),
                
                # زر الانتقال لطلب هذه الخدمة
                ft.ElevatedButton(
                    "اطلب هذه الخدمة الآن",
                    bgcolor=PRIMARY,
                    color="white",
                    height=50,
                    width=400,
                    on_click=on_order_click
                ),
            ]
        )
    )
