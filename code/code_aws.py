import reflex as rx
import httpx

# Lambda API 엔드포인트 (배포 후 수정)
LAMBDA_API_URL = "https://YOUR_LAMBDA_API_GATEWAY_URL/names"

class State(rx.State):
    name: str = ""
    message: str = ""
    show_message: bool = False
    is_loading: bool = False

    async def handle_submit(self):
        if not self.name.strip():
            self.message = "이름을 입력해주세요."
            self.show_message = True
            return
        
        self.is_loading = True
        try:
            # Lambda API에 POST 요청
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    LAMBDA_API_URL,
                    json={"name": self.name.strip()},
                    timeout=10.0
                )
                
                if response.status_code == 200:
                    data = response.json()
                    self.message = data.get("message", "저장되었습니다!")
                    self.show_message = True
                    self.name = ""
                else:
                    self.message = "저장 실패"
                    self.show_message = True
        except Exception as e:
            self.message = f"오류 발생: {str(e)}"
            self.show_message = True
        finally:
            self.is_loading = False

def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("🥕 Carrot", size="9"),
            rx.text("이름을 입력해주세요"),
            rx.input(
                placeholder="예: 홍길동",
                value=State.name,
                on_change=State.set_name,
                width="100%",
                is_disabled=State.is_loading,
            ),
            rx.button(
                "제출",
                on_click=State.handle_submit,
                width="100%",
                is_loading=State.is_loading,
            ),
            rx.cond(
                State.show_message,
                rx.box(
                    rx.text(State.message),
                    padding="4",
                    background_color="#d4edda",
                    border_radius="0.5rem",
                    color="#155724",
                ),
            ),
            spacing="4",
            align_items="center",
            width="100%",
            max_width="400px",
        ),
        center_content=True,
        padding="8",
    )

app = rx.App()
app.add_page(index)
