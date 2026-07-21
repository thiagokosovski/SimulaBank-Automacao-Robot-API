from dotenv import load_dotenv
import os

load_dotenv()


def get_base_url():
    return os.getenv("API_BASE_URL")


def get_username():
    return os.getenv("API_USERNAME")


def get_password():
    return os.getenv("API_PASSWORD")


def get_environment():
    return os.getenv("ENVIRONMENT")