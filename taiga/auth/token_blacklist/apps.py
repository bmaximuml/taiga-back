# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos Ventures SL
#
# The code is partially taken (and modified) from djangorestframework-simplejwt v. 4.7.1
# (https://github.com/jazzband/djangorestframework-simplejwt/tree/5997c1aee8ad5182833d6b6759e44ff0a704edb4)
# that is licensed under the following terms:
#
#   Copyright 2017 David Sanders
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy of
#   this software and associated documentation files (the "Software"), to deal in
#   the Software without restriction, including without limitation the rights to
#   use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#   of the Software, and to permit persons to whom the Software is furnished to do
#   so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

"""
Blacklist app
=============

This app provides token blacklist functionality.

If the blacklist app is detected in ``INSTALLED_APPS``, Taiga Auth will add any
generated refresh token to a list of outstanding tokens.  It will also check
that any refresh token does not appear in a blacklist of tokens before it
considers it as valid.

The blacklist app implements its outstanding and blacklisted token lists using
two models: ``OutstandingToken`` and ``BlacklistedToken``.  Model admins are
defined for both of these models.  To add a token to the blacklist, find its
corresponding ``OutstandingToken`` record in the admin and use the admin again
to create a ``BlacklistedToken`` record that points to the ``OutstandingToken``
record.

Alternatively, you can blacklist a token by creating a ``BlacklistMixin``
subclass instance and calling the instance's ``blacklist`` method:

.. code-block:: python

  from rest_framework_simplejwt.tokens import RefreshToken

  token = RefreshToken(base64_encoded_token_string)
  token.blacklist()

This will create unique outstanding token and blacklist records for the token's
"jti" claim or whichever claim is specified by the ``JTI_CLAIM`` setting.

The blacklist app also provides a management command, ``flushexpiredtokens``,
which will delete any tokens from the outstanding list and blacklist that have
expired.
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TokenBlacklistConfig(AppConfig):
    name = 'taiga.auth.token_blacklist'
    verbose_name = _('Token Blacklist')
    default_auto_field = 'django.db.models.BigAutoField'
