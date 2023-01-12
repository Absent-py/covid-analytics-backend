from app.connection import DBConnection


class JPackage:
    def __init__(self):
        self.headers = None
        self.body = None
        self.packageSize = 1000

    def __del__(self):
        del self.headers
        del self.body

    def setHeaders(self, count):
        parts = []
        currentId = 1
        while currentId < count:
            if currentId + self.packageSize - 1 < count:
                parts.append([currentId, currentId + self.packageSize - 1])
                currentId += self.packageSize
            else:
                parts.append([currentId, count])
                currentId = count
        self.headers = {
            'count': count,
            'parts': parts
        }
        return self.headers

    def setBody(self, table):
        self.body = []
        try:
            Connection = DBConnection()
            for part in self.headers['parts']:
                print(part)
                self.body.append(Connection.getPackage(part, table, self.packageSize))
        except ():
            pass
        return self.body
