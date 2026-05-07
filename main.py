import flet as ft
import time
import threading
from views.home import HomeView
from views.works import WorksView
from views.order import OrderView
from views.about import AboutView
from views.service_details import ServiceDetailView

def main(page: ft.Page):
    # 1. تعريف الخط الجديد (تأكد أن الملف موجود داخل مجلد assets باسم pixel.ttf)
    page.fonts = {
        "PixelFont": "pixel.ttf"
    }
    
    # 2. تعيين الخط كخط افتراضي للتطبيق بالكامل
    page.theme = ft.Theme(font_family="PixelFont")
    
    page.title = "نبض البيكسل"
    page.rtl = True
    page.padding = 0
    page.bgcolor = "#f8f9fc"
    
    # إخفاء شريط التمرير
    page.scrollbar_theme = ft.ScrollbarTheme(
        thickness=0,
        radius=0,
        thumb_color=ft.colors.TRANSPARENT,
        track_color=ft.colors.TRANSPARENT,
    )

    container = ft.Container(expand=True)

    def show_service_details(service_name):
        page.navigation_bar.selected_index = None
        container.content = ServiceDetailView(
            title=service_name,
            on_back_click=lambda _: navigate(0),
            on_order_click=lambda _: navigate(2)
        )
        page.update()

    def navigate(index):
        page.navigation_bar.selected_index = index
        pages = {
            0: HomeView(on_order_click=lambda _: navigate(2), on_service_select=show_service_details),
            1: WorksView(),
            2: OrderView(),
            3: AboutView()
        }
        container.content = pages[index]
        page.update()

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="الرئيسية"),
            ft.NavigationDestination(icon=ft.icons.PALETTE, label="أعمالنا"),
            ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG, label="أطلب"),
            ft.NavigationDestination(icon=ft.icons.INFO, label="حولنا"),
        ],
        on_change=lambda e: navigate(e.control.selected_index)
    )

    def show_splash():
        page.navigation_bar = None
        container.content = ft.Container(
            expand=True,
            image_src="splash_bg.jpg",
            image_fit=ft.ImageFit.COVER,
            content=ft.Stack([
                ft.Container(expand=True, bgcolor=ft.colors.with_opacity(0.5, "black")),
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        # المؤشر الدائري
                        ft.ProgressRing(width=65, height=65, stroke_width=5, color="white"),
                        ft.Container(height=25),
                        
                        ft.Text("جاري التحميل...", size=16, color="white"),
                        ft.Container(height=15),
                        
                        # اسم التطبيق بالخط الجديد
                        ft.Text("نبض البيكسل", size=50, weight="bold", color="white"),
                        ft.Container(height=20),
                        
                        ft.Container(
                            padding=ft.padding.symmetric(horizontal=40),
                            content=ft.Text(
                                "نحن فريق شغوف بالتصميم الرقمي، نسعى لتحويل الأفكار التقليدية إلى هويات بصرية تنبض بالحياة. نؤمن بأن كل بكسل له قصة، ومهمتنا هي حكاية قصتك بأجمل صورة ممكنة لتترك أثراً لا ينسى.",
                                size=15,
                                color="white70",
                                text_align=ft.TextAlign.CENTER,
                            )
                        ),
                    ]
                )
            ])
        )
        page.update()

        def start_navigation():
            time.sleep(4)
            page.navigation_bar = nav_bar
            navigate(0)
            page.update()

        threading.Thread(target=start_navigation).start()

    page.add(container)
    show_splash()

# تشغيل التطبيق مع التأكد من مسار الـ assets للخط والصور
ft.app(target=main, assets_dir="assets")
