import discord
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime, timedelta, timezone
import asyncio
import itertools
import json
import os
from discord.ui import View, Select, Button
from discord import ButtonStyle
from discord import ui

TOKEN = "bot_token_here"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="B!", intents=intents)

status_cycle = itertools.cycle([
    discord.Game("Made by 1Vortexx"),
    discord.Game("brickmasterbot.xyz")
])

import datetime
import discord
from discord.ext import commands

OWNER_ID = 1049015164709646427

bot_start_time = datetime.datetime.utcnow()
last_guild_join_time = None

@bot.event
async def on_guild_join(guild):
    global last_guild_join_time
    last_guild_join_time = datetime.datetime.utcnow()

@bot.command()
async def botstats(ctx):
    if ctx.author.id != OWNER_ID:
        return await ctx.send("❌ You do not have permission to use this command.")

    total_guilds = len(bot.guilds)
    total_members = sum(guild.member_count for guild in bot.guilds)
    latency_ms = round(bot.latency * 1000)

    if last_guild_join_time:
        last_join_str = last_guild_join_time.strftime("%Y-%m-%d %H:%M:%S UTC")
    else:
        last_join_str = "No record of last join yet."

    uptime_delta = datetime.datetime.utcnow() - bot_start_time
    uptime_str = str(uptime_delta).split('.')[0]

    embed = discord.Embed(title="🤖 Bot Statistics", color=discord.Color.blue())
    embed.add_field(name="Servers", value=str(total_guilds), inline=True)
    embed.add_field(name="Total Users", value=str(total_members), inline=True)
    embed.add_field(name="Latency", value=f"{latency_ms} ms", inline=True)
    embed.add_field(name="Uptime", value=uptime_str, inline=False)
    embed.add_field(name="Last Server Joined", value=last_join_str, inline=False)

    try:
        await ctx.author.send(embed=embed)
        await ctx.message.add_reaction("✅")
    except discord.Forbidden:
        await ctx.send("❌ I couldn't DM you. Please check your privacy settings.")

@tasks.loop(seconds=30)
async def rotate_status():
    await bot.change_presence(activity=next(status_cycle))

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not rotate_status.is_running():
        rotate_status.start()

ticket_sessions = {}
setup_data_path = r"/Users/local/ VSCode Projects (DO NOT TOUCH)/DevSolutions Client Bots/Oklahoma RP/setup.json"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not rotate_status.is_running():
        rotate_status.start()



@bot.command()
async def cmd_support(ctx):
    embed = discord.Embed(
        title="📘 Bot Commands Help",
        description="Here's a list of available commands:",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="`!setup`",
        value="Configure all bot settings.\nWho can use: Server Owner & Admins",
        inline=False
    )
    embed.add_field(
        name="`!reconfigure`",
        value="Update a specific setting from setup.\nWho can use: Server Owner & Admins",
        inline=False
    )
    embed.add_field(
        name="`!viewsetup`",
        value="View current bot configuration.\nWho can use: Anyone",
        inline=False
    )
    embed.add_field(
        name="`!resetsetup`",
        value="Reset all setup configuration.\nWho can use: Server Owner only",
        inline=False
    )
    embed.add_field(
        name="`!ssuvote`",
        value="Start a vote to launch a session.\nWho can use: Session Management only",
        inline=False
    )
    embed.add_field(
        name="`!ssu`",
        value="Announce a session startup.\nWho can use: Session Management only",
        inline=False
    )
    embed.add_field(
        name="`!ssd`",
        value="Announce a session shutdown.\nWho can use: Session Management only",
        inline=False
    )
    embed.add_field(
        name="~`!ticket [reason]`~",
        value="~Open a new ticket with an optional reason.~\nWho can use: Anyone",
        inline=False
    )
    embed.add_field(
        name="`!close`",
        value="Close your current ticket.\nWho can use: Anyone (ticket owner or with manage channels)",
        inline=False
    )
    embed.add_field(
        name="`!session`",
        value="Check your active ticket channel.\nWho can use: Anyone",
        inline=False
    )
    embed.add_field(
        name="`!kick @user [reason]`",
        value="Kick a member.\nWho can use: Members with kick permissions",
        inline=False
    )
    embed.add_field(
        name="`!ban @user [reason]`",
        value="Ban a member.\nWho can use: Members with ban permissions",
        inline=False
    )

    await ctx.send(embed=embed)


@bot.command()
async def cmds(ctx):
    embed = discord.Embed(
        title="📃 Command List",
        description="List of bot commands, what they do, and who can use them.",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="`!setup`",
        value="Configure all bot settings.\nWho can use: Server Owner & Admins",
        inline=False
    )
    embed.add_field(
        name="`!reconfigure`",
        value="Update a specific setting from setup.\nWho can use: Server Owner & Admins",
        inline=False
    )
    embed.add_field(
        name="`!viewsetup`",
        value="View current bot configuration.\nWho can use: Anyone",
        inline=False
    )
    embed.add_field(
        name="`!resetsetup`",
        value="Reset all setup configuration.\nWho can use: Server Owner only",
        inline=False
    )
    embed.add_field(
        name="`!ssuvote`",
        value="Start a vote to launch a session.\nWho can use: Session Management only",
        inline=False
    )
    embed.add_field(
        name="`!ssu`",
        value="Announce a session startup.\nWho can use: Session Management only",
        inline=False
    )
    embed.add_field(
        name="`!ssd`",
        value="Announce a session shutdown.\nWho can use: Session Management only",
        inline=False
    )
    embed.add_field(
        name="~`!ticket [reason]`~",
        value="~Open a new ticket with an optional reason.~\nWho can use: Anyone",
        inline=False
    )
    embed.add_field(
        name="`!close`",
        value="Close your current ticket.\nWho can use: Anyone (ticket owner or with manage channels)",
        inline=False
    )
    embed.add_field(
        name="`!session`",
        value="Check your active ticket channel.\nWho can use: Anyone",
        inline=False
    )
    embed.add_field(
        name="`!kick @user [reason]`",
        value="Kick a member.\nWho can use: Members with kick permissions",
        inline=False
    )
    embed.add_field(
        name="`!ban @user [reason]`",
        value="Ban a member.\nWho can use: Members with ban permissions",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command()
async def ticket(ctx, *, reason="No reason provided"):
    category = get(ctx.guild.categories, name="Tickets")
    if not category:
        category = await ctx.guild.create_category("Tickets")

    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
    }

    channel = await ctx.guild.create_text_channel(
        f"ticket-{ctx.author.name}", overwrites=overwrites, category=category
    )
    await channel.send(f"🎫 Ticket created by {ctx.author.mention}.\n**Reason:** {reason}")
    
    ticket_sessions[ctx.author.id] = {
        "channel_id": channel.id,
        "timestamp": datetime.now(timezone.utc)
    }


@bot.command()
async def close(ctx):
    author_id = ctx.author.id
    session = ticket_sessions.get(author_id)

    if ctx.channel.category and "ticket" in ctx.channel.name:
        if session and ctx.channel.id == session["channel_id"] or ctx.author.guild_permissions.manage_channels:
            await ctx.send("🗑️ Closing ticket in 5 seconds...")
            await asyncio.sleep(5)
            await ctx.channel.delete()
            ticket_sessions.pop(author_id, None)
        else:
            await ctx.send("❌ You can't close someone else's ticket.")
    else:
        await ctx.send("❌ This doesn't look like a ticket channel.")


@bot.command()
async def session(ctx):
    session = ticket_sessions.get(ctx.author.id)
    if session:
        channel = bot.get_channel(session["channel_id"])
        if channel:
            await ctx.send(f"📍 Your ticket is in <#{channel.id}>.")
        else:
            await ctx.send("⚠️ Your ticket session exists but I can't find the channel.")
    else:
        await ctx.send("❌ No active ticket session found.")


async def log_action(ctx, action, member, reason):
    modlog = get(ctx.guild.text_channels, name="mod-log")
    if modlog:
        em = discord.Embed(title=f"{action}", color=discord.Color.red())
        em.add_field(name="Target", value=str(member), inline=True)
        em.add_field(name="Moderator", value=str(ctx.author), inline=True)
        em.add_field(name="Reason", value=reason or "No reason", inline=False)
        await modlog.send(embed=em)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"👢 {member} was kicked.")
    await log_action(ctx, "Kick", member, reason)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 {member} was banned.")
    await log_action(ctx, "Ban", member, reason)

@tasks.loop(minutes=5)
async def session_cleanup():
    now = datetime.now(timezone.utc)
    expired_users = [uid for uid, data in ticket_sessions.items()
                     if (now - data["timestamp"]).total_seconds() > 3600]
    for uid in expired_users:
        ticket_sessions.pop(uid)


class PaginatedRoleSelectView(View):
    def __init__(self, roles, placeholder, timeout=180, allow_skip=False, allow_use_same=False, management_roles=None):
        super().__init__(timeout=timeout)
        self.roles = roles
        self.placeholder = placeholder
        self.page = 0
        self.selected_role_id = None
        self.max_per_page = 25
        self.stopped_early = False
        self.use_same_as_management = False
        self.management_roles = management_roles or []

        self.select = Select(placeholder=self.placeholder, options=[])
        self.select.callback = self.select_callback
        self.add_item(self.select)

        self.prev_button = Button(label="Previous", style=ButtonStyle.secondary)
        self.prev_button.callback = self.prev_page
        self.add_item(self.prev_button)

        self.next_button = Button(label="Next", style=ButtonStyle.secondary)
        self.next_button.callback = self.next_page
        self.add_item(self.next_button)

        if allow_skip:
            self.skip_button = Button(label="Skip", style=ButtonStyle.danger)
            self.skip_button.callback = self.skip_callback
            self.add_item(self.skip_button)
        else:
            self.skip_button = None

        if allow_use_same:
            self.use_same_button = Button(label="Use Same as Management Role", style=ButtonStyle.success)
            self.use_same_button.callback = self.use_same_callback
            self.add_item(self.use_same_button)
        else:
            self.use_same_button = None

        self.update_options()

    def update_options(self):
        start = self.page * self.max_per_page
        end = start + self.max_per_page
        page_roles = self.roles[start:end]
        self.select.options = [
            discord.SelectOption(label=role.name, value=str(role.id))
            for role in page_roles
        ]
        self.select.placeholder = f"{self.placeholder} (Page {self.page+1}/{(len(self.roles)-1)//self.max_per_page + 1})"

        self.prev_button.disabled = self.page == 0
        self.next_button.disabled = end >= len(self.roles)

    async def select_callback(self, interaction: discord.Interaction):
        self.selected_role_id = int(self.select.values[0])
        self.disable_all()
        await interaction.response.edit_message(view=self)
        self.stop()

    async def prev_page(self, interaction: discord.Interaction):
        if self.page > 0:
            self.page -= 1
            self.update_options()
            await interaction.response.edit_message(view=self)

    async def next_page(self, interaction: discord.Interaction):
        if (self.page + 1) * self.max_per_page < len(self.roles):
            self.page += 1
            self.update_options()
            await interaction.response.edit_message(view=self)

    async def skip_callback(self, interaction: discord.Interaction):
        self.stopped_early = True
        self.selected_role_id = None
        self.disable_all()
        await interaction.response.edit_message(content="⏭️ Selection skipped.", view=self)
        self.stop()

    async def use_same_callback(self, interaction: discord.Interaction):
        self.use_same_as_management = True
        self.stopped_early = True
        self.disable_all()
        await interaction.response.edit_message(content="✅ Using same role(s) as management role.", view=self)
        self.stop()

    def disable_all(self):
        self.select.disabled = True
        self.prev_button.disabled = True
        self.next_button.disabled = True
        if self.skip_button:
            self.skip_button.disabled = True
        if self.use_same_button:
            self.use_same_button.disabled = True

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx, reconfig_target: str = None):
    if ctx.author.id != ctx.guild.owner_id and not ctx.author.guild_permissions.administrator:
        return await ctx.send(embed=discord.Embed(
            description="❌ You do not have permission to run this command.",
            color=discord.Color.red()))

    all_configs = {}
    if os.path.exists(setup_data_path):
        try:
            with open(setup_data_path, "r") as f:
                all_configs = json.load(f)
        except json.JSONDecodeError:
            all_configs = {}

    guild_id_str = str(ctx.guild.id)
    existing_config = all_configs.get(guild_id_str, {})


    if reconfig_target is None and existing_config:
        await ctx.send(embed=discord.Embed(
            description="✅ Existing configuration found for this server. Auto-applied.",
            color=discord.Color.green()))
        return

    management_roles_ids = existing_config.get("management_roles", [])
    user_roles_ids = [r.id for r in ctx.author.roles]

 
    can_change_management = (ctx.author.id == ctx.guild.owner_id or
                             not any(rid in management_roles_ids for rid in user_roles_ids))

    def role_description_embed(title: str, description: str):
        return discord.Embed(title=title, description=description, color=discord.Color.blue())

    guild_roles = [r for r in ctx.guild.roles if r != ctx.guild.default_role]

  
    setup_config = existing_config.copy()

   
    if reconfig_target is None or reconfig_target == "management_roles":
        if can_change_management:
            embed = role_description_embed(
                "Management Role Setup",
                "This role has full management permissions over the bot setup and configuration.\n"
                "Select **one** role from the dropdown below to be the management role.\n" \
                "Please drag or add Oklahoma Managemnet to the ***TOP*** of the role list to view all roles."
            )
            view = PaginatedRoleSelectView(
                guild_roles,
                placeholder="Select Management Role",
                allow_skip=bool(existing_config.get("management_roles"))
            )
            msg = await ctx.send(embed=embed, view=view)
            await view.wait()
            if view.selected_role_id is None and not view.stopped_early:
                return await ctx.send(embed=discord.Embed(
                    description="⚠️ Setup timed out or no role selected. Aborting.",
                    color=discord.Color.red()))
            elif view.stopped_early:
                
                pass
            else:
                setup_config["management_roles"] = [view.selected_role_id]
        else:
            await ctx.send(embed=discord.Embed(
                description="ℹ️ You do not have permission to change the management role. Skipping that step.",
                color=discord.Color.gold()))

    
    if reconfig_target is None or reconfig_target == "session_roles":
        session_roles = []
        embed = role_description_embed(
            "Session Management Roles Setup",
            "These roles can manage active sessions such as closing tickets and managing session channels.\n"
            "You must select a role, or use the same role as management."
        )
        for i in range(2):
            view = PaginatedRoleSelectView(
                guild_roles,
                placeholder=f"Select Session Management Role #{i+1}",
                allow_skip=bool(existing_config.get("session_roles")),
                allow_use_same=True,
                management_roles=setup_config.get("management_roles", [])
            )
            msg = await ctx.send(embed=embed, view=view)
            await view.wait()
            if view.use_same_as_management:
                session_roles.extend(setup_config.get("management_roles", []))
                break
            elif view.selected_role_id is not None:
                session_roles.append(view.selected_role_id)
            elif view.selected_role_id is None and view.stopped_early:
            
                pass
            else:
                return await ctx.send(embed=discord.Embed(
                    description="⚠️ Setup timed out or no role selected. Aborting.",
                    color=discord.Color.red()))
        setup_config["session_roles"] = session_roles


    if reconfig_target is None or reconfig_target == "session_ping_roles":
        session_ping_roles = []
        embed = role_description_embed(
            "Session Ping Roles Setup",
            "These roles will receive pings for session updates.\n"
            "The first selection is required. You may skip the rest."
        )
        for i in range(3):
            view = PaginatedRoleSelectView(
                guild_roles,
                placeholder=f"Select Session Ping Role #{i+1}",
                allow_skip=(i != 0 or bool(existing_config.get("session_ping_roles"))),
                allow_use_same=False
            )
            msg = await ctx.send(embed=embed, view=view)
            await view.wait()
            if view.selected_role_id is None and not view.stopped_early:
                return await ctx.send(embed=discord.Embed(
                    description="⚠️ Setup timed out or no role selected. Aborting.",
                    color=discord.Color.red()))
            elif view.stopped_early:
              
                session_ping_roles.append(None)
            elif view.selected_role_id is not None:
                session_ping_roles.append(view.selected_role_id)
        setup_config["session_ping_roles"] = session_ping_roles

    
    if reconfig_target is None or reconfig_target == "command_runner_role":
        embed = role_description_embed(
            "Command Runner Role Setup",
            "This role has permissions to run bot commands.\n"
            "Select **one** role from the dropdown below or skip."
        )
        view = PaginatedRoleSelectView(
            guild_roles,
            placeholder="Select Command Runner Role",
            allow_skip=bool(existing_config.get("command_runner_role")),
            allow_use_same=False
        )
        msg = await ctx.send(embed=embed, view=view)
        await view.wait()
        if view.selected_role_id is None and not view.stopped_early:
            return await ctx.send(embed=discord.Embed(
                description="⚠️ Setup timed out or no role selected. Aborting.",
                color=discord.Color.red()))
        elif view.stopped_early:
            
            pass
        else:
            setup_config["command_runner_role"] = view.selected_role_id

   
    if reconfig_target is None or reconfig_target == "steam_friend_code":
        current_friend_code = setup_config.get("steam_friend_code", "Not set")
        embed = role_description_embed(
            "Steam Friend Code",
            f"Current value: `{current_friend_code}`\nPlease enter the Steam friend code of the server host.\nExample: `123456789`"
        )
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await bot.wait_for("message", check=check, timeout=60)
            new_val = msg.content.strip()
            if new_val != current_friend_code:
                setup_config["steam_friend_code"] = new_val
        except asyncio.TimeoutError:
            return await ctx.send(embed=discord.Embed(
                description="⚠️ Timeout: no code entered. Aborting setup.",
                color=discord.Color.red()))

    
    if reconfig_target is None or reconfig_target == "server_name":
        current_name = setup_config.get("server_name", "Not set")
        embed = role_description_embed(
            "Server Name",
            f"Current value: `{current_name}`\nPlease enter the name of your RP server.\nExample: `Oklahoma RP`"
        )
        await ctx.send(embed=embed)

        try:
            msg = await bot.wait_for("message", check=check, timeout=60)
            new_val = msg.content.strip()
            if new_val != current_name:
                setup_config["server_name"] = new_val
        except asyncio.TimeoutError:
            return await ctx.send(embed=discord.Embed(
                description="⚠️ Timeout: no name entered. Aborting setup.",
                color=discord.Color.red()))

   
    if reconfig_target is None or reconfig_target == "server_owner":
        current_owner = setup_config.get("server_owner", "Not set")
        embed = role_description_embed(
            "Server Owner",
            f"Current value: `{current_owner}`\nPlease enter the name of the server owner or primary founder.\nExample: `VrtxsVoid`"
        )
        await ctx.send(embed=embed)

        try:
            msg = await bot.wait_for("message", check=check, timeout=60)
            new_val = msg.content.strip()
            if new_val != current_owner:
                setup_config["server_owner"] = new_val
        except asyncio.TimeoutError:
            return await ctx.send(embed=discord.Embed(
                description="⚠️ Timeout: no owner name entered. Aborting setup.",
                color=discord.Color.red()))

    
    if reconfig_target is None or reconfig_target == "session_vote_threshold":
        embed = role_description_embed(
            "Session Vote Threshold Setup",
            "Enter the number of ✅ votes required to start a session."
        )
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg = await bot.wait_for("message", check=check, timeout=60)
            vote_count = int(msg.content)
            setup_config["session_vote_threshold"] = vote_count
        except (asyncio.TimeoutError, ValueError):
            return await ctx.send(embed=discord.Embed(
                description="⚠️ Invalid input or timeout. Aborting setup.",
                color=discord.Color.red()))

    
    all_configs[guild_id_str] = setup_config
    with open(setup_data_path, "w") as f:
        json.dump(all_configs, f, indent=4)

    await ctx.send(embed=discord.Embed(
        description="✅ Setup complete. Configuration saved.",
        color=discord.Color.green()))



@bot.command()
async def viewsetup(ctx):
    if not os.path.exists(setup_data_path):
        return await ctx.send("⚠️ No setup configuration found.")

    try:
        with open(setup_data_path, "r") as f:
            all_configs = json.load(f)
    except json.JSONDecodeError:
        return await ctx.send("⚠️ Setup file is empty or corrupted. Please run the setup command again.")

    guild_id_str = str(ctx.guild.id)
    config = all_configs.get(guild_id_str)
    if not config:
        return await ctx.send("⚠️ No configuration found for this server.")

    em = discord.Embed(title="📄 Current Setup Configuration", color=discord.Color.blue())
    role_sections = {
        "Management Roles": config.get("management_roles", []),
        "Session Roles": config.get("session_roles", []),
        "Bot Roles": config.get("bot_roles", []),
        "Moderation Roles": config.get("mod_roles", []),
        "Session Ping Roles": config.get("session_ping_roles", [])
    }

    for section, ids in role_sections.items():
        roles = [f"<@&{rid}>" for rid in ids if rid is not None]
        em.add_field(name=section, value=", ".join(roles) if roles else "None set", inline=False)

    
    cmd_runner_id = config.get("command_runner_role")
    if cmd_runner_id:
        em.add_field(name="Command Runner Role", value=f"<@&{cmd_runner_id}>", inline=False)
    else:
        em.add_field(name="Command Runner Role", value="None set", inline=False)

    await ctx.send(embed=em)


@bot.command()
async def resetsetup(ctx):
    if ctx.author.id != ctx.guild.owner_id:
        return await ctx.send("❌ Only the server owner can reset the setup.")

    guild_id_str = str(ctx.guild.id)
    if os.path.exists(setup_data_path):
        try:
            with open(setup_data_path, "r") as f:
                all_configs = json.load(f)
        except json.JSONDecodeError:
            all_configs = {}
        if guild_id_str in all_configs:
            all_configs.pop(guild_id_str)
            with open(setup_data_path, "w") as f:
                json.dump(all_configs, f, indent=4)
            await ctx.send("🗑️ Setup configuration for this server has been reset.")
        else:
            await ctx.send("⚠️ No setup configuration exists for this server.")
    else:
        await ctx.send("⚠️ No setup file exists to delete.")



from discord.ui import Select, View

@bot.command()
@commands.has_permissions(administrator=True)
async def reconfigure(ctx):
    if not os.path.exists(setup_data_path):
        return await ctx.send("⚠️ Setup not completed yet.")

    options = [
        discord.SelectOption(label="Management Role", value="management_roles"),
        discord.SelectOption(label="Session Management Roles", value="session_roles"),
        discord.SelectOption(label="Session Ping Roles", value="session_ping_roles"),
        discord.SelectOption(label="Bot Manager Roles", value="bot_roles"),
        discord.SelectOption(label="Moderation Roles", value="mod_roles"),
        discord.SelectOption(label="Command Runner Role", value="command_runner_role"),
        discord.SelectOption(label="Session Vote Threshold", value="session_vote_threshold"),
    ]

    class ConfigSelectView(View):
        def __init__(self):
            super().__init__(timeout=60)
            self.select = Select(placeholder="Select a config to update", options=options)
            self.select.callback = self.select_callback
            self.add_item(self.select)

        async def select_callback(self, interaction: discord.Interaction):
            await interaction.response.send_message(
                f"🔧 Reconfiguring **{self.select.values[0]}**...",
                ephemeral=True
            )
            await ctx.invoke(bot.get_command("setup"), reconfig_target=self.select.values[0])
            self.stop()

    embed = discord.Embed(
        title="⚙️ Reconfigure Bot Settings",
        description="Select a setting below to reconfigure.",
        color=discord.Color.orange()
    )
    await ctx.send(embed=embed, view=ConfigSelectView())


def is_role_allowed(ctx, role_key):
    if not os.path.exists(setup_data_path):
        return False
    with open(setup_data_path, "r") as f:
        all_configs = json.load(f)
    guild_id_str = str(ctx.guild.id)
    config = all_configs.get(guild_id_str, {})
    role_ids = config.get(role_key, [])
    return any(role.id in role_ids for role in ctx.author.roles)

@bot.command()
async def ssu(ctx):
    if not os.path.exists(setup_data_path):
        return await ctx.send("⚠️ Setup has not been completed yet.")

    with open(setup_data_path, "r") as f:
        all_configs = json.load(f)
    guild_id_str = str(ctx.guild.id)
    config = all_configs.get(guild_id_str, {})

    session_roles = config.get("session_roles", [])
    author_role_ids = [role.id for role in ctx.author.roles]

    if not any(rid in session_roles for rid in author_role_ids):
        return await ctx.send("❌ You do not have permission to run this command.")

    session_ping_roles = config.get("session_ping_roles", [])
    server_name = config.get("server_name", "Unknown Server")
    server_owner = config.get("server_owner", "Unknown Owner")
    friend_code = config.get("steam_friend_code", None)

    if not friend_code:
        return await ctx.send("⚠️ Steam friend code not set in setup.")

    ping_mentions = [f"<@&{rid}>" for rid in session_ping_roles if rid]

    embed = discord.Embed(
        title="Session Startup!",
        description=(
            f"{server_name} Management Team is Hosting a Session! Come join us for some quality-roleplay and fun! "
            "Voting and not joining will result in moderation action!\n\n"
            f"**Server Name:** {server_name}\n"
            f"**Server Owner:** {server_owner}\n"
            f"**Steam Friend Code:** `{friend_code}`"
        ),
        color=discord.Color.blue()
    )
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)

    embed.set_image(url="https://i.imgur.com/8ihBaYM.png")

    embed.set_footer(text="Made by 1Vortexx")

    await ctx.send(content=" ".join(ping_mentions), embed=embed)

@bot.command()
async def ssuvote(ctx):
    if not os.path.exists(setup_data_path):
        return await ctx.send("⚠️ Setup has not been completed yet.")

    with open(setup_data_path, "r") as f:
        all_configs = json.load(f)
    guild_id_str = str(ctx.guild.id)
    config = all_configs.get(guild_id_str, {})

    session_roles = config.get("session_roles", [])
    author_role_ids = [role.id for role in ctx.author.roles]

    if not any(rid in session_roles for rid in author_role_ids):
        return await ctx.send("❌ You do not have permission to run this command.")

    ping_roles = config.get("session_ping_roles", [])
    vote_count = config.get("session_vote_threshold", 5)

    ping_mentions = [f"<@&{rid}>" for rid in ping_roles if rid]
    session_mentions = [f"<@&{rid}>" for rid in session_roles if rid]

    if not ping_mentions:
        return await ctx.send("⚠️ No session ping roles are set up.")

    server_name = config.get("server_name", "Unknown Server")

    class VoteView(View):
        def __init__(self):
            super().__init__(timeout=None)
            self.voters = set()
            self.message = None

        @discord.ui.button(label="✅ Vote", style=discord.ButtonStyle.success, custom_id="vote_button")
        async def vote(self, interaction: discord.Interaction, button: discord.ui.Button):
            user_id = interaction.user.id
            if user_id in self.voters:
                await interaction.response.send_message("❗ You’ve already voted.", ephemeral=True)
                return

            self.voters.add(user_id)
            embed = self.message.embeds[0]
            current_votes = len(self.voters)
            embed.set_field_at(0, name="✅ Votes", value=f"{current_votes} / {vote_count}", inline=False)
            embed.set_footer(text="Made by 1Vortexx")
            await self.message.edit(embed=embed, view=self)

            await interaction.response.send_message("🗳️ Your vote has been counted!", ephemeral=True)

            if current_votes >= vote_count:
                await ctx.send(content=" ".join(session_mentions))
                ready_embed = discord.Embed(
                    title="✅ Session Ready to Start",
                    description="Enough users have voted to start the session!",
                    color=discord.Color.green()
                )
                ready_embed.set_footer(text="Made by 1Vortexx")
                await ctx.send(embed=ready_embed)
                try:
                    await ctx.author.send(f"✅ You now have enough votes to start the session in **{ctx.guild.name}**.")
                except discord.Forbidden:
                    pass

    embed = discord.Embed(
        title="📢 Session Startup Vote",
        description=(
            f"The **{server_name} Management Team** is looking to host a session!\n\n"
            "Click the button below to vote.\n"
            f"We need **{vote_count} votes** to start."
        ),
        color=discord.Color.green()
    )
    embed.add_field(name="✅ Votes", value=f"0 / {vote_count}", inline=False)
    embed.set_footer(text="Made by 1Vortexx")

    view = VoteView()
    view.message = await ctx.send(content=" ".join(ping_mentions), embed=embed, view=view)


@bot.command()
async def ssd(ctx):
    if not os.path.exists(setup_data_path):
        return await ctx.send("⚠️ Setup has not been completed yet.")

    with open(setup_data_path, "r") as f:
        all_configs = json.load(f)
    guild_id_str = str(ctx.guild.id)
    config = all_configs.get(guild_id_str, {})

    session_roles = config.get("session_roles", [])
    author_role_ids = [role.id for role in ctx.author.roles]

    if not any(rid in session_roles for rid in author_role_ids):
        return await ctx.send("❌ You do not have permission to run this command.")

    embed = discord.Embed(
        title="Server Shutdown",
        description=(
            "The server is currently shut down.\n"
            "Please do not join until the management team hosts a new session."
        ),
        color=discord.Color.red()
    )
    if ctx.guild.icon:
        embed.set_thumbnail(url=ctx.guild.icon.url)

    embed.set_footer(text="Made by 1Vortexx")

    await ctx.send(embed=embed)

@bot.command()
async def cmds_support(ctx):
    embed = discord.Embed(
        title="🛠️ Command Support - Detailed Command List",
        description="Here is a detailed list of all bot commands, their usage, who can use them, and example usage.",
        color=discord.Color.teal()
    )

    commands_info = [
        {
            "name": "!setup",
            "description": "Configure all bot settings for your server. Run once or to reconfigure specific settings.",
            "permissions": "Server Owner or Administrator",
            "example": "!setup"
        },
        {
            "name": "!reconfigure",
            "description": "Update a specific bot setting without redoing the full setup process.",
            "permissions": "Administrator Or Bot Manager",
            "example": "!reconfigure"
        },
        {
            "name": "!viewsetup",
            "description": "View the current bot configuration for your server.",
            "permissions": "Everyone",
            "example": "!viewsetup"
        },
        {
            "name": "!resetsetup",
            "description": "Reset the bot’s setup configuration for this server.",
            "permissions": "Server Owner only",
            "example": "!resetsetup"
        },
        {
            "name": "!ssuvote",
            "description": "Start a vote to launch a session. Session Management roles only.",
            "permissions": "Session Management Roles",
            "example": "!ssuvote"
        },
        {
            "name": "!ssu",
            "description": "Announce a session startup to the server. Session Management roles only.",
            "permissions": "Session Management Roles",
            "example": "!ssu"
        },
        {
            "name": "!ssd",
            "description": "Announce a session shutdown to the server. Session Management roles only.",
            "permissions": "Session Management Roles",
            "example": "!ssd"
        },
        {
            "name": "~~!ticket [reason]~~ (WIP AVAILABLE FOR BRICKMASTER BETA)",
            "description": "Open a new ticket with an optional reason.",
            "permissions": "Everyone",
            "example": "!ticket I need help with my account"
        },
        {
            "name": "~~!close~~ (WIP AVAILABLE FOR BRICKMASTER BETA)",
            "description": "Close your current ticket. Can only close tickets you own or if you have manage channels permission.",
            "permissions": "Ticket owner or staff with Manage Channels permission",
            "example": "!close"
        },
        {
            "name": "~~!session~~ (WIP AVAILABLE FOR BRICKMASTER BETA)",
            "description": "Check which ticket channel you currently have open.",
            "permissions": "Ticket owner",
            "example": "!session"
        },
        {
            "name": "!kick @user [reason]",
            "description": "Kick a member from the server.",
            "permissions": "Users with Kick Members permission",
            "example": "!kick @user Spamming"
        },
        {
            "name": "!ban @user [reason]",
            "description": "Ban a member from the server.",
            "permissions": "Users with Ban Members permission",
            "example": "!ban @user Harassment"
        }
    ]

    for cmd in commands_info:
        embed.add_field(
            name=cmd["name"],
            value=(
                f"**Description:** {cmd['description']}\n"
                f"**Who can use it:** {cmd['permissions']}\n"
                f"**Example:** `{cmd['example']}`"
            ),
            inline=False
        )
    
    embed.set_footer(text="Made by 1Vortexx")

    await ctx.send(embed=embed)
bot.run(TOKEN)
