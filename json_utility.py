import json, os

class JSONUtility:
  def from_json(file_path: str) -> dict | list:
    """
    Load JSON data from a file.

    #### Parameters:
     - file_path : str > The path to the JSON file.

    #### Returns:
    dict | list > The loaded JSON data as a dictionary or a list, or None if the file does not exist.
    """
    # Check if the file exists at the specified file_path
    if os.path.exists(file_path):
      # If the file exists, open it
      with open(file_path) as file:
        # Read the content of the file
        content = file.read()
        # Parse the JSON content into a Python dictionary or list
        data = json.loads(content)
        # Return the parsed JSON data
        return data
    else:
      # If the file does not exist, return None
      return None
  
  def to_json(file_path: str, data: dict | list) -> None:
    """
    Write data to a JSON file.

    Parameters:
     - file_path : str > The path to the JSON file.
     - data : dict | list > The data to be written to the JSON file.
    """
    # Open the file at the specified file_path in write mode with the write access
    # The "w+" mode truncates the file if it exists, and creates a new file if it doesn't exist
    with open(file_path, "w+", encoding="utf-8") as file:
      # Convert the Python dictionary or list data to a JSON string
      new_data = json.dumps(data)
      # Write the JSON string to the file
      file.write(new_data)