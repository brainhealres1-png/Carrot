import reflex as rx


class State(rx.State):
    name: str = ""
    message: str = ""
    show_message: bool = False

    def handle_submit(self):
        if self.name.strip():
            self.message = f"안녕하세요, {self.name}님! 👋"
            self.show_message = True
        else:
            self.message = "이름을 입력해주세요."
            self.show_message = True

    def clear_message(self):
        self.show_message = False


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("🥕 Carrot", size="xl"),
            rx.text("이름을 입력해주세요"),
            rx.input(
                placeholder="예: 홍길동",
                value=State.name,
                on_change=State.set_name,
                width="100%",
            ),
            rx.button(
                "제출",
                on_click=State.handle_submit,
                width="100%",
            ),
            rx.cond(
                State.show_message,
                rx.box(
                    rx.text(State.message),
                    padding="1rem",
                    background_color="#d4edda",
                    border_radius="0.5rem",
                    color="#155724",
                ),
            ),
            spacing="1rem",
            align_items="center",
            width="100%",
            max_width="400px",
        ),
        center_content=True,
        padding="2rem",
    )


app = rx.App()
app.add_page(index)
