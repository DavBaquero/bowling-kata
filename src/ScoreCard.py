class ScoreCard:

    def __init__(self, scorecard):
        self.pins = scorecard
        self.last_frame = 10
        self.frame = 1
        self.score = 0
    
    def score_frame(self, roll):
        frame_pin = self.pins[roll]