class Work:
    def preprocess(self, arr):

        return arr

    def sort(self, arr):

        return arr

    def postprocess(self, arr):

        return arr

    def work(self):
        arr = 1
        arr = self.preprocess(arr)
        arr = self.sort(arr)
        arr = self.postprocess(arr)
        return arr
