from datetime import datetime

class Deal:
    def __init__(self, ad_id: int, redeemer_id: int, rating: int, text: str, redeemed_at: datetime):
        self.ad_id = ad_id
        self.redeemer_id = redeemer_id
        self.rating = rating
        self.text = text
        self.redeemed_at = redeemed_at

    def __eq__(self, other):
        if isinstance(other, Deal):
            return self.ad_id == other.ad_id
        else:
            return False

    def to_print(self):
        return f"{self.text} от {self.redeemed_at} / Оценка: {self.rating}"