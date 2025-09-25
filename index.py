import flet as ft

class PDFConverterApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.setup_page()
        self.create_main_view()

    def setup_page(self):
        self.page.title = "PDF Converter"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor = "#F2F2F7"
        self.page.window_width = 400
        self.page.window_height = 700
        self.page.window_resizable = False
        self.page.padding = 0
        self.page.spacing = 0

    def create_main_view(self):
        self.main_container = ft.Container(
            content=ft.Column([
                self.create_header(),
                self.create_cards_section(),
            ]),
            bgcolor="#F2F2F7",
            expand=True,
        )
        
        self.page.add(self.main_container)
        self.page.update()

    def create_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Container(height=50),
                ft.Text(
                    "PDF Converter",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="#000000",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Convert your files easily",
                    size=16,
                    color="#8E8E93",
                    text_align=ft.TextAlign.CENTER,
                ),
            ]),
            padding=ft.padding.all(20),
            alignment=ft.alignment.center,
        )

    def create_cards_section(self):
        return ft.Container(
            content=ft.Column([
                self.create_card(
                    title="PDF to Word",
                    subtitle="Convert PDF files to Word documents",
                    icon=ft.icons.DESCRIPTION,
                    color="#007AFF",
                    on_click=lambda _: self.open_pdf_to_word()
                ),
                ft.Container(height=20),
                self.create_card(
                    title="Word to PDF",
                    subtitle="Convert Word documents to PDF files",
                    icon=ft.icons.PICTURE_AS_PDF,
                    color="#FF3B30",
                    on_click=lambda _: self.open_word_to_pdf()
                ),
            ]),
            padding=ft.padding.all(20),
        )

    def create_card(self, title, subtitle, icon, color, on_click):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(
                        icon,
                        color="white",
                        size=24,
                    ),
                    width=50,
                    height=50,
                    bgcolor=color,
                    border_radius=12,
                    alignment=ft.alignment.center,
                ),
                ft.Container(width=15),
                ft.Column([
                    ft.Text(
                        title,
                        size=18,
                        weight=ft.FontWeight.W600,
                        color="#000000",
                    ),
                    ft.Text(
                        subtitle,
                        size=14,
                        color="#8E8E93",
                    ),
                ], spacing=2, expand=True),
                ft.Icon(
                    ft.icons.CHEVRON_RIGHT,
                    color="#C7C7CC",
                    size=20,
                ),
            ]),
            bgcolor="white",
            border_radius=12,
            padding=ft.padding.all(20),
            on_click=on_click,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=10,
                color=ft.colors.with_opacity(0.1, "#000000"),
                offset=ft.Offset(0, 2),
            ),
            animate=ft.animation.Animation(100, ft.AnimationCurve.EASE_OUT),
        )

    def create_web_view(self, url, title):
        web_view = ft.WebView(
            url=url,
            expand=True,
        )
        
        back_button = ft.Container(
            content=ft.Row([
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK_IOS,
                    icon_color="white",
                    on_click=lambda _: self.go_back(),
                ),
                ft.Text(
                    title,
                    size=18,
                    weight=ft.FontWeight.W600,
                    color="white",
                ),
            ]),
            bgcolor="#007AFF",
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
            height=80,
        )
        
        return ft.Column([
            back_button,
            web_view,
        ], spacing=0, expand=True)

    def open_pdf_to_word(self):
        web_view_container = self.create_web_view(
            "https://www.ilovepdf.com/pdf_to_word",
            "PDF to Word"
        )
        self.page.clean()
        self.page.add(web_view_container)
        self.page.update()

    def open_word_to_pdf(self):
        web_view_container = self.create_web_view(
            "https://www.ilovepdf.com/word_to_pdf",
            "Word to PDF"
        )
        self.page.clean()
        self.page.add(web_view_container)
        self.page.update()

    def go_back(self):
        self.page.clean()
        self.create_main_view()

def main(page: ft.Page):
    app = PDFConverterApp(page)

if __name__ == "__main__":
    ft.app(target=main)