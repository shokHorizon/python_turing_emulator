class Validators():
    def __init__(self) -> None:
        self.vocabulary = set()
    

    def vocabulary_validator(self, value, old_value):
        match(len(value)):
            case 0:
                if old_value in self.vocabulary:
                    self.vocabulary.remove(old_value)
                return True
            case 1:
                if value not in self.vocabulary:
                    self.vocabulary.add(value)
                    return True
        return False

    def rule_validator(self, value):
        if len(value) >= 3:
            return value[2:].isdigit()
        if len(value) == 2:
            return value[1] in ('<', '>', '.',)
        return True