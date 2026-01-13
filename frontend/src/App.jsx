import { useState , useEffect} from 'react'
import './App.css';


const API_URL = "http://127.0.0.1:8000/todos";


function App() {
  const [todos, setTodos] = useState([]);
  const [item, setItem] = useState("");

  // load item 
  useEffect(() => {
    loadTodos();
  }, []);

  // load item function
  async function loadTodos() {
    const res = await fetch(API_URL);
    const data = await res.json();
    setTodos(data);
  }

  // add item function
  async function addTodo(e) {
    e.preventDefault();

    await fetch(API_URL, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({item}),
    });

    setItem("");
    loadTodos();
  }

  // delete item 
  async function deleteTodo(id) {
    await fetch(`${API_URL}/${id}`, {
      method: "DELETE"
    });
    loadTodos();
  }

  return (
    <div className='container'>
      <h1>Todo app</h1>

      <form onSubmit={addTodo}>
        <input
          type='text'
          value={item}
          onChange={(e) => setItem(e.target.value)}
          placeholder='Enter a todo'
          required
        />
        <button type='submit'>Add</button>
      </form>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            {todo.item}
            <button onClick={() => deleteTodo(todo.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
