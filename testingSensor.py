# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os 



def arrayUpdate():
    global counter;
    global array;

    counter += 1;
    array.append(counter)


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        
        global array
        arrayUpdate()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open(dir_path + '/MainFile.html', 'rb') as file: 
            self.wfile.write(file.read())

        #Sends array containing data

        self.wfile.write(bytes("var myArray =" + str(array) +"</script>", "utf-8"))
        self.wfile.write(bytes("\n","utf-8"))

        self.wfile.write(bytes("</body></html>", "utf-8"))
        self.wfile.write(bytes("\n","utf-8"))


if __name__ == "__main__":

    hostName = "localhost"
    serverPort = 8080
    array = []
    counter = 0

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

