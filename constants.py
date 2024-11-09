import os
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL") or "gpt-4o-mini"
INSTANCE_TYPE = os.environ.get("INSTANCE_TYPE") or "local"