# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

from hypothesis import given, settings, strategies as st

from unibuf import UnicodeBuffer


@given(st.text())
@settings(max_examples=2000)
def test_unicode_buffer(text: str) -> None:
    buffer = UnicodeBuffer(text)
    assert bytes(buffer) == text.encode(buffer.encoding)
    assert bytes(buffer).decode(buffer.encoding) == text
