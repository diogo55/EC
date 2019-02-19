import asyncio
import os
import pickle
from Functs import cifrar,decifrar

password = b"Some password"

@asyncio.coroutine 
def echo_emitter(message, loop):
    reader,writer = yield from asyncio.open_connection('127.0.0.1', 9999, loop=loop)
    crypto = cifrar(message,password)
    print(str(crypto))
    mess = pickle.dumps(crypto)
    writer.write(mess)
    writer.close()

def run_emitter():
   message = b'Hello, World!' 
  
   loop = asyncio.get_event_loop()
   loop.run_until_complete(echo_emitter(message,loop))
   loop.close() 

run_emitter()