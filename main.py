import flet as ft
import urllib.parse

# constants
PRIMARY = "#6C2BD9"
SECONDARY = "#00C2FF"
DARK = "#111827"
WHATSAPP = "249112002131"

# Social Media Links
INSTAGRAM_URL = "https://instagram.com"
TWITTER_URL = "https://twitter.com"
FACEBOOK_URL = "https://facebook.com"

# About Text
ABOUT_TEXT = (
    "نحن فريق شغوف بالتصميم الرقمي، نسعى لتحويل الأفكار التقليدية إلى هويات بصرية تنبض بالحياة. "
    "نؤمن بأن كل بكسل له قصة، ومهمتنا هي حكاية قصتك بأجمل صورة ممكنة لتترك أثراً لا ينسى."
)

def main(page: ft.Page):
    page.title = "نبض البيكسل | Pixel Pulse"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True
    page.padding = 0
    page.bgcolor = "#f8f9fc"

    content_area = ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)

    # dialog closing
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    #zoom in the image
    def open_image(img_src):
        page.dialog = ft.AlertDialog(
            content=ft.Container(
                content=ft.Image(src=img_src, fit=ft.ImageFit.CONTAIN),
                border_radius=20,
                width=320,
                height=250,
            ),
            actions=[
                ft.TextButton("إغلاق", on_click=close_dialog)
            ],
        )
        page.dialog.open = True
        page.update()

    # ---------------- NAVIGATION LOGIC ----------------
    def show_page(index):
        pages = [
            home_page,       # 0
            works_page,      # 1
            order_page,      # 2
            about_page,      # 3
            logo_detail_page # 4
        ]
        content_area.controls.clear()
        content_area.controls.append(pages[index])
        
        if index < 4:
            page.navigation_bar.selected_index = index
            
        page.update()

    # ---------------- WORK ITEM COMPONENT ----------------
    def work_item(title, category, img_url):
        return ft.Container(
            width=page.width,
            height=180,
            bgcolor="white",
            border_radius=20,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.with_opacity(0.1, "black")),
            on_click=lambda _: open_image(img_url),
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

    # ---------------- LOGO DETAIL PAGE ----------------
    logo_detail_page = ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: show_page(0)),
                ft.Text("تفاصيل خدمة تصميم الشعارات", size=24, weight="bold", color=DARK),
                ft.Container(
                    border_radius=20,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    content=ft.Image(
                        src="works/1.jpg",
                        fit=ft.ImageFit.CONTAIN,
                    )
                ),
                ft.Container(height=10),
                ft.Text(
                    "نحن نحول رؤيتك إلى واقع بصرى ملموس. شعاراتنا تتميز بالبساطة والعمق لتترك أثراً لا ينسى.",
                    size=16, color="grey"
                ),
                ft.ElevatedButton(
                    "اطلب تصميمك الآن",
                    bgcolor=PRIMARY,
                    color="white",
                    on_click=lambda _: show_page(2)
                )
            ]
        )
    )

    # ---------- CARD COMPONENT (Home) ----------
    def service_card(icon, title, desc, target_index=None):
        return ft.Container(
            bgcolor="white",
            border_radius=18,
            padding=15,
            on_click=lambda _: show_page(target_index) if target_index is not None else None,
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
                            ft.Text(title, size=16, weight=ft.FontWeight.BOLD),
                            ft.Text(desc, size=12, color="grey"),
                        ]
                    )
                ]
            )
        )

    # --- TESTIMONIAL CARD ---
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
    hero = ft.Container(
        padding=30,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[PRIMARY, SECONDARY],
        ),
        border_radius=ft.border_radius.only(bottom_left=30, bottom_right=30),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.icons.BOLT, size=50, color="white"),
                ft.Text("نبض البيكسل", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text("هنا نصنع هويتك الرقمية بإحتراف", size=16, color="white70"),
                ft.Container(height=10),
                ft.ElevatedButton(
                    text="اطلب الآن",
                    bgcolor="white",
                    color=PRIMARY,
                    on_click=lambda e: show_page(2)
                ),
            ]
        )
    )

    home_page = ft.Column(
        controls=[
            hero,
            ft.Container(
                padding=20,
                content=ft.Column(
                    spacing=15,
                    controls=[
                        ft.Text("خدماتنا", size=24, weight=ft.FontWeight.BOLD, color=DARK),
                        service_card(ft.icons.BRUSH, "تصميم شعارات", "هوية احترافية تبرز مشروعك", target_index=4),
                        service_card(ft.icons.PHONE_IPHONE, "تصميم تطبيقات", "واجهات عصرية وتجربة مستخدم", target_index=5),
                        service_card(ft.icons.CAMPAIGN, "سوشيال ميديا", "منشورات جذابة وإعلانات قوية"),
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

    # --- WORKS PAGE
    works_page = ft.Container(
        padding=20,
        content=ft.Column(
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text("معرض المشاريع الإبداعية", size=26, weight="bold", color=DARK),
                ft.Text("نماذج من أحدث تصاميمنا الاحترافية (انقر للتكبير)", size=13, color="grey"),
                work_item("هوية شركة تكنولوجيا", "تصميم شعارات", "works/1.jpg"),
                work_item("تطبيق توصيل طعام", "واجهة مستخدم UI", "works/2.jpg"),
                work_item("حملة رمضانية", "سوشيال ميديا", "works/3.jpg"),
                work_item("غلاف مجلة فنية", "مطبوعات", "works/4.jpg"),
            ]
        )
    )

    # ---------------- ORDER PAGE ----------------
    name_field = ft.TextField(label="الاسم الكريم", prefix_icon=ft.icons.PERSON_OUTLINE, border_radius=15, border_color=PRIMARY, bgcolor="white")
    phone_field = ft.TextField(label="رقم التواصل", prefix_icon=ft.icons.PHONE_ANDROID_OUTLINED, border_radius=15, border_color=PRIMARY, bgcolor="white", keyboard_type=ft.KeyboardType.PHONE)
    details_field = ft.TextField(label="تفاصيل مشروعك الإبداعي", prefix_icon=ft.icons.DESCRIPTION_OUTLINED, multiline=True, min_lines=4, border_radius=15, border_color=PRIMARY, bgcolor="white")

    def send_whatsapp(e):
        msg = f"الاسم: {name_field.value}\nالهاتف: {phone_field.value}\nالتفاصيل: {details_field.value}"
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
                        ft.Text("أبدأ رحلتك الإبداعية مع نبض البيكسل", size=20, weight="bold", color=DARK),
                        ft.Text("أخبرنا بما يدور في ذهنك وسنتواصل معك فوراً", size=14, color="grey"),
                    ]
                ),
                ft.Divider(height=10, color="transparent"),
                name_field, phone_field, details_field,
                ft.Container(
                    margin=ft.margin.only(top=10),
                    content=ft.ElevatedButton(
                        content=ft.Row([ft.Icon(ft.icons.SEND_ROUNDED), ft.Text("إرسال الطلب عبر واتساب", size=16, weight="bold")], alignment=ft.MainAxisAlignment.CENTER),
                        style=ft.ButtonStyle(color="white", bgcolor=PRIMARY, shape=ft.RoundedRectangleBorder(radius=15)),
                        width=400, height=55, on_click=send_whatsapp
                    )
                ),
            ]
        )
    )

    # ---------------- ABOUT PAGE (Modified for Flet 0.19.0) ----------------
    def social_icon_btn(icon, color, url):
        return ft.IconButton(
            icon=icon,
            icon_color=color,
            icon_size=30,
            on_click=lambda _: page.launch_url(url),
        )

    about_page = ft.Container(
        padding=20,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            spacing=25,
            controls=[
                ft.Container(height=20),
                ft.CircleAvatar(
                    content=ft.Icon(ft.icons.AUTO_AWESOME_MOTION, size=40, color=PRIMARY),
                    bgcolor="#eef2ff",
                    radius=45,
                ),
                ft.Text("نبض البيكسل", size=28, weight="bold", color=DARK),
                ft.Container(
                    bgcolor="white",
                    padding=25,
                    border_radius=20,
                    shadow=ft.BoxShadow(blur_radius=15, color=ft.colors.with_opacity(0.1, "black")),
                    content=ft.Text(
                        ABOUT_TEXT,
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.colors.GREY_800,
                    )
                ),
                ft.Text("تواصل معنا", size=18, weight="bold", color=DARK),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        social_icon_btn(ft.icons.CAMERA_ALT_OUTLINED, "#E4405F", INSTAGRAM_URL),
                        social_icon_btn(ft.icons.FACEBOOK_OUTLINED, "#1877F2", FACEBOOK_URL),
                        social_icon_btn(ft.icons.CHAT_OUTLINED, "#25D366", f"https://wa.me/{WHATSAPP}"),
                    ]
                ),
                ft.Text("الإصدار 1.0.0", size=12, color="grey"),
            ]
        )
    )

    # ---------------- NAVIGATION ----------------
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

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
