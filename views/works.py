import flet as ft
from constants import DARK, SECONDARY
import plyer  

def WorksView():
    # دالة المشاركة مع نظام "دعم احتياطي"
    def native_share(page, title, category):
        share_text = f"شاهد هذا المشروع: {title}\nالتصنيف: {category}"
        try:
            plyer.share.share(title=title, message=share_text)
        except Exception:
            # إذا لم تفتح القائمة، يتم النسخ تلقائياً كبديل
            page.set_clipboard(share_text)
            page.snack_bar = ft.SnackBar(
                ft.Text("تم نسخ تفاصيل المشروع للحافظة"),
                bgcolor=SECONDARY
            )
            page.snack_bar.open = True
            page.update()

    def close_bs(page, bs):
        bs.open = False
        page.update()

    def show_detail(e, title, category, img_url):
        page = e.page
        bs = ft.BottomSheet(
            ft.Container(
                padding=ft.padding.only(left=25, right=25, top=15, bottom=40), # زيادة البادينج السفلي هنا
                bgcolor="white",
                border_radius=ft.border_radius.only(top_left=30, top_right=30),
                content=ft.Column(
                    tight=True,
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(width=40, height=4, bgcolor="grey300", border_radius=10),
                        ft.Image(src=img_url, border_radius=15, height=200, fit=ft.ImageFit.COVER),
                        ft.Row([
                            ft.Column([
                                ft.Text(title, size=22, weight="bold", color=DARK),
                                ft.Text(category, size=14, color=SECONDARY),
                            ], expand=True),
                            ft.IconButton(
                                icon=ft.icons.SHARE_ROUNDED, 
                                icon_color=DARK,
                                on_click=lambda _: native_share(page, title, category)
                            ),
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Divider(height=1, color="grey100"),
                        ft.Row([
                            ft.ElevatedButton("زيارة العمل", expand=True, style=ft.ButtonStyle(bgcolor=DARK, color="white")),
                            ft.OutlinedButton("إغلاق", on_click=lambda _: close_bs(page, bs)),
                        ], spacing=10),
                    ]
                )
            )
        )
        page.bottom_sheet = bs
        bs.open = True
        page.update()

    def work_item(title, category, img_url):
        return ft.Container(
            height=180,
            bgcolor="white",
            border_radius=20,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            on_click=lambda e: show_detail(e, title, category, img_url),
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
        # تم تعديل البادينج هنا لإبعاد العناصر عن حافة الشاشة السفلية
        padding=ft.padding.only(left=20, right=20, top=20, bottom=100), 
        content=ft.Column(
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text("معرض المشاريع الإبداعية", size=26, weight="bold", color=DARK),
                work_item("هوية شركة تكنولوجيا", "تصميم شعارات", "works/1.jpg"),
                work_item("تطبيق توصيل طعام", "واجهة مستخدم UI", "works/2.jpg"),
                work_item("حملة رمضانية", "سوشيال ميديا", "works/3.jpg"),
                # حاوية فارغة إضافية للتأكد من وجود مساحة عند التمرير للنهاية
                ft.Container(height=20) 
            ]
        )
    )
