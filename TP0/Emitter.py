import asyncio
import os
import json
from Functs import cifrar,decifrar

password = b"Some password"

@asyncio.coroutine 
def echo_emitter(message, loop):
    reader,writer = yield from asyncio.open_connection('127.0.0.1', 9999, loop=loop)
    crypto = cifrar(message,password)
    print(str(crypto))
    crypto = json.dumps(str(crypto))
    e = crypto.encode()
    writer.write(e)
    writer.close()

def run_emitter():
   message = b'Hello, World!' 
  
   loop = asyncio.get_event_loop()
   loop.run_until_complete(echo_emitter(message,loop))
   loop.close() 

run_emitter()