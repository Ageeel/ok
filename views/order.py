import flet as ft
import urllib.parse
from constants import PRIMARY, DARK, WHATSAPP

def OrderView():
    name_field = ft.TextField(label="الاسم الكريم", border_radius=15, border_color=PRIMARY)
    phone_field = ft.TextField(label="رقم التواصل", border_radius=15, border_color=PRIMARY)
    details_field = ft.TextField(label="تفاصيل مشروعك", multiline=True, min_lines=4, border_radius=15)

    def send_whatsapp(e):
        msg = f"الاسم: {name_field.value}\nالهاتف: {phone_field.value}\nالتفاصيل: {details_field.value}"
        url = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg)}"
        e.page.launch_url(url)

    return ft.Container(
        padding=30,
        content=ft.Column(
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.icons.EDIT_NOTE_ROUNDED, size=50, color=PRIMARY),
                ft.Text("أبدأ رحلتك الإبداعية", size=20, weight="bold", color=DARK),
                name_field, 
                phone_field, 
                details_field,
                ft.ElevatedButton(
                    "إرسال الطلب عبر واتساب",
                    color="white", bgcolor=PRIMARY,
                    height=55, width=400,
                    on_click=send_whatsapp
                ),
            ]
        )
    )
