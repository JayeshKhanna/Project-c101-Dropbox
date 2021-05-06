import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AuxjCnQP9ha1v7a_JupOXGVf81JgEc3-VrA59tvhVvi-ancQJhW9FBMFwtUgMPnvieJ3dgkohtXscXO8DMa8OsEG5RKMBzlXtxXu3Fx482_2EE0IgJXG7sXO9fOg7s3xcumRauo'
    transferData = TransferData(access_token)

    file_from = input('Enter the path of the file to be transferred')
    file_to = input('Enter the path of the file to be uploaded to Dropbox') 

    # API v2
    transferData.upload_file(file_from, file_to)
print("File has been moved")
if __name__ == '__main__':
    main()