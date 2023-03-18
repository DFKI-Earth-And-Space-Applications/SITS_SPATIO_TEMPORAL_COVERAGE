import os
from utils.read_utils import save_yaml

if __name__ == "__main__":
    input_dir = '/ds/images/AI4EO/multi/landcovernet/ref_landcovernet_sa_v1/ref_landcovernet_sa_v1_source_sentinel_2/'

    patches_ids = list(set(['_'.join(patch.split('_')[7:9]) for patch in os.listdir(input_dir) if patch != 'collection.json']))[:2]
    dataset_structure =  dict.fromkeys(patches_ids, {})
    print(patches_ids)
    for patch_id in patches_ids:
        print(patch_id,'___')
        scl_paths = [os.path.join(input_dir,ts,'SCL.tif') for ts in os.listdir(input_dir) if patch_id in ts]
        dataset_structure[patch_id] = {'scl_mask_paths': scl_paths, 'boundary_paths': None}
    print(f"In total {len(patches_ids)} patches were scanned ")

    save_yaml(yaml_path='../coverage/test/test.yaml', data = dataset_structure)
