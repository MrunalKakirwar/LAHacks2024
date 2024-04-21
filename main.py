from uagents import Agent, Bureau, Context, Model, Protocol

from pydantic import Field
from ai_engine import UAgentResponse, UAgentResponseType
import random

owner = Agent(name="owner", seed="owneraniket1",port=8002, mailbox='f12bb3b3-1b10-4292-b9e0-67f7c9e34cce@https://agentverse.ai')
print(owner.address)

# class DiceRoll(Model):
#     num_rolls: int = Field(description="How much incentive you expect?")

class DiceRoll(Model):
    pkg: int = Field(description="How many packages you wish to deliver?")

class Message(Model):
    text: str

dice_roll_protocol = Protocol("Incentive")

@owner.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.text}")

@dice_roll_protocol.on_message(model=DiceRoll, replies={UAgentResponse})
async def roll_dice(ctx: Context, sender: str, msg: DiceRoll):
    result = ", ".join([str(random.randint(6, 10)) for _ in range(msg.pkg)])
    message = f"Expected Incentive: {result}"
    await ctx.send(
        sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
    )
owner.include(dice_roll_protocol, publish_manifest=True)

if __name__ == "__main__":
    owner.run()