class TimeMap:

    def __init__(self):
        '''
        store = {alice: {1:'happy'}}
        timestamps = {'key':[]}
        '''
        self.store = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = {}
            self.timestamps[key] = []
        self.store[key][timestamp] = value
        self.timestamps[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        if key not in  self.store:
            return ""
        if timestamp in self.timestamps[key]:
            return self.store[key][timestamp]
        l, r = 0, len(self.timestamps[key])-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if self.timestamps[key][m] <= timestamp:
                res = self.store[key][self.timestamps[key][m]]
                l = m + 1
            else:
                r = m - 1
        return res
        