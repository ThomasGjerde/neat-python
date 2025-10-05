import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHECKPOINT_DIR = os.path.join(BASE_DIR, "checkpoints")
DEFAULT_CHECKPOINT_PREFIX = os.path.join(CHECKPOINT_DIR, "neat-checkpoint-")
