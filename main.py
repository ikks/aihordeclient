#!env python
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
#


# When you are developing, remember to run this as
#
# uv run main.py
#

import logging
import os
import random
import sys
import tempfile
from aihordeclient import (
    opustm_hf_translate,
    AiHordeClient,
    InformerFrontend,
    ANONYMOUS_KEY,
    IdentifiedError,
    MESSAGE_PROCESS_INTERRUPTED,
)
from typing import Any, Dict, Tuple


DEBUG = False

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
        super().__init__()
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


def configuration(
    prompt: str = "blue cat with purple mouse",
) -> Tuple[Dict[str, Any], AiHordeClient, SimpleInformer]:
    """
    Sets up options to call the service
    """

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

    return options, ah_client, informer


def process(
    options: Dict[str, Any], ah_client: AiHordeClient, informer: InformerFrontend
):
    """
    Given that the service was configured, proceeding to make all the calls
    """
    try:
        result = ah_client.generate_image(options)

        if result:
            for image in result:
                print("✨✨✨✨✨\n\nvv " + image + "\n\n")
        else:
            # If no images were generated, still review if there is option to download
            # one being processed
            print(f"{ah_client.get_tooltip()}")
            if informer.generated_url:
                print("✅\n\n" + informer.get_generated_image_url_status()[2])

        if options["api_key"] != ANONYMOUS_KEY:
            print(ah_client.get_balance())

    except IdentifiedError as ex:
        if ex.message == MESSAGE_PROCESS_INTERRUPTED:
            print("Expected interruption")
        if ah_client.status_url:
            print(f"Grab the image from {ah_client.status_url}")


def simple_sample(text) -> None:
    """
    Configuration and calling
    """
    options, ah_client, informer = configuration(text)
    process(options, ah_client, informer)
    print(f"seed is {ah_client.settings['seed']}")
    print(ah_client.get_full_description())


def cancel_sample(text) -> None:
    """
    The user will be able to cancel, there will be a delay because
    if a request is being answered by the API, we wait it to finish
    and stop from making new requests. This sample waits 10 seconds
    to send a message to cancel the process.
    """
    options, ah_client, informer = configuration(text)

    options["max_wait_minutes"] = 20

    from threading import Thread

    t = Thread(target=process, args=[options, ah_client, informer])
    t.start()
    print("Wait 10 seconds")
    from time import sleep

    sleep(10)
    print("Interrupting")
    logging.error("Interrupting\n\n\n")
    ah_client.cancel_process()
    if informer.generated_url:
        print("✅\n\n" + informer.get_generated_image_url_status()[2])


def main():
    if sys.argv == 2:
        prompt = sys.argv[1]
    else:
        prompts = (
            ("Una vaca dentro de una lavadora", "es"),
            ("un chien buvant du lait", "fr"),
        )
        chosen = random.choice(prompts)
        if isinstance(chosen[0], str):
            print(f"translating «{chosen[0]}»")
            prompt = opustm_hf_translate(*chosen)
        else:
            prompt = chosen[0]
        print(f"prompt is «{prompt}»")

    # simple_sample(prompt)

    # The next one shows how to cancel from the user
    cancel_sample(prompt)


if __name__ == "__main__":
    main()
