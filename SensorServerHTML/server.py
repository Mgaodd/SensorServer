import BaseHTTPServer
import SocketServer
import os
import random



PORT = 8000

counter = 1
array =[]





class MyHttpRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    global array 
    def do_GET(self):
        self.send_response(200)

        with open("index.html", "r+") as f:
            for line in f:
                self.wfile.write(line);
        f.close()
        return
    
    def do_POST(self):
        global array;
        global counter;
        

        array = [array] + [counter, random.randrange(0, 10)]
        counter = counter + 1
        
        
        
        # Parse the form data posted

        # Begin the response
        response = str(array)
        
        self.send_response(200)
        self.send_header("content-length", str(len(response)))
        #self.send_header("response_text", response)
        self.end_headers()
        self.wfile.write(response)
        

        # Echo back information about what was posted in the form
        return 
        
        
    

        


def run_while_true(server_class=BaseHTTPServer.HTTPServer,
                   handler_class=MyHttpRequestHandler):
    """
    This assumes that keep_running() is a function of no arguments which
    is tested initially and after each request.  If its return value
    is true, the server continues.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run_while_true()
