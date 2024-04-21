"""The dashboard page."""

from LAHacks2024.templates import template

import reflex as rx

class FormState(rx.State):
    form_data = {},
    globally_avavilable_packages: list[dict[str, str]] = []

    def handle_submit(self, form_data: dict):
        self.globally_avavilable_packages.append(form_data)
        print(form_data)
        print("globally_avavilable_packages ", self.globally_avavilable_packages)
        return rx.window_alert("Data Submitted!!!!")


@template(route="/dashboard", title="Add Package")
def dashboard():

    return rx.vstack(
        rx.form(
            rx.heading("Package Details", size="8"),
            rx.vstack(
                rx.text("Name"),
                rx.input(
                    placeholder="Enter package Name",
                    name="package_name",
                    width="15em"
                ),
                rx.text("Pickup Address"),
                rx.input(
                    placeholder="Enter pickup Address",
                    name="pickup",
                    width="15em"
                ),
                rx.text("Delivery Address"),
                rx.input(
                    placeholder="Enter destination Address",
                    name="destination",
                    width="15em"
                ),
                rx.button("Submit", type="submit"),
                paddingTop="2rem"
            ),

            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
    )

