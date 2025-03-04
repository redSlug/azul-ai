# azul-ai

An AI that provides the next azul move in json form, given a game state. 

Here is an example response,

```json
{
    "source_factory_index": 0,
    "source_tile_index": 0,
    "source_tile_color": "green",
    "source_tile_count": 2,
    "target_row": 1,
    "target_open_space_count": 2
}
```

### Setup
``` bash
python -m virtualenv venv
source venv/bin/activate
```

### Run
Run the server and hit it with a POST request, [example payload](example_post.json).
```bash
server.py
```