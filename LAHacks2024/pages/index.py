"""The home page of the app."""

from LAHacks2024 import styles
from LAHacks2024.templates import template
from .dashboard import FormState


import reflex as rx

# from uagents import Agent, Model

# class Message(Model):
#     text: str

class traveler_data(rx.State):  
    form_data = {},
    traveler_data = []
    flag: bool = False

    async def handle_submit(self, form_data: dict):
        self.traveler_data.append(form_data)
        print(form_data)
        print("traveler_data ", self.traveler_data)
        print("can access ", FormState.globally_avavilable_packages)

        available_pack = await self.get_state(FormState)
        print("can access ", available_pack.globally_avavilable_packages)

        return rx.window_alert("Data Submitted")

    def toggle_flag(self):
        self.flag = not self.flag

# class PackageState(rx.State):

#     response: str

#     async def test_msg(self):
#         print("inside test function")
#         test_travel = Agent(name='test_travel')
#         response = await test_travel._ctx.send('agent1qdwpw9vulfrejfncham3sc79tuek5s5n9nywcnazl5p53y37lgacxytcgrj',Message(text="Package was picked up."))

#         print(response)
#         self.response = str(response)
#         if self.response != "":
#             self.response = "Package was picked up."


@template(route="/", title="Add travel route")
def index(available_pack=None):

    return rx.vstack(
     rx.flex(
         rx.form(
            rx.vstack(
            rx.heading("Today's journey details", size="8"),
                     rx.vstack(
            rx.text("Source Address"),
            rx.input(
                placeholder="Enter source Address",
                name="pickup",
                width="15em"
            ),
            rx.text("Destination Address"),
            rx.input(
                placeholder="Enter destination Address",
                name="destination",
                width="15em"
            ),
            rx.button("Submit", type="submit", color_scheme="green",    ),
            paddingTop="2rem"
        ),
        ),
             on_submit=traveler_data.handle_submit,
             reset_on_submit=True,
    ),
        rx.divider(orientation="vertical", size="4"),
         rx.vstack(
         rx.heading("Available packages", size="8"),
        rx.vstack(
                rx.alert_dialog.root(
                        rx.alert_dialog.trigger(
                            rx.card(
                                rx.link(
                                    rx.flex(
                                        rx.avatar(src="/img_1.png"),
                                        rx.box(
                                            rx.heading("Onboarding documents"),
                                            rx.box(
                                                rx.text(
                                                    "Pickup from : CSUF"
                                                ),
                                                rx.text(
                                                    "Destination address : Denver"
                                                ),
                                                spacing="2",
                                                paddingTop="1em",
                                            ),
                                        ),
                                        spacing="2",
                                    ),
                                ),
                                as_child=True,
                                variant="classic",
                                width="30rem"
                            ),
                        ),
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("Select package"),
                        rx.alert_dialog.description(
                            "Are you sure? You want to deliver this package.",
                        ),
                        rx.flex(
                            rx.alert_dialog.cancel(
                                rx.button("Cancel", color_scheme="green",),
                            ),
                            rx.alert_dialog.action(
                                rx.button("Select Package", color_scheme="green",),
                            ),
                            spacing="3",
                            paddingTop="1em"
                        ),
                    ),
),
            rx.alert_dialog.root(
                rx.alert_dialog.trigger(
                    rx.card(
                        rx.link(
                            rx.flex(
                                rx.avatar(src="/img_1.png"),
                                rx.box(
                                    rx.heading("Plushtoy"),
                                    rx.box(
                                        rx.text(
                                            "Pickup from : San Diego"
                                        ),
                                        rx.text(
                                            "Destination address : Fullerton"
                                        ),
                                        spacing="2",
                                        paddingTop="1em",
                                    ),
                                ),
                                spacing="2",
                            ),
                        ),
                        as_child=True,
                        variant="ghost",
                        width="30rem"
                    ),
                ),
                rx.alert_dialog.content(
                    rx.alert_dialog.title("Select package"),
                    rx.alert_dialog.description(
                        "Are you sure? You want to deliver this package.",
                    ),
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button("Cancel", color_scheme="green", ),
                        ),
                        rx.alert_dialog.action(
                            rx.button("Select Package", color_scheme="green", ),
                        ),
                        spacing="3",
                        paddingTop="1em"
                    ),
                ),
            ),
            rx.alert_dialog.root(
                rx.alert_dialog.trigger(
                    rx.card(
                        rx.link(
                            rx.flex(
                                rx.avatar(src="/img_1.png"),
                                rx.box(
                                    rx.heading("Backpack"),
                                    rx.box(
                                        rx.text(
                                            "Pickup from : San Diego"
                                        ),
                                        rx.text(
                                            "Destination address : Irvine"
                                        ),
                                        spacing="2",
                                        paddingTop="1em",
                                    ),
                                ),
                                spacing="2",
                            ),
                        ),
                        as_child=True,
                        variant="classic",
                        width="30rem"
                    ),
                ),
                rx.alert_dialog.content(
                    rx.alert_dialog.title("Select package"),
                    rx.alert_dialog.description(
                        "Are you sure? You want to deliver this package.",
                    ),
                    rx.flex(
                        rx.alert_dialog.cancel(
                            rx.button("Cancel", color_scheme="green", ),
                        ),
                        rx.alert_dialog.action(
                            rx.button("Select Package", color_scheme="green", ),
                        ),
                        spacing="3",
                        paddingTop="1em"
                    ),
                ),
            ),

            paddingTop="2rem"
    ),
         ),
         spacing="9",
         width="100%",
         height="50vh",
    ),
    )