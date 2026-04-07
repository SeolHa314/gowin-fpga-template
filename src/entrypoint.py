import pathlib
import glob
import sys
from . import yosys
from . import nextpnr
from . import openfpgaloader

def entrypoint():

    if len(sys.argv) > 1 and not "--skip-synthesis" in sys.argv:
        skip_synthesis = False
    else:
        skip_synthesis = True
    
    for file in glob.glob(str(pathlib.Path("fpga_build") / "*")):
        if file.endswith(".gitkeep") or (skip_synthesis and file.endswith(".fs")):
            continue
        pathlib.Path(file).unlink()

    if not "--skip-synthesis" in sys.argv:
        yosys.run_yosys()
        nextpnr.runNextpnr()
        nextpnr.runGowinPack()
    else:
        # if "fpga_build/pack.fs" doesn't exist, raise an error
        if not pathlib.Path("fpga_build/pack.fs").exists():
            print("Error: fpga_build/pack.fs not found. Please run the script without --skip-synthesis first.")
            sys.exit(1)
    
    if len(sys.argv) > 1 and ("--write-flash" in sys.argv or "-f" in sys.argv):
        openfpgaloader.runOpenFPGALoader(write_flash=True)
    else:
        openfpgaloader.runOpenFPGALoader()
