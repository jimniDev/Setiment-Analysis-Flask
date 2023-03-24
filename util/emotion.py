class Emotion:
    def __init__(self):
        pass

    JOY = 0
    ANXIETY = 1
    EMBARRASSMENT = 2
    SADNESS = 3
    ANGER = 4
    HURT = 5

    def to_string(self, num):
        if num == self.JOY:
            return "기쁨"
        if num == self.ANXIETY:
            return "불안"
        if num == self.EMBARRASSMENT:
            return "당황"
        if num == self.SADNESS:
            return "슬픔"
        if num == self.ANGER:
            return "분노"
        if num == self.HURT:
            return "상처"
        
    def to_num(self, st):
        st = st.strip()
        if st == "기쁨":
            return self.JOY
        if st == "불안":
            return self.ANXIETY
        if st == "당황":
            return self.EMBARRASSMENT
        if st == "슬픔":
            return self.SADNESS
        if st == "분노":
            return self.ANGER
        if st == "상처":
            return self.HURT

