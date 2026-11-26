 class Claim:
    claim_id: int
    item_id: int
    user_id: int
    claim_date: str
    status: str
    def __init__(self,claim_id,item_id,user_id,claim_date,status):
            self.claim_id=claim_id
            self.item_id = item_id
            self.user_id = user_id
            self.claim_date = claim_date
            self.status = status
 def __str__(self):
        return "Claim " + str(self.claim_id) + ": item " + str(self.item_id) + \
               " claimed by user " + str(self.user_id) + \
               " on " + self.claim_date + " (" + self.status + ")"