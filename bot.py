from db_campeoes import *
from cadastro_campeoes import *
from funcoes_consultas import *

import discord
import discord.ext
from discord import app_commands
 
import os
from dotenv import load_dotenv

load_dotenv()





TOKEN = os.getenv("DISCORD_TOKEN")

MY_GUILD = discord.Object(id=586669208214044673)


class MyClient(discord.Client):
    
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)



    

intents = discord.Intents.default()
bot = MyClient(intents=intents)


@bot.event
async def on_ready():
    print(f'Logado como: {bot.user} (ID: {bot.user.id})')
    print('Bot Online!')
    print('------')



class Regioes(discord.ui.View,):
    def __init__(self):
        super().__init__()
        self.value = None

    
    @discord.ui.button(label='Noxus', style=discord.ButtonStyle.grey)
    async def noxus(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r1=consulta_regiao("Noxus").lista
        await interaction.response.send_message("Os campeões de Noxus são:\n{}".format('\n'.join(c_r1)))
        button.disabled = True

    @discord.ui.button(label='Demacia', style=discord.ButtonStyle.grey)
    async def demacia(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r2=consulta_regiao("Demacia").lista
        await interaction.response.send_message("Os campeões de Demacia são:\n{}".format('\n'.join(c_r2)))
        button.disabled = True
        

    @discord.ui.button(label='Ixtal', style=discord.ButtonStyle.grey)
    async def ixtal(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r3=consulta_regiao("Ixtal").lista
        await interaction.response.send_message("Os campeões de Ixtal são:\n{}".format('\n'.join(c_r3)))
        button.disabled = True
        

    @discord.ui.button(label='Shurima', style=discord.ButtonStyle.grey)
    async def shurima(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r4=consulta_regiao("Shurima").lista
        await interaction.response.send_message("Os campeões de Shurima são:\n{}".format('\n'.join(c_r4)))
        button.disabled = True
        

    @discord.ui.button(label='Ionia', style=discord.ButtonStyle.grey)
    async def ionia(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r5=consulta_regiao("Ionia").lista
        await interaction.response.send_message("Os campeões de Ionia são:\n{}".format('\n'.join(c_r5)))
        button.disabled = True
        

    @discord.ui.button(label='Piltover', style=discord.ButtonStyle.grey)
    async def piltover(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r6=consulta_regiao("Piltover").lista
        await interaction.response.send_message("Os campeões de Piltover são:\n{}".format('\n'.join(c_r6)))
        button.disabled = True
        

    @discord.ui.button(label='Zaun', style=discord.ButtonStyle.grey)
    async def zaun(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r7=consulta_regiao("Zaun").lista
        await interaction.response.send_message("Os campeões de Zaun são:\n{}".format('\n'.join(c_r7)))
        button.disabled = True
        

    @discord.ui.button(label='Freljord', style=discord.ButtonStyle.grey)
    async def freljord(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r8=consulta_regiao("Freljord").lista
        await interaction.response.send_message("Os campeões de Freljord são:\n{}".format('\n'.join(c_r8)))
        button.disabled = True
        

    @discord.ui.button(label='Void', style=discord.ButtonStyle.grey)
    async def void(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r9=consulta_regiao("Void").lista
        await interaction.response.send_message("Os campeões do Void são:\n{}".format('\n'.join(c_r9)))
        button.disabled = True
        

    @discord.ui.button(label='Bilgewater', style=discord.ButtonStyle.grey)
    async def bilgewater(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r10=consulta_regiao("Bilgewater").lista
        await interaction.response.send_message("Os campeões de Bilgewater são:\n{}".format('\n'.join(c_r10)))
        button.disabled = True
        

    @discord.ui.button(label='Shadow Isles', style=discord.ButtonStyle.grey)
    async def shadow_isles(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r11=consulta_regiao("Shadow Isles").lista
        await interaction.response.send_message("Os campeões de Shadow Isles são:\n{}".format('\n'.join(c_r11)))
        button.disabled = True
        

    @discord.ui.button(label='Mount Targon', style=discord.ButtonStyle.grey)
    async def mount_targon(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r12=consulta_regiao("Mount Targon").lista
        await interaction.response.send_message("Os campeões do Mount Targon são:\n{}".format('\n'.join(c_r12)))
        button.disabled = True
        

    @discord.ui.button(label='Bandle City', style=discord.ButtonStyle.grey)
    async def bandle_city(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_regiao.lista = []
        c_r13=consulta_regiao("Bandle City").lista
        await interaction.response.send_message("Os campeões de Bandle City são:\n{}".format('\n'.join(c_r13)))
        button.disabled = True
        
    

class Funcoes(discord.ui.View,):
    def __init__(self):
        super().__init__()
        self.value = None

    
    @discord.ui.button(label='ULTIMATE JÁ DIZ TUDO', style=discord.ButtonStyle.grey)
    async def ultimate(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f1=consulta_funcao("ULTIMATE JÁ DIZ TUDO").lista
        await interaction.response.send_message("Os campeões com Ultimate em área são:\n{}".format('\n'.join(c_f1)))
        button.disabled = True
    
    @discord.ui.button(label='CADÊ ELES?!', style=discord.ButtonStyle.grey)
    async def cade(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f2=consulta_funcao("CADÊ ELES?!").lista
        await interaction.response.send_message("Os campeões com invisibildade são:\n{}".format('\n'.join(c_f2)))
        button.disabled = True
    
    @discord.ui.button(label='É UMA ARMADILHA', style=discord.ButtonStyle.grey)
    async def armadilha(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f3=consulta_funcao("É UMA ARMADILHA").lista
        await interaction.response.send_message("Os campeões que colocam armadilha são:\n{}".format('\n'.join(c_f3)))
        button.disabled = True

    @discord.ui.button(label='ELES... NUNCA... MORREM!', style=discord.ButtonStyle.grey)
    async def nunca_morrem(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f4=consulta_funcao("ELES... NUNCA... MORREM!").lista
        await interaction.response.send_message("Os campeões com habilidades de ressurreição, imunidade ou zumbi são:\n{}".format('\n'.join(c_f4)))
        button.disabled = True
    
    @discord.ui.button(label='EQUIPE PROTETORA', style=discord.ButtonStyle.grey)
    async def protetora(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f5=consulta_funcao("EQUIPE PROTETORA").lista
        await interaction.response.send_message("Os campeões com habilidades de escudo ou cura são:\n{}".format('\n'.join(c_f5)))
        button.disabled = True

    @discord.ui.button(label='ESTAMOS BEM AQUI', style=discord.ButtonStyle.grey)
    async def bem_aqui(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f6=consulta_funcao("ESTAMOS BEM AQUI").lista
        await interaction.response.send_message("Os campeões com habilidades de poke são:\n{}".format('\n'.join(c_f6)))
        button.disabled = True

    @discord.ui.button(label='INVOCADORES NO RIFT', style=discord.ButtonStyle.grey)
    async def invocadores(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f7=consulta_funcao("INVOCADORES NO RIFT").lista
        await interaction.response.send_message("Os campeões com habilidades de invocação ou mascote são:\n{}".format('\n'.join(c_f7)))
        button.disabled = True
    
    @discord.ui.button(label='NÃO SE MEXE!', style=discord.ButtonStyle.grey)
    async def nao_mexe(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f8=consulta_funcao("NÃO SE MEXE!").lista
        await interaction.response.send_message("Os campeões com 2 ou mais habilidades imobilizadoras são:\n{}".format('\n'.join(c_f8)))
        button.disabled = True
    
    @discord.ui.button(label='SEM ESCONDERIJO', style=discord.ButtonStyle.grey)
    async def sem_esconderijo(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f9=consulta_funcao("SEM ESCONDERIJO").lista
        await interaction.response.send_message("Os campeões com habilidades globais são:\n{}".format('\n'.join(c_f9)))
        button.disabled = True
    
    @discord.ui.button(label='TÔ AJUDANDO', style=discord.ButtonStyle.grey)
    async def ajudando(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f10=consulta_funcao("TÔ AJUDANDO").lista
        await interaction.response.send_message("Os campeões com habilidades de criação de terreno são:\n{}".format('\n'.join(c_f10)))
        button.disabled = True
    
    @discord.ui.button(label='VEM CÁ', style=discord.ButtonStyle.grey)
    async def vem(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_funcao.lista = []
        c_f11=consulta_funcao("VEM CÁ").lista
        await interaction.response.send_message("Os campeões com habilidades de efeito de deslocamento são:\n{}".format('\n'.join(c_f11)))
        button.disabled = True
        

class Classes(discord.ui.View,):
    def __init__(self):
        super().__init__()
        self.value = None

    
    @discord.ui.button(label='Assassino', style=discord.ButtonStyle.grey)
    async def assassino(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_classe.lista = []
        c_c1=consulta_classe("Assassino").lista
        await interaction.response.send_message("Os campeões com a classe Assassino são:\n{}".format('\n'.join(c_c1)))
        button.disabled = True

    @discord.ui.button(label='Atirador', style=discord.ButtonStyle.grey)
    async def atirador(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_classe.lista = []
        c_c2=consulta_classe("Atirador").lista
        await interaction.response.send_message("Os campeões com a classe Atirador são:\n{}".format('\n'.join(c_c2)))
        button.disabled = True
    
    @discord.ui.button(label='Lutador', style=discord.ButtonStyle.grey)
    async def lutador(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_classe.lista = []
        c_c3=consulta_classe("Lutador").lista
        await interaction.response.send_message("Os campeões com a classe Lutador são:\n{}".format('\n'.join(c_c3)))
        button.disabled = True
    
    @discord.ui.button(label='Mago', style=discord.ButtonStyle.grey)
    async def mago(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_classe.lista = []
        c_c4=consulta_classe("Mago").lista
        await interaction.response.send_message("Os campeões com a classe Mago são:\n{}".format('\n'.join(c_c4)))
        button.disabled = True

    @discord.ui.button(label='Suporte', style=discord.ButtonStyle.grey)
    async def suporte(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_classe.lista = []
        c_c5=consulta_classe("Suporte").lista
        await interaction.response.send_message("Os campeões com a classe Suporte são:\n{}".format('\n'.join(c_c5)))
        button.disabled = True

    @discord.ui.button(label='Tank', style=discord.ButtonStyle.grey)
    async def tank(self, interaction: discord.Interaction, button: discord.ui.Button):
        consulta_classe.lista = []
        c_c6=consulta_classe("Tank").lista
        await interaction.response.send_message("Os campeões com a classe Tank são:\n{}".format('\n'.join(c_c6)))
        button.disabled = True
            
    
class Opcoes(discord.ui.Select):
    def __init__(self):

        
        options = [
            discord.SelectOption(label='Regiões', description='Desafios Por Região'),
            discord.SelectOption(label='Funções', description='Desafios Por Funções'),
            discord.SelectOption(label='Classes', description='Desafios Por Classes'),
        ]

        
        super().__init__(placeholder='Escolha uma Opção de Desafios', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        
        if self.values[0] == 'Regiões':
            mostrar = Regioes()
        if self.values[0] == 'Funções':
            mostrar = Funcoes()
        if self.values[0] == 'Classes':
            mostrar = Classes()
        await interaction.response.send_message(f'Sua Opção de desafios foi: {self.values[0]}',view=mostrar)
        


class OpcoesView(discord.ui.View):
    def __init__(self):
        super().__init__()

        
        self.add_item(Opcoes())   

@bot.tree.command()
async def menu(interaction: discord.Interaction):
    """Manda uma Mensagem com os desafios escolhidos"""

    
    view = OpcoesView()

    
    await interaction.response.send_message('Escolha uma Opção de Desafios:', view=view)








bot.run(TOKEN)


