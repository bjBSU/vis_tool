import sys, os

os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

os.environ['RETICO'] = 'retico-core'
os.environ['RETICOV'] = 'retico-vision'
os.environ['WASR'] = 'retico-whisperasr'


sys.path.append(os.environ['RETICO'])
sys.path.append(os.environ['RETICOV'])
sys.path.append(os.environ['WASR'])


import retico_core
from retico_core.audio import MicrophoneModule
from retico_whisperasr.whisperasr import WhisperASRModule
from retico_core.debug import DebugModule


# configure loggers
terminal_logger, file_logger, server_logger = retico_core.log_utils.configurate_logger(
    "logs/run", filters = None, server_port='http://localhost:3000'
)

mic = MicrophoneModule()
asr = WhisperASRModule(language="english")
debug = DebugModule()  

mic.subscribe(asr)
asr.subscribe(debug)
mic.subscribe(debug)

mic.run()
asr.run()
debug.run()  

print("running now!")
input()

mic.stop()
asr.stop()
debug.stop()   