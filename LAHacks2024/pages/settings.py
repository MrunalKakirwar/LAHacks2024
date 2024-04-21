"""The settings page."""

from LAHacks2024.templates import ThemeState, template
import creds
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

class WhatsappNotif(rx.State):
    
    def sending_update(self):
        from twilio.rest import Client

        account_sid = 'AC0bdab2d35e0b52a9da91e413294c42dc'
        auth_token = creds.auth_token
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Your Package was delivered!',
        to='whatsapp:+16575259745'
        )

        print(message.sid)


@template(route="/settings", title="Profile")
def settings() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("Package tracking", size="8"),
        rx.box(
            rx.card(
                rx.flex(
                    rx.flex(
                        rx.avatar(src="/img_1.png"),
                        rx.heading("Onboarding documents"),
                    ),
                    rx.box(
                        rx.text(
                            "Pickup from : CSUF"
                        ),
                        rx.text(
                            "Destination address : Denver"
                        ),
                        rx.flex(
                            rx.text("Status"),
                            rx.select(
                                ["Start Journey", "Package picked", "Delivered"],
                                placeholder="Select the status",
                            ),
                            spacing="4"
                        ),
                        rx.flex(
                            rx.button("Push notification",type='submit', on_click=PackageState.test_msg, color_scheme="yellow"),
                            
                            rx.button("Whatsapp notification update", color_scheme="green",on_click=WhatsappNotif.sending_update),
                            spacing="3",
                            paddingTop="1em",
                            justify="end"
                        ),
                        rx.text(
                            PackageState.response,
                            spacing="2",
                        ),
                        spacing="2",
                        paddingTop="1em",
                        paddingBottom="1em"
                    ),
                    spacing="2",
                ),
                as_child=True,
                variant="classic",
                width="30em"
            ),
            paddingTop="2em"
        ),
    )
