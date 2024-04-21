"""The home page of the app."""

from LAHacks2024 import styles
from LAHacks2024.templates import template

import reflex as rx

from uagents import Agent, Model

class Message(Model):
    text: str


class PackageState(rx.State):

    response: str

    async def test_msg(self):
        print("inside test function")
        test_travel = Agent(name='test_travel')
        response = await test_travel._ctx.send('agent1qdwpw9vulfrejfncham3sc79tuek5s5n9nywcnazl5p53y37lgacxytcgrj',Message(text="Package was picked up."))

        print(response)
        self.response = str(response)
        if self.response != "":
            self.response = "Package was picked up."


@template(route="/", title="Add Travel route")
def index():
    return rx.vstack(
        rx.heading("Available packages", size="8"),
        rx.card(
            rx.link(
                rx.flex(
                    rx.avatar(src="/reflex_banner.png"),
                    rx.box(
                        rx.heading("Plush Toy"),
                        rx.text(
                            # PackageState.form_data[0]["pickup"] + " ---> " + PackageState.form_data[0]["destination"]
                            "Monday 22nd April \n"
                            "San Diego, CA  to CSU Fullerton, CA"
                        ),
                    ),
                    spacing="2",
                ),
                rx.flex(
                    rx.avatar(src="/reflex_banner.png"),
                    rx.box(
                        rx.heading("Small Table"),
                        rx.text(
                            "Tuesday 23rd April \n"
                            "San Diego, CA to Los Angeles Airport"
                        ),
                    ),
                    spacing="2",
                ),
            ),
            as_child=True,
        ),
        rx.button('Start Journey', type='submit', on_click=PackageState.test_msg),
        rx.text(PackageState.response),
        padding_left="250px",
    )
