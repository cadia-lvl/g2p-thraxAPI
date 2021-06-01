
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse,PlainTextResponse
import subprocess
__version__ = 0.1

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def home() -> str:
    return """
<html>
    <head><title>g2p thrax API</title></head>
    <body>
        <h1>g2p thrax API Server v{0}</h1>
        <ul><li><a href="/docs">Documentation</a></li></ul>
    </body>
</html>
""".format(__version__)

def run(text):
    proc = subprocess.Popen(['build/thraxg2p','--far=/usr/src/app/g2p-thrax/grammars/g2p.far'],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            )
    stdout_value, stderr_value = proc.communicate(text.encode('utf-8'))
    a = stdout_value.decode('utf-8')
    return a[29:-15]
    print(stdout_value, stderr_value)
    return ""
@app.post('/g2p', response_class=PlainTextResponse)
def g2p(text : str): 
    return run(text)

