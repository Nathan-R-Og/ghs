# Gregory Horror Show
WIP Decompilation of Gregory Horror Show (PS2)

### Requirements
Python. Linux or WSL (for now). A Legally obtained rom of Gregory Horror Show.

1. Install prerequisites using `./install`. This should install everything required.

2. Unpack your ISO using `./unpack`. This will move all contents of your disc to `volume/` as well as copying `SLES_519.33` to the root of the project.

3. Run `./configure`. This should clean your `SLES_519.33` into `SLES_519.33.rom` and start splitting it for data.

4. When you are ready to build, run `ninja` to build the project. This will assemble assembly, compile C and repack everything back into a destination ISO.

5. The output ROM should be under `build/(version)/Gregory Horror Show.iso`

A matching ROM will output an **"OK"** in the console when building.

Note you can run `./configure --clean` and `ninja` whenever you make changes to the project to make sure the rom builds OK again.
