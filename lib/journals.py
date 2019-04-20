from enum import IntEnum

class Journal():
    def __init__(self, name, cite):
        self.name = name
        self.cite = cite

class Journals(IntEnum):
    HARV_JOLT = 0

## TODO: Find a better storage format for journals
JOURNALS = {
    0: Journal('Harvard Journal of Law & Technology', 'Harv. J.L. Tech.')
}
