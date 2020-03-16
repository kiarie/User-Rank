class User:
    def __init__(self):
        self.user_rank = -8
        self.user_progress = 0
        self.update_rank()

    @property
    def rank(self):
        return self.user_rank

    @property
    def progress(self):
        return self.user_progress

    def set_rank(self, inc):
        self.user_rank += inc

    def inc_progress(self, rnk):
        if rnk < -8 or rnk > 8 or rnk == 0:
            raise ValueError(f"Rank {rnk} is Beyond Bounding values")

        curr_rank = self.rank if self.rank != -1 else 0  # hanldle for the case where rank is -1
        if rnk == curr_rank:
            self.user_progress += 3
        if rnk > curr_rank:
            diff = rnk - curr_rank
            self.user_progress += 10 * diff * diff
        if rnk < curr_rank:
            diff = curr_rank - rnk
            if diff < 2:
                self.user_progress += 1
        self.update_rank()

    def update_rank(self):
        if self.user_progress >= 100 and self.rank < 8:
            self.set_rank(1)
            self.user_progress -= 100
        if self.rank == 0:
            self.set_rank(1)