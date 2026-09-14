def json_content_extractor(content):
    starting_index=content.find("{")
    ending_index=content.rfind("}")+1
    extracted_content=content[starting_index:ending_index]
    return extracted_content