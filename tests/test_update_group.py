# -*- coding: utf-8 -*-
from model.group_m import Group


def test_update_group_name(app):
    app.group.update_first_group(Group(name="Only name"))


def test_update_group_header(app):
    app.group.update_first_group(Group(header="Only header"))
