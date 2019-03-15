import hashlib
#datum
class packet:

    def __init__(self, source, destination, sequence_number, size, data, checksum, transmission_id ):
        self.source = source
        self.destination = destination
        self.sequence_number = sequence_number
        self.size = size
        self.data = data
        self.checksum = self.generateChecksum(self)


    def generateChecksum(self):
        return hashlib.md5(self.data)




