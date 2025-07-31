import React, { useReducer, useState, useEffect, useCallback, useMemo } from 'react';

// ---------- Code 1: React CRUD Application ----------
const initialState = [];

function userReducer(state, action) {
  switch (action.type) {
    case 'ADD_USER':
      return [...state, action.payload];
    case 'UPDATE_USER':
      return state.map((user) =>
        user.id === action.payload.id ? action.payload : user
      );
    case 'DELETE_USER':
      return state.filter((user) => user.id !== action.payload);
    default:
      return state;
  }
}

function CrudApp() {
  const [state, dispatch] = useReducer(userReducer, initialState);
  const [form, setForm] = useState({ id: '', name: '', email: '' });
  const [isEditMode, setIsEditMode] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  useEffect(() => {
    console.log(state);
  }, [state]);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (isEditMode) {
      dispatch({ type: 'UPDATE_USER', payload: form });
      setIsEditMode(false);
    } else {
      const newUser = {
        ...form,
        id: Date.now(),
      };
      dispatch({ type: 'ADD_USER', payload: newUser });
    }

    setForm({ id: '', name: '', email: '' });
  };

  const handleEdit = (user) => {
    setForm(user);
    setIsEditMode(true);
  };

  const handleDelete = (id) => {
    dispatch({ type: 'DELETE_USER', payload: id });
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>React CRUD Application </h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Name"
          value={form.name}
          onChange={handleChange}
          required
        />
        <br />
        <br />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
          required
        />
        <br />
        <br />
        <button type="submit">{isEditMode ? 'Update' : 'Add'} User</button>
      </form>
      <br />
      <hr />

      <h3>User List</h3>
      {state.length === 0 ? (
        <p>No users added.</p>
      ) : (
        <ul>
          {state.map((user) => (
            <li key={user.id} style={{ marginBottom: '12px' }}>
              <strong>{user.name}</strong> ({user.email}){' '}
              <button onClick={() => handleEdit(user)} style={{ marginRight: '10px' }}>Edit</button>
              <button onClick={() => handleDelete(user.id)}>Delete</button>
            </li>
          ))}
        </ul>
      )}
      <br />
    </div>
  );
}

// ---------- Code 2: useCallback Example ----------
function UseCallbackExample() {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState(1);

  const calculateSquare = useCallback(() => {
    console.log('Calculating...');
    let result = 0;
    for (let i = 0; i < 100000000; i++) {
      result = input * input;
    }
    return result;
  }, [input]);

  const squaredNumber = calculateSquare();

  return (
    <div>
      <h2>useCallback Example Demo</h2>
      <input
        type="number"
        value={input}
        onChange={(e) => setInput(Number(e.target.value))}
      />
      <p>Squared: {squaredNumber}</p>

      <button onClick={() => setCount(count + 1)}>Re-render</button>
      <p>Render count: {count}</p>
    </div>
  );
}

// ---------- Code 3: useMemo Example ----------
function UseMemoExample() {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState(1);

  const squaredNumber = useMemo(() => {
    console.log('Calculating...');
    let result = 0;
    for (let i = 0; i < 100000000; i++) {
      result = input * input;
    }
    return result;
  }, [input]);

  return (
    <div>
      <h2>useMemo Example Demo</h2>
      <input
        type="number"
        value={input}
        onChange={(e) => setInput(Number(e.target.value))}
      />
      <p>Squared: {squaredNumber}</p>

      <button onClick={() => setCount(count + 1)}>Re-render</button>
      <p>Render count: {count}</p>
    </div>
  );
}

// ---------- Main App ----------
function App() {
  return (
    <div>
      <CrudApp />
      <hr />
      <UseCallbackExample />
      <hr />
      <UseMemoExample />
    </div>
  );
}

export default App;