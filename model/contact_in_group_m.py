from sys import maxsize


class ContactInGroup:

    def __init__(self, user_id=None, group_id=None):
        self.user_id = user_id
        self.group_id = group_id

    def __repr__(self):
        return "%s:%s" % (self.user_id, self.group_id)

    def __eq__(self, other):
        return self.user_id is None or other.user_id is None or self.user_id == other.user_id and self.group_id == other.group_id

    def user_id_or_max(self):
        if self.user_id:
            return int(self.user_id)
        else:
            return maxsize
