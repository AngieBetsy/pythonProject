#
# import asyncio
# from asyncio import AbstractEventLoop
# from typing import Any, Callable, Dict, Generator, List, Optional
#
# import pytest
# from playwright.sync_api import (
#     Browser,
#     BrowserContext,
#     Page,
#     Playwright,
#     sync_playwright,
# )
#
#
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, video_path):
#     return {
#         **browser_context_args,
#         "record_video_dir": video_path,
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         }
#     }
#
#
# @pytest.fixture(scope="session")
# def video_path():
#     return "./videos"
