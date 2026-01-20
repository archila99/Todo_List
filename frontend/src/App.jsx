import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import './App.css';

const API_BASE_URL = "http://127.0.0.1:8000/todos";

function App() {
  const [todos, setTodos] = useState([]);
  const [item, setItem] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
      return;
    }
    loadTodos();
  }, []);

  const getHeaders = () => {
    const token = localStorage.getItem("token");
    return {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    };
  };

  async function loadTodos() {
    try {
      const res = await fetch(`${API_BASE_URL}/`, {
        headers: getHeaders()
      });

      if (res.status === 401) {
        navigate("/login");
        return;
      }

      const data = await res.json();
      if (Array.isArray(data)) {
        setTodos(data);
      } else {
        setTodos([]);
      }
    } catch (error) {
      console.error("Failed to load todos", error);
    }
  }

  async function addTodo(e) {
    e.preventDefault();
    await fetch(`${API_BASE_URL}/`, {
      method: "POST",
      headers: getHeaders(),
      body: JSON.stringify({ item }),
    });

    setItem("");
    loadTodos();
  }

  async function deleteTodo(id) {
    await fetch(`${API_BASE_URL}/${id}`, {
      method: "DELETE",
      headers: getHeaders()
    });
    loadTodos();
  }

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <div className='container'>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1>Todo app</h1>
        <button onClick={handleLogout} style={{ height: 'fit-content' }}>Logout</button>
      </div>

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
