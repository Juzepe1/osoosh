###################################################################################
# 
#    Copyright (C) 2020 Cetmix OÜ
#
#   Odoo Proprietary License v1.0
# 
#   This software and associated files (the "Software") may only be used (executed,
#   modified, executed after modifications) if you have purchased a valid license
#   from the authors, typically via Odoo Apps, or if you have received a written
#   agreement from the authors of the Software (see the COPYRIGHT file).
# 
#   You may develop Odoo modules that use the Software as a library (typically
#   by depending on it, importing it and using its resources), but without copying
#   any source code or material from the Software. You may distribute those
#   modules under the license of your choice, provided that this license is
#   compatible with the terms of the Odoo Proprietary License (For example:
#   LGPL, MIT, or proprietary licenses similar to this one).
# 
#   It is forbidden to publish, distribute, sublicense, or sell copies of the Software
#   or modified copies of the Software.
# 
#   The above copyright notice and this permission notice must be included in all
#   copies or substantial portions of the Software.
# 
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#   DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#   ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#
###################################################################################

{
    "name": "Mail Messages Easy Pro:"
    " Show Lost Message, Move Message, Reply, Forward,"
    " Move, Edit or Delete from Chatter,"
    " Filter Messages in Chatter",
    "version": "14.0.5.0.0",
    "summary": """Extra features for free 'Mail Messages Easy' app""",
    "author": "Ivan Sokolov, Cetmix",
    "license": "OPL-1",
    "price": 79.00,
    "currency": "EUR",
    "category": "Discuss",
    "support": "odooapps@cetmix.com",
    "website": "https://cetmix.com",
    "live_test_url": "https://demo.cetmix.com",
    "description": """
Show Lost Message, Move Message, Reply,
 Forward, Move, Edit or Delete
  from Chatter, Filter Messages in Chatter
""",
    "depends": ["prt_mail_messages", "mail"],
    "data": [
        "security/groups.xml",
        "views/assets.xml",
        "views/prt_mail_pro.xml",
        "views/mail_assign.xml",
    ],
    "images": ["static/description/banner_pro.png"],
    "qweb": [
        "static/src/components/message/message.xml",
        "static/src/components/chatter_topbar/chatter_topbar.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
