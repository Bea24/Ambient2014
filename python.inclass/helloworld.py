'''
Created on 03/apr/2014

@author: Baleani
'''

import cherrypy

class HelloWorld:
    exposed = True
    
    def GET(self):
        return "Hello world!"
    
if __name__ == '__main__':
    
    hello= HelloWorld()
    
    # publish the resource at api/v1/helloworld 
    cherrypy.tree.mount( 
        hello, '/api/v1/helloworld', 
        {'/': 
        {'request.dispatch': cherrypy.dispatch.MethodDispatcher()} 
        } 
    )
    
cherrypy.engine.start()
cherrypy.engine.block()