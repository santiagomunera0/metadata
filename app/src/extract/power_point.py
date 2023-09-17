from pptx import Presentation
import os

from src.common.common_tools import parameters

def get_propierties(presentation, file):
    file_size_mb = os.path.getsize(file) / (1024 * 1024)
    try:
        metadata = {
            "Title": presentation.core_properties.title,
            "Author": presentation.core_properties.author,
            "Subject": presentation.core_properties.subject,
            "Keywords": presentation.core_properties.keywords,
            "Created": presentation.core_properties.created,
            "Modified": presentation.core_properties.modified,
            "File Size (MB)": round(file_size_mb, 2),
            "Number of Slides": len(presentation.slides),
            "Categories": presentation.core_properties.category,
            "Comments": presentation.core_properties.comments,
        }

        return metadata

    except Exception as e:
        print("Error:", e)
        return None
    
def extract_metadata(file):
    presentation = Presentation(file)
    metadata = get_propierties(presentation, file)    

    print(metadata)    