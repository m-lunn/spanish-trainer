class AuxiliaryVerbIsMissingException(Exception):
    """Haber and estar must be in the database before adding other verbs."""
    pass

class TenseNotFoundException(Exception):
    """Tense not found."""
    pass

class PersonNotFoundException(Exception):
    """Person not found."""
    pass