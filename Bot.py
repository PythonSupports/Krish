from pyrogram import Client, filters
import config

# Initialize the bot client with credentials from config.py
app = Client(
    "edit_guardian_bot",
    bot_token=config.BOT_TOKEN,   # Your Telegram bot token
    api_id=config.API_ID,         # Your API ID (integer)
    api_hash=config.API_HASH      # Your API Hash
)

# /start command handler - sends welcome message and video
@app.on_message(filters.command("start"))
def start_handler(client, message):
    welcome_text = "I'm group edit guardian bot I detect group edit message and delete him fast"
    video_url = "https://files.catbox.moe/ir15jt.mp4"
    
    # Send the welcome text
    client.send_message(
        chat_id=message.chat.id,
        text=welcome_text
    )
    
    # Send the start video
    client.send_video(
        chat_id=message.chat.id,
        video=video_url,
        caption="Start video"
    )

# Handler for edited messages in groups
@app.on_edited_message(filters.group)
def handle_edited_message(client, message):
    try:
        # Delete the edited message
        client.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)
    except Exception as e:
        print(f"Failed to delete message: {e}")
    
    # Send a warning reply in the group
    client.send_message(
        chat_id=message.chat.id,
        text=f"{message.from_user.first_name}, edited messages are not allowed in this group!",
        reply_to_message_id=message.message_id
    )

if __name__ == "__main__":
    app.run()
