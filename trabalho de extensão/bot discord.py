Bot de FAQ automatico para servidor de Discord.
Responde automaticamente a perguntas frequentes da turma/comunidade.

Como usar:
1. Cole seu token do Discord na variavel TOKEN abaixo.
2. Edite as respostas dos comandos com as informacoes reais.
3. Rode: python bot_discord.py

import discord
from discord.ext import commands

TOKEN = "COLE_SEU_TOKEN_AQUI"

# Configuracao basica do bot
intents = discord.Intents.default()
intents.message_content = True  # necessario para o bot ler mensagens

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


# ============================================
# COMANDOS - edite os textos abaixo como quiser
# ============================================

@bot.command(name="ajuda")
async def ajuda(ctx):
    """Mostra todos os comandos disponiveis"""
    mensagem = (
        "**Comandos disponiveis:**\n"
        "`!regras` - regras do servidor\n"
        "`!links` - links do servidor\n"
        "`!duvidas` - guardar duvidas para resposta da moderação\n"
        "`!contato` - contato de suporte/duvidas\n"
    )
    await ctx.send(mensagem)


@bot.command(name="prazo")
async def regras(ctx):
    """Informa todas as regras do servidor"""
    await ctx.send("a primeira e unica regra é ser moderado no linguajar.")


@bot.command(name="links")
async def links(ctx):
    """Informa todos os links ligados ao servidor"""
    await ctx.send("Link do servidor: https://exemplo-da-sua-plataforma.com")


@bot.command(name="duvidas")
async def duvidas(ctx):
    """Lista todas as duvidas registradas"""
    try:
        with open("duvidas.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
    except FileNotFoundError:
        conteudo = ""
 
    if not conteudo:
        await ctx.send("Nenhuma duvida registrada ainda.")
        return
 
    mensagem = "**Duvidas registradas:**\n" + conteudo
    await ctx.send(mensagem)

@bot.command(name="contato")
async def contato(ctx):
    """Informa contato para duvidas"""
    await ctx.send("Para duvidas, envie um e-mail para: contato@exemplo.com")


# ============================================
# Inicia o bot
# ============================================
bot.run(TOKEN)
