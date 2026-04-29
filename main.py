import flet as ft
import urllib.parse

# constants
PRIMARY = "#6C2BD9"
SECONDARY = "#00C2FF"
DARK = "#111827"
WHATSAPP = "249112002131"

# About Text
ABOUT_TEXT = (
    "في نبض البيكسل، لا نصمم مجرد صور، بل نصنع هوية تنبض بالحياة. "
    "نحن فريق من المبدعين المتخصصين في فنون التصميم الجرافيكي وصناعة المحتوى الإعلامي، نؤمن بأن كل بكسل له قصة، ومهمتنا هي سرد قصتكم بأبهى صورة ممكنة.\n\n"
    "رؤيتنا\n"
    "أن نكون الشريك الإبداعي الأول للمؤسسات والطموحين، من خلال تقديم حلول بصرية مبتكرة تدمج بين الفن والتكنولوجيا.\n\n"
    "ماذا نقدم؟\n"
    "• تصميم الشعارات والهويات البصرية\n"
    "• تصميم البوسترات والمطبوعات\n"
    "• تصميم تطبيقات ومواقع\n"
    "• إدارة المحتوى الإعلامي\n"
)

def main(page: ft.Page):
    page.title = "نبض البيكسل | Pixel Pulse"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True
    page.padding = 0
    page.bgcolor = "#f8f9fc"

    content_area = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)

    # --- وظيفة إغلاق النافذة المنبثقة ---
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    # --- وظيفة تكبير الصور ---
    def open_image(e):
        img_src = e.control.data
        page.dialog = ft.AlertDialog(
            content=ft.Container(
                content=ft.Image(src=img_src, fit=ft.ImageFit.CONTAIN),
                border_radius=20,
            ),
            actions=[
                ft.TextButton("إغلاق", on_click=close_dialog)
            ],
        )
        page.dialog.open = True
        page.update()

    # ---------------- HERO ----------------
    hero = ft.Container(
        padding=30,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[PRIMARY, SECONDARY],
        ),
        border_radius=ft.border_radius.only(
            bottom_left=30,
            bottom_right=30
        ),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.icons.BOLT, size=60, color="white"),
                ft.Text(
                    "نبض البيكسل",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="white"
                ),
                ft.Text(
                    "نصنع هويتك الرقمية باحتراف",
                    size=16,
                    color="white70"
                ),
                ft.Container(height=10),
                ft.ElevatedButton(
                    text="اطلب الآن",
                    bgcolor="white",
                    color=PRIMARY,
                    on_click=lambda e: show_page(2) # الانتقال لصفحة الطلب
                ),
            ]
        )
    )

    # ---------------- CARD COMPONENT ----------------
    def service_card(icon, title, desc):
        return ft.Container(
            bgcolor="white",
            border_radius=18,
            padding=15,
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=50,
                        height=50,
                        bgcolor="#eef2ff",
                        border_radius=15,
                        content=ft.Icon(icon, color=PRIMARY)
                    ),
                    ft.Column(
                        expand=True,
                        controls=[
                            ft.Text(
                                title,
                                size=16,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.Text(
                                desc,
                                size=12,
                                color="grey"
                            ),
                        ]
                    )
                ]
            )
        )

    # --- مكون: رأي عميل ---
    def testimonial_card(name, text):
        return ft.Container(
            width=250,
            bgcolor="white",
            padding=15,
            border_radius=15,
            border=ft.border.all(1, "#f1f5f9"),
            content=ft.Column([
                ft.Icon(ft.icons.FORMAT_QUOTE, color=SECONDARY, size=20),
                ft.Text(text, size=12, italic=True),
                ft.Text(name, size=11, weight="bold", color=PRIMARY),
            ])
        )

    # ---------------- HOME PAGE ----------------
    home_page = ft.Column(
        controls=[
            hero,
            ft.Container(
                padding=20,
                content=ft.Column(
                    spacing=15,
                    controls=[
                        ft.Text(
                            "خدماتنا",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=DARK
                        ),
                        service_card(
                            ft.icons.BRUSH,
                            "تصميم شعارات",
                            "هوية احترافية تبرز مشروعك"
                        ),
                        service_card(
                            ft.icons.PHONE_IPHONE,
                            "تصميم تطبيقات",
                            "واجهات عصرية وتجربة مستخدم"
                        ),
                        service_card(
                            ft.icons.CAMPAIGN,
                            "سوشيال ميديا",
                            "منشورات جذابة وإعلانات قوية"
                        ),
                        # --- قسم قالوا عن نبض البيكسل ---
                        ft.Divider(height=30, color="transparent"),
                        ft.Text("قالوا عن نبض البيكسل", size=20, weight="bold", color=DARK),
                        ft.Row([
                            testimonial_card("شركة المسار", "دقة مذهلة في التصميم وسرعة في التنفيذ."),
                            testimonial_card("متجر الأناقة", "أفضل تجربة هوية بصرية حصلنا عليها.")
                        ], scroll=ft.ScrollMode.ALWAYS)
                    ]
                )
            )
        ]
    )

    # ---------------- ABOUT PAGE ----------------
    about_page = ft.Container(
        padding=20,
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text(
                    "من نحن؟",
                    size=24,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Container(
                    bgcolor="white",
                    border_radius=20,
                    padding=20,
                    content=ft.Text(
                        ABOUT_TEXT,
                        size=14,
                        text_align=ft.TextAlign.RIGHT
                    )
                )
            ]
        )
    )

    # ---------------- ORDER PAGE ----------------
    name = ft.TextField(
        label="الاسم الكريم",
        prefix_icon=ft.icons.PERSON_OUTLINE,
        border_radius=15,
        border_color=PRIMARY,
        bgcolor="white",
    )
    phone = ft.TextField(
        label="رقم التواصل",
        prefix_icon=ft.icons.PHONE_ANDROID_OUTLINED,
        border_radius=15,
        border_color=PRIMARY,
        bgcolor="white",
        keyboard_type=ft.KeyboardType.PHONE
    )
    details = ft.TextField(
        label="تفاصيل مشروعك الإبداعي",
        prefix_icon=ft.icons.DESCRIPTION_OUTLINED,
        multiline=True,
        min_lines=4,
        border_radius=15,
        border_color=PRIMARY,
        bgcolor="white",
    )

    def send_whatsapp(e):
        msg = f"الاسم: {name.value}\nالهاتف: {phone.value}\nالتفاصيل: {details.value}"
        url = f"https://wa.me/{WHATSAPP}?text={urllib.parse.quote(msg)}"
        page.launch_url(url)

    order_page = ft.Container(
        padding=30,
        content=ft.Column(
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        ft.Icon(ft.icons.EDIT_NOTE_ROUNDED, size=50, color=PRIMARY),
                        ft.Text(
                            "ابدأ رحلتك الإبداعية معنا",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                            color=DARK
                        ),
                        ft.Text(
                            "أخبرنا بما يدور في ذهنك وسنتواصل معك فوراً",
                            size=14,
                            color="grey"
                        ),
                    ]
                ),
                ft.Divider(height=10, color="transparent"),
                name,
                phone,
                details,
                ft.Container(
                    margin=ft.margin.only(top=10),
                    content=ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.SEND_ROUNDED),
                                ft.Text("إرسال الطلب عبر واتساب", size=16, weight=ft.FontWeight.BOLD),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        style=ft.ButtonStyle(
                            color="white",
                            bgcolor=PRIMARY,
                            shape=ft.RoundedRectangleBorder(radius=15),
                        ),
                        width=400,
                        height=55,
                        on_click=send_whatsapp
                    )
                ),
                ft.Row(
                    [
                        ft.Icon(ft.icons.LOCK_OUTLINE, size=14, color="grey"),
                        ft.Text("بياناتك في أمان وسيتم الرد خلال أقل من 24 ساعة", size=12, color="grey"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        )
    )

    # ---------------- WORKS PAGE ----------------
    works_page = ft.Container(
        padding=20,
        expand=True,
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text(
                    "أعمالنا",
                    size=26,
                    weight=ft.FontWeight.BOLD,
                    color=DARK
                ),
                ft.Text(
                    "نماذج من أحدث تصاميمنا الاحترافية (انقر للتكبير)",
                    size=13,
                    color="grey"
                ),
                ft.Container(height=15),
                ft.GridView(
                    expand=True,
                    runs_count=2,
                    max_extent=220,
                    child_aspect_ratio=0.85,
                    spacing=12,
                    run_spacing=12,
                    controls=[
                        ft.GestureDetector(
                            content=ft.Image(src=f"images/work{i}.jpg", fit=ft.ImageFit.COVER, border_radius=20),
                            on_tap=open_image,
                            data=f"images/work{i}.jpg"
                        ) for i in range(1, 5)
                    ]
                )
            ]
        )
    )

    # ---------------- NAVIGATION LOGIC ----------------
    def show_page(index):
        pages = [
            home_page,
            works_page,
            order_page,
            about_page,
        ]
        content_area.controls.clear()
        content_area.controls.append(pages[index])
        page.update()

    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_ROUNDED, label="الرئيسية"),
            ft.NavigationDestination(icon=ft.icons.PALETTE_ROUNDED, label="أعمالنا"),
            ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG, label="أطلب"),
            ft.NavigationDestination(icon=ft.icons.INFO_OUTLINE_ROUNDED, label="حولنا"),
        ],
        on_change=lambda e: show_page(e.control.selected_index)
    )

    page.add(content_area)
    show_page(0)

ft.app(
    target=main,
    view=ft.AppView.WEB_BROWSER,
    assets_dir=".",
    port=46715
)
