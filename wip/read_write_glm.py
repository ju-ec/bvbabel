"""Read and write BrainVoyager GLM (general linear model) file."""

import os
import bvbabel
from pprint import pprint

FILE = "/home/faruk/Documents/temp_bvbabel_glm/BOLD_whole_brain_GLM.glm"

# =============================================================================

# Load GLM
header, data_R2, data_SS, data_beta, data_SS_XiY, data_meantc, data_ARlag = bvbabel.glm.read_glm(FILE)

# See header information
pprint(header)

# Save GLM
# in the same order as returned by bvbabel.glm.read_glm
# RFX: 
#    'data_R2' is the first (global) RFX map, 'data_beta' 
#    holds the subject/predictor beta maps, and all other map arguments 
#    should be 'None'
basename = FILE.split(os.extsep, 1)[0]
outname = "{}_bvbabel.glm".format(basename)
bvbabel.glm.write_glm(outname, header, data_R2, data_SS, data_beta, data_SS_XiY, data_meantc, data_ARlag)

print("Finished.")
