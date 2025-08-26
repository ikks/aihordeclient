#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Minimal sample usage of AiHordeClient
# Authors:
#  * Igor Támara <https://github.com/ikks>
#
# MIT lICENSE
#
# https://github.com/ikks/aihorde-client/blob/main/LICENSE

import os
import tempfile
from typing import Tuple, Union
from aihordeclient import AiHordeClient, InformerFrontend, ANONYMOUS_KEY


class SimpleInformer(InformerFrontend):
    def __init__(self):
        self.finished: bool = False
        self.progress: float = 0.0
        self.status: str = ""

    def has_asked_for_update(self) -> bool:
        return True

    def just_asked_for_update(self) -> None:
        pass

    def path_store_directory(self) -> str:
        return tempfile.gettempdir()

    def get_generated_image_url_status(self) -> Union[Tuple[str, int, str], None]:
        return None

    def set_generated_image_url_status(self, url: str, valid_to: int) -> None:
        pass

    def set_finished(self):
        self.finished = True

    def show_error(message: str, url: str, title: str, buttons: int) -> None:
        print(message)

    def show_message(message: str, url: str, title: str, buttons: int):
        print("Error:" + message)

    def update_status(self, text: str, progress: float) -> None:
        self.progress = max(0.0, min(100.0, progress))
        self.status = text


def main():
    informer = SimpleInformer()

    ah_client = AiHordeClient(
        "0.1",
        "https://github.com/ikks/aihordeclient/example/version.json",
        "https://github.com/ikks/aihordeclient/README.md",
        "https://github.com/ikks/aihordeclient/main.py",
        {"api_key": os.getenv("AIHORDE_API_KEY", ANONYMOUS_KEY)},
        "sample_client",
        informer,
    )
    print(ah_client.get_balance())


if __name__ == "__main__":
    main()
