import os
from dotenv import load_dotenv

load_dotenv()

from elevenlabs import ElevenLabs
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("XI_API_KEY")

user_name = "Luis"
schedule = "Computer Science classes at 12:00; Gym with Maya at 17:00"
prompt = f"You are a helpful assistant. Your interlocutor has the following schedule: {schedule}."
first_message = f"Hello {user_name}, how can I help you today?"

conversation_override = {
  "agent": {
    "prompt": {
      "prompt": prompt,
    },
    "first_message": first_message,
  },
}

config = ConversationConfig(
  conversation_config_override=conversation_override,
  extra_body={},
  dynamic_variables={},
)

client = ElevenLabs(api_key=API_KEY)

def print_agent_response(response):
  print(f"Agent: {response}")

def print_interrupted_response(original, corrected):
  print(f"Agent interrupted, truncated response: {corrected}")

def print_user_transcript(transcript):
  print(f"User: {transcript}")

conversation = Conversation(
  client=client,
  agent_id=AGENT_ID,
  config=config,
  requires_auth=True,
  audio_interface=DefaultAudioInterface(),
  callback_agent_response=print_agent_response,
  callback_agent_response_correction=print_interrupted_response,
  callback_user_transcript=print_user_transcript,
)

conversation.start_session()