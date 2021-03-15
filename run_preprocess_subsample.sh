VGG_BASE='/data/vggface'
python preprocess_vggface.py --op preprocess --image_directory "${VGG_BASE}/test" --output_directory "${VGG_BASE}/test_preprocessed_sampled" --bbox_file "${VGG_BASE}/bb_landmark/loose_bb_test.csv" --sampled_identities "sampled_identities.txt"
python preprocess_vggface.py --op write_embeddings --image_directory "${VGG_BASE}/test_preprocessed_sampled" --output_directory "${VGG_BASE}/test_preprocessed_sampled" --bbox_file "${VGG_BASE}/bb_landmark/loose_bb_test.csv" --sampled_identities "sampled_identities.txt"
