class Log:

    outFile = None

    @staticmethod
    def init(outPath = None):
        if outPath != None:
            Log.outFile = open(outPath, "w")

    @staticmethod
    def w(str):
        Log.write("[WARN] " + str)

    @staticmethod
    def e(str):
        Log.write("[ERR] " + str)

    @staticmethod
    def i(str):
        Log.write(str)

    @staticmethod
    def write(str):
        if Log.outFile != None:
            Log.outFile.write(str)
        else:
            print(str)

    @staticmethod
    def dispose():
        if Log.outFile != None:
            Log.outFile.close()