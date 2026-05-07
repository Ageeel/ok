import flet as ft
from constants import PRIMARY, SECONDARY, DARK

def HomeView(on_order_click, on_service_select):
    # 1. مكوّن بطاقة الخدمة (الشبكة)
    def service_card(icon, title, desc):
        return ft.Container(
            col={"xs": 6},
            bgcolor="white",
            border_radius=18,
            padding=15,
            on_click=lambda _: on_service_select(title),
            shadow=ft.BoxShadow(
                blur_radius=15, 
                color=ft.colors.with_opacity(0.07, "black"),
                offset=ft.Offset(0, 5)
            ),
            content=ft.Column([
                ft.Container(
                    width=45, height=45, bgcolor="#f0f7ff", 
                    border_radius=12, content=ft.Icon(icon, color=PRIMARY, size=24)
                ),
                ft.Text(title, size=14, weight="bold", color=DARK, text_align=ft.TextAlign.CENTER),
                ft.Text(desc, size=10, color="grey", text_align=ft.TextAlign.CENTER, max_lines=1),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8)
        )

    # 2. مكوّن "قالوا عن نبض البيكسل"
    def testimonial_card(name, text):
        return ft.Container(
            width=260,
            bgcolor="white",
            padding=20,
            border_radius=20,
            border=ft.border.all(1, "#f1f5f9"),
            content=ft.Column([
                ft.Icon(ft.icons.FORMAT_QUOTE_ROUNDED, color=SECONDARY, size=25),
                ft.Text(text, size=12, italic=True, color="#4b5563"),
                ft.Text(name, size=11, weight="bold", color=PRIMARY),
            ], spacing=10)
        )

    # 3. قسم الهيرو (Header)
    hero = ft.Container(
        padding=30,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[PRIMARY, SECONDARY]
        ),
        border_radius=ft.border_radius.only(bottom_left=35, bottom_right=35),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.icons.BOLT_ROUNDED, size=55, color="white"),
                ft.Text("نبض البيكسل", size=32, weight="bold", color="white"),
                ft.Text("هوية بصرية تنبض بالحياة", size=16, color="white70"),
                ft.Container(height=10),
                ft.ElevatedButton(
                    "اطلب الآن", 
                    bgcolor="white", 
                    color=PRIMARY,
                    on_click=on_order_click
                )
            ], spacing=5
        )
    )
    
    # 4. بناء الصفحة كاملة داخل Column قابل للتمرير
    return ft.Column(
        expand=True,
        scroll=ft.ScrollMode.HIDDEN, # إخفاء الشريط مع السماح بالتمرير
        spacing=0,
        controls=[
            hero,
            ft.Container(
                padding=25,
                content=ft.Column([
                    ft.Text("خدماتنا الإبداعية", size=22, weight="bold", color=DARK),
                    # شبكة الخدمات
                    ft.ResponsiveRow(
                        spacing=12,
                        run_spacing=12,
                        controls=[
                            service_card(ft.icons.BRUSH_ROUNDED, "تصميم شعارات", "هوية احترافية"),
                            service_card(ft.icons.PHONE_IPHONE_ROUNDED, "تصميم تطبيقات", "واجهات عصرية"),
                            service_card(ft.icons.CAMPAIGN_ROUNDED, "سوشيال ميديا", "منشورات جذابة"),
                            service_card(ft.icons.COLOR_LENS_ROUNDED, "هوية متكاملة", "بناء علامة"),
                        ]
                    ),
                    
                    ft.Divider(height=40, color="transparent"),
                    
                    # قسم الآراء
                    ft.Text("قالوا عن نبض البيكسل", size=20, weight="bold", color=DARK),
                    ft.Row([
                        testimonial_card("شركة المسار", "دقة مذهلة في التصميم وسرعة في التنفيذ."),
                        testimonial_card("متجر الأناقة", "أفضل تجربة هوية بصرية حصلنا عليها."),
                    ], scroll=ft.ScrollMode.ALWAYS, spacing=15),
                    
                ], spacing=15)
            ),
            ft.Container(height=40) # مساحة سفلية
        ]
    )
