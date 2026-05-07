# views/about.py
import flet as ft
from constants import PRIMARY, DARK, ABOUT_TEXT, WHATSAPP, INSTAGRAM_URL, FACEBOOK_URL

def AboutView():
    APP_VERSION = "1.0.0"

    def social_btn(icon, color, url):
        return ft.Container(
            content=ft.IconButton(icon=icon, icon_color=color, on_click=lambda _: ft.Page.launch_url(None, url)),
            bgcolor=ft.colors.with_opacity(0.05, color),
            border_radius=12
        )

    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.HIDDEN, # هذه الخاصية تخفي الشريط وتعمل في Pydroid
        controls=[
            ft.Container(
                padding=30,
                content=ft.Column([
                    ft.Container(height=10),
                    ft.CircleAvatar(content=ft.Icon(ft.icons.AUTO_AWESOME_MOTION, color=PRIMARY), radius=45, bgcolor="#eef2ff"),
                    ft.Text("نبض البيكسل", size=28, weight="bold", color=DARK),
                    ft.Container(
                        bgcolor="white", padding=25, border_radius=20,
                        shadow=ft.BoxShadow(blur_radius=15, color=ft.colors.with_opacity(0.05, "black")),
                        content=ft.Text(ABOUT_TEXT, text_align=ft.TextAlign.CENTER, color="#4b5563")
                    ),
                    ft.Text("تواصل معنا", size=18, weight="bold", color=DARK),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,
                        controls=[
                            social_btn(ft.icons.CAMERA_ALT, "#E4405F", INSTAGRAM_URL),
                            social_btn(ft.icons.FACEBOOK, "#1877F2", FACEBOOK_URL),
                            social_btn(ft.icons.CHAT, "#25D366", f"https://wa.me/{WHATSAPP}"),
                        ]
                    ),
                    ft.Divider(height=40, color="transparent"),
                    ft.Text(f"الإصدار {APP_VERSION}", size=12, color="grey700"),
                    ft.Text("جميع الحقوق محفوظة © 2026", size=10, color="grey500"),
                    ft.Container(height=20),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=25)
            )
        ]
    )
