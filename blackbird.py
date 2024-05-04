import os
import argparse
from rich.console import Console
import logging
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import config
from modules.whatsmyname.list_operations import checkUpdates
from modules.core.main import verifyUsername


def initiate():
    logging.basicConfig(
    filename=config.LOG_PATH,
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    parser = argparse.ArgumentParser(
        prog="blackbird",
        description="An OSINT tool to search for accounts by username in social networks.",
    )
    parser.add_argument("-u", "--username", help="The given username to search.")
    parser.add_argument("--csv", default=False, action=argparse.BooleanOptionalAction, help="Generate a CSV with the results.")
    parser.add_argument("--pdf", default=False, action=argparse.BooleanOptionalAction, help="Generate a PDF with the results.")
    parser.add_argument(
        "-v", "--verbose", default=False, action=argparse.BooleanOptionalAction, help="Show verbose output."
    )
    parser.add_argument("-t", "--timeout", type=int, default=30, help="Timeout in seconds for each HTTP request (Default is 30).")
    parser.add_argument("--no-update", action="store_true", help="Don't update sites lists.")
    parser.add_argument('-a', '--about', action='store_true', help='Show about information and exit.')
    args = parser.parse_args()

    # Store the necessary arguments to config Object
    config.username = args.username
    config.csv = args.csv
    config.pdf = args.pdf
    config.verbose = args.verbose
    config.timeout = args.timeout
    config.no_update = args.no_update
    config.about = args.about

    config.console = Console()
    

if __name__ == "__main__":
    initiate()
    config.console.print(
        """[red]
    ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ ▄▄▄▄    ██▓ ██▀███  ▓█████▄ 
    ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█████▄ ▓██▒▓██ ▒ ██▒▒██▀ ██▌
    ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒ ▄██▒██▒▓██ ░▄█ ▒░██   █▌
    ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██░█▀  ░██░▒██▀▀█▄  ░▓█▄   ▌
    ░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▓█  ▀█▓░██░░██▓ ▒██▒░▒████▓ 
    ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓███▀▒░▓  ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
    ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░▒░▒   ░  ▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ 
    ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░  ░    ░  ▒ ░  ░░   ░  ░ ░  ░ 
    ░          ░  ░     ░  ░░ ░      ░  ░    ░       ░     ░        ░    
        ░                  ░                     ░               ░      

    [/red]"""
    )
    config.console.print(
        "[white]Made with :beating_heart: by Lucas Antoniaci ([red]p1ngul1n0[/red])[/white]"
    )

    if config.about:
        config.console.print("""
        Author: Lucas Antoniaci (p1ngul1n0)
        Description: This tool search for accounts using data from the WhatsMyName project, which is an open-source tool developed by WebBreacher.
        WhatsMyName License: The WhatsMyName project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0).
        WhatsMyName Project: https://github.com/WebBreacher/WhatsMyName
        """)
        sys.exit()


    if not config.username:
        config.console.print("--username is required.")
        sys.exit()

    if config.no_update:
        config.console.print(":next_track_button:  Skipping update...")
    else:
        checkUpdates()

    if config.username:
        verifyUsername(config.username)
