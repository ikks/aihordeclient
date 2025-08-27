#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Minimal sample usage of AiHordeClient
# Authors:
#  * Igor Támara <https://github.com/ikks>
#
# MIT lICENSE
#
# https://github.com/ikks/aihorde-client/blob/main/LICENSE
#
# This script uses AiHordeClient class to generate an image
# using AIHorde https://aihorde.net

import logging
import os
import random
import sys
import tempfile
from aihordeclient import AiHordeClient, InformerFrontend, ANONYMOUS_KEY


DEBUG = True

VERSION = "0.2"

logger = logging.getLogger(__name__)
# Change the logging level to ERROR to lower the verbosity
# in the log
LOGGING_LEVEL = logging.INFO

log_file = os.path.join(tempfile.gettempdir(), "simple_client.log")
if DEBUG:
    LOGGING_LEVEL = logging.DEBUG
logging.basicConfig(
    filename=log_file,
    level=LOGGING_LEVEL,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class SimpleInformer(InformerFrontend):
    def __init__(self):
        self.finished: bool = False
        self.progress: float = 0.0
        self.status: str = ""
        self.asked: bool = False

    def has_asked_for_update(self) -> bool:
        return self.asked

    def just_asked_for_update(self) -> None:
        self.asked = True

    def path_store_directory(self) -> str:
        return tempfile.gettempdir()

    def set_finished(self):
        self.finished = True

    def show_error(
        self, message: str, url: str = "", title: str = "", buttons: int = 0
    ) -> None:
        print("[ERROR]: " + message)

    def show_message(
        self, message: str, url: str = "", title: str = "", buttons: int = 0
    ):
        print("NOTICE : " + message)

    def update_status(self, text: str, progress: float) -> None:
        self.progress = max(0.0, min(100.0, progress))
        self.status = text
        # logger.info(f"{self.status} { self.progress }")


def main():
    prompt = "blue cat with purple mouse"
    if sys.argv == 2:
        prompt = sys.argv[1]

    options = {
        "api_key": os.getenv("AIHORDE_API_KEY", ANONYMOUS_KEY),
        "prompt": prompt,
        "image_width": 384,
        "image_height": 384,
        "model": "stable_diffusion",
        "prompt_strength": 6.5,
        "steps": 15,
        "nsfw": False,
        "censor_nsfw": True,
        "max_wait_minutes": 3,
        "seed": "",
    }
    informer = SimpleInformer()
    ah_client = AiHordeClient(
        VERSION,
        "https://github.com/ikks/aihordeclient/raw/refs/heads/main/example/version.json",
        "https://github.com/ikks/aihordeclient/blob/main/README.md",
        "https://github.com/ikks/aihordeclient/raw/refs/heads/main/main.py",
        options,
        "sample_client",
        informer,
    )
    if options["api_key"] != ANONYMOUS_KEY:
        options["model"] = random.choice(
            ["Blank Canvas XL", "Dreamshaper", "Ultraspice"]
        )
        print(ah_client.get_balance())
    print(f"Using model «{options['model']}»")
    result = ah_client.generate_image(options)
    warned = False
    if "generated_url" in dir(informer):
        warned = True
        print(f"{informer.generated_url} to download in the future")
    else:
        for image in result:
            print(image)
        print(f"{ ah_client.get_tooltip()}")

    if ah_client.status_url and not warned:
        print(f"Please download from {ah_client.status_url}")

    print(ah_client.get_balance())


if __name__ == "__main__":
    main()
