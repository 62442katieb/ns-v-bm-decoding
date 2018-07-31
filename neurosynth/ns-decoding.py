from neurosynth.base.dataset import Dataset
from neurosynth.analysis import decode, meta
from os.path import join

parent_dir = '/Users/Katie/Dropbox/Data/neurosynth_current_data/'
roi_dir = '/Users/Katie/Dropbox/Data/NSvBM-decoding/ROIs/'
sink_dir = '/Users/Katie/Dropbox/Data/NSvBM-decoding/'
paracentral = join(roi_dir, 'l-paracentral.nii.gz')
ofc = join(roi_dir, 'r-ofc.nii.gz')
uncus = join(roi_dir, 'r-ofc.nii.gz')
visual = join(roi_dir, 'smith-rsn70-1.nii.gz')
mask_list = [paracentral, ofc, uncus, visual]
mask_names = ['paracentral', 'orbitofrontal', 'uncus', 'visual']
dataset = Dataset.load(join(parent_dir,'dataset.pkl'))
for i, mask in enumerate(mask_list):
    ids = dataset.get_studies(mask=mask)
    ma = meta.MetaAnalysis(dataset, ids)
    ma.save_results(output_dir='.', prefix=mask_names[i])
    decoder = decode.Decoder(dataset)
    result = decoder.decode(['{0}_pFgA_z.nii.gz'.format(mask_names)], save=join(sink_dir,'decoded_{0}.txt'.format(mask_names)))
