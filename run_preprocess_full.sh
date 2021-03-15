VGG_BASE='/data/vggface'
python preprocess_vggface.py --op preprocess --image_directory "${VGG_BASE}/test" --output_directory "${VGG_BASE}/test_preprocessed" --bbox_file "${VGG_BASE}/bb_landmark/loose_bb_test.csv" --sampled_identities ""
python preprocess_vggface.py --op write_embeddings --image_directory "${VGG_BASE}/test_preprocessed" --output_directory "${VGG_BASE}/test_preprocessed" --bbox_file "${VGG_BASE}/bb_landmark/loose_bb_test.csv" --sampled_identities ""
