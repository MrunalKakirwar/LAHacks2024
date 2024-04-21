
from uagents import Agent, Model




class Message(Model):
    text: str

import asyncio
async def test_msg():
        print("inside test function")
        test_travel = Agent(name='test_travel')
        # test_travel.include(service_protocol)
        response = await test_travel._ctx.send('agent1qdwpw9vulfrejfncham3sc79tuek5s5n9nywcnazl5p53y37lgacxytcgrj',Message(text="Hello, picked the package."))

        # sms = await test_travel._ctx.send(
        #     'agent1qdwpw9vulfrejfncham3sc79tuek5s5n9nywcnazl5p53y37lgacxytcgrj',
        #     Message(receiver="6575259745", msg="hello there aniket sms", type=MessageType.sms),
        # )


asyncio.run(test_msg())