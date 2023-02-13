from discord import app_commands, Intents, Client, Interaction
 
 
class Bot(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
 
    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)
 
 
bot = Bot(intents=Intents.default())
 
@bot.event
async def on_ready():
    print(f"Conectado como: {bot.user}")
 
@bot.tree.command()
async def givemebadge(interaction: Interaction):
    await interaction.response.send_message("mensaje de prueba bot interaccion")
 
 
bot.run("MTA1MDU4MTAzNDIxNjk4NDY0Ng.GrJ15J.UWn26nQqil5AZHfua7mWYEY2XD17c7hDFKZyKs")