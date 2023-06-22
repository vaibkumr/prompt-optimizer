from datetime import datetime
from prompt_optimizer.wrapper import SQLDBManager

def test_db():
    db_manager = SQLDBManager("temp", "temp.db")
    with db_manager:
        data = [
            datetime.now(),
            "test_user",
            "prompt before",
            "prompt after",
            "continuation",
            2,
            2,
            1,
            "text-davinci-003",
            0,
            "None",
            0.12,
            0.11
        ]
        success = db_manager.add(data)
    assert success, "failed"
