from bs4 import BeautifulSoup
import base64, sys, getopt

def main(argv):
    encode=''
    opts, args = getopt.getopt(argv,"hf:e:",["filename=","encode="])
    for opt, arg in opts:
        if opt == '-h':
            print ('convert.py -f <filename> -e <encode>')
            sys.exit()
        elif opt in ("-f", "--filename"):
            xml_input_file = arg
        elif opt in ("-e", "--encode"):
            pass_encode = arg

    with open(xml_input_file, 'r') as f:
        data = f.read()
    root = BeautifulSoup(data, "xml")
    server_list = root.find_all('Server')
    content=''
    try:
        for server in server_list:
            password  = server.find('Pass')
            if password is None:
                password = ''
            else:
                password = password.text
                if encode == 'b64':
                    password=base64.b64decode(password).decode('utf8')
            content = content + '\n\r' + server.Host.text + ':' + server.Port.text + ';' + server.User.text + ';' + password
    except Exception as e:
        print(str(e))
    print(content)

if __name__ == "__main__":
   main(sys.argv[1:])
