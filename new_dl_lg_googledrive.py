import requests, re 

with open('alistmeldtrim2.txt', 'r') as rf:
    meld_trim_contents = rf.read()
array= meld_trim_contents.split('\n')
test=array[0:1]


i=0
full=re.compile(r'-->(.+)<.+\'(0B-.+)\/\'')


while i< len(array):
    st= array[i]
    i+=1
    f=full.search(st)
    if f:
        title=f.group(1)
        tit= title.replace(':', '-')
        code=f.group(2)
        print('Downloading '+ title, code +'...')
    else:
        print('no match found')

    def download_file_from_google_drive(id, destination):
        URL = "https://docs.google.com/uc?export=download"

        session = requests.Session()

        response = session.get(URL, params = { 'id' : id }, stream = True)
        token = get_confirm_token(response)

        if token:
            params = { 'id' : id, 'confirm' : token }
            response = session.get(URL, params = params, stream = True)

        save_response_content(response, destination)    

    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    if __name__ == "__main__":
        file_id = code
        destination = 'C:\\Users\\andrew\\Desktop\\c1\\%s.pdf' %(tit)
        download_file_from_google_drive(file_id, destination)

