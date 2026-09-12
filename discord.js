// Discord.js Configuration for Chico Loco 40
// Bot integration for music, community engagement, and notifications

const { Client, Intents, Collection } = require('discord.js');

// Initialize Discord Client
const client = new Client({
  intents: [
    Intents.FLAGS.GUILDS,
    Intents.FLAGS.GUILD_MEMBERS,
    Intents.FLAGS.GUILD_MESSAGES,
    Intents.FLAGS.DIRECT_MESSAGES,
    Intents.FLAGS.MESSAGE_CONTENT
  ]
});

// Bot configuration
const config = {
  token: process.env.DISCORD_TOKEN,
  prefix: '!',
  owner: process.env.DISCORD_OWNER_ID
};

// Command collection
client.commands = new Collection();

// Event: Bot Ready
client.on('ready', () => {
  console.log(`✅ Bot logged in as ${client.user.tag}`);
  client.user.setActivity('🎤 Chico Loco 40 | Hip-Hop', { type: 'LISTENING' });
});

// Event: Message Commands
client.on('messageCreate', async (message) => {
  if (message.author.bot) return;
  if (!message.content.startsWith(config.prefix)) return;

  const args = message.content.slice(config.prefix.length).trim().split(/ +/);
  const commandName = args.shift().toLowerCase();

  // Command handlers would go here
  if (commandName === 'ping') {
    message.reply(`🏓 Pong! Latency: ${client.ws.ping}ms`);
  }
  
  if (commandName === 'music') {
    message.reply('🎵 Check out Chico Loco 40 on all streaming platforms!');
  }
});

// Error handling
client.on('error', error => {
  console.error('❌ Discord Client Error:', error);
});

process.on('unhandledRejection', error => {
  console.error('❌ Unhandled Rejection:', error);
});

// Login to Discord
client.login(config.token);

module.exports = client;
