"""
Better use livereload CLI instead
Start a `livereload` server: livereload [-h] [-p PORT] [-w WAIT] [directory]
"""

from livereload import Server, shell

server = Server()
server.watch("*.html", shell("make html", cwd=""))
server.serve(root="")
