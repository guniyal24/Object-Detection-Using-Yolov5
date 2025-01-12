from dataclasses import dataclass

@dataclass
class DataIngestionArtifect:
    data_zip_file_path : str 
    feature_store_path : str