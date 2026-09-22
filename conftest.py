import os
from pathlib import Path
from dotenv import load_dotenv


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment: dev, qa, pre, prod"
    )


def pytest_configure(config):
    env = config.getoption("--env")

    env_file = Path(__file__).parent / "config" / f"{env}.env"

    if not env_file.exists():
        raise FileNotFoundError(
            f"Environment file not found: {env_file}"
        )

    load_dotenv(env_file)

    print(f"\nRunning tests against: {env.upper()}")
    print(f"Environment file: {env_file}")