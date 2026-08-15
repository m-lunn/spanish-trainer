class tense:
 
     def __init__(self, mood, timeframe, is_compound=False, auxiliary_verb=None):
         self.mood = mood
         self.timeframe = timeframe
         self.is_compound = is_compound
         self.auxiliary_verb = auxiliary_verb