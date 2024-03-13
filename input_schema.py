INPUT_SCHEMA = {
    "prompt": {
        "type": str,
        "required": True,
        "shape": [1],
        "data": ["There is a fine house in the forest"],
    },
    "negative_prompt": {"type": str, "required": False, "example": None, "shape": [1]},
    "width": {"type": int, "required": False, "example": [768, 512], "shape": [2]},
}
