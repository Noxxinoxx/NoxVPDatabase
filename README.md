
# 📦 JSON File Database Handler in Python

A lightweight file-based JSON database manager written in Python. This module provides a simple interface for managing collections of data (referred to as **clusters**) stored in JSON files.

> Designed for small-scale data storage, quick prototyping, or environments where a full-fledged database is unnecessary.

---

## ✨ Features

- Simple JSON-based storage  
- Create, read, update, and delete (CRUD) operations  
- Automatic ID assignment and reassignment  
- Cluster (file) management  
- JSON command interface for easy integration  

---

## ⚙️ How It Works

- **Clusters** = JSON files that act as tables  
- Each **record** is a dictionary with a unique `"id"` and associated `"data"`  
- The `DBWriter` class handles low-level file operations  
- The `CommandHandler` provides a simple JSON-based command interface  

---

### Available Commands

| Command   | Arguments            | Description                              |
|-----------|----------------------|------------------------------------------|
| `Create`  | `[cluster_name]`     | Create a new cluster (JSON file)         |
| `Set`     | `[cluster_name]`     | Set the current active cluster           |
| `Get`     | `[]`                 | Get all items in the current cluster     |
| `Add`     | `[data_dict]`        | Add a new item to the cluster            |
| `Update`  | `[id, data_dict]`    | Update an existing item by ID            |
| `Remove`  | `[id]`               | Remove an item by ID                     |
| `Delete`  | `[]`                 | Delete the entire active cluster         |

---

## 🧠 Internals

### 🔹 DBWriter

Handles direct interaction with the file system and JSON data. Main methods include:

- `set_cluster`, `get_cluster`  
- `create_cluster`, `delete_cluster`  
- `add_cluster`, `update_cluster`, `remove_item`  
- `get_item_from_id`  



## 📝 Notes

- All clusters must be stored inside the `../Database/` directory relative to the script.  
- IDs are auto-incremented and reassigned when items are removed to maintain order.  
- Data for each item should be passed as a list inside a dictionary with a `"data"` key:  
  Example: `{"data": [{"name": "Alice"}]}`  


## 📄 License

MIT License. Free to use and modify.
