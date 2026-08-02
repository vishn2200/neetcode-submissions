class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append([value,timestamp])
        else:
            self.d[key] = [[value, timestamp]] 

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            # print(type(self.d[key][0]))
            for i in range(len(self.d[key])-1,-1,-1):
                if self.d[key][i][1]<=timestamp:
                    return self.d[key][i][0]
            return ""
        else:
            return ""
