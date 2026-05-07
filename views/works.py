import flet as ft
from constants import DARK, SECONDARY

def WorksView():
    # عنصر المشروع البرمجي
    def work_item(title, category, img_url):
        return ft.Container(
            height=180,
            bgcolor="white",
            border_radius=20,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(0.1, "black")),
            content=ft.Stack([
                ft.Image(src=img_url, fit=ft.ImageFit.COVER, width=1000),
                ft.Container(
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.bottom_center,
                        end=ft.alignment.top_center,
                        colors=["black", "transparent"]
                    ),
                    padding=20,
                    content=ft.Column([
                        ft.Text(category, color=SECONDARY, size=12, weight="bold"),
                        ft.Text(title, color="white", size=18, weight="bold"),
                    ], alignment=ft.MainAxisAlignment.END)
                )
            ])
        )

    return ft.Container(
        padding=20,
        content=ft.Column(
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text("معرض المشاريع الإبداعية", size=26, weight="bold", color=DARK),
                ft.Text("نماذج من أحدث تصاميمنا الاحترافية", size=13, color="grey"),
                work_item("هوية شركة تكنولوجيا", "تصميم شعارات", "works/1.jpg"),
                work_item("تطبيق توصيل طعام", "واجهة مستخدم UI", "works/2.jpg"),
                work_item("حملة رمضانية", "سوشيال ميديا", "works/3.jpg"),
            ]
        )
    )
