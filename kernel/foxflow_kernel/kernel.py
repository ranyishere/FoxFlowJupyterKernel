from ipykernel.kernelbase import Kernel
import subprocess

import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class FoxFlowKernel(Kernel):

    implementation = 'FoxFlow'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'

    language_info = {
        'name': 'FoxFlow',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }

    banner = "Fox Flow kernel 0.01"

    fox_flow_bin_location = '/home/rany/Work/research/FoxFlow/src/foxflow.jl'

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None,
                   allow_stdin=False):


        if not silent:

            # results = 'test'
            # logging.debug("test hello world")
            # print("code: ", code)

            results = subprocess.run(
                    ['julia', self.fox_flow_bin_location, code],
                    capture_output=True,
                    text=True
            )

            stream_content = {
                        'name': 'stdout',
                        # 'text': 'woops'
                        'text': results.stdout
                    }

            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
                'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
       }
