from ipykernel.kernelapp import IPKernelApp
from . import FoxFlowKernel


print("Launching kernel")
IPKernelApp.launch_instance(kernel_class=FoxFlowKernel)
