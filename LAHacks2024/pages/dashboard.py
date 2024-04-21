"""The dashboard page."""

from LAHacks2024.templates import template

import reflex as rx

class FormState(rx.State):
    form_data = {}


    def handle_submit(self, form_data: dict):

        print(form_data)
        self.form_data = list(form_data.values())


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
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text("Package Added: " + FormState.form_data.to_string()),

    )