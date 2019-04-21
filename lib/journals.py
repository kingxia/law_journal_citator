from enum import IntEnum

class Journal():
    def __init__(self, _id, name, short):
        self.id = _id
        self.name = name
        self.short = short

class Journals(IntEnum):
    HARV_JOLT = 0

## TODO: Find a better storage format for journals
JOURNALS = {
    0: Journal(0, 'Harvard Journal of Law & Technology', 'Harv. J.L. Tech.')
}
