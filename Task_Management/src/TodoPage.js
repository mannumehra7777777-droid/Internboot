import React, { useState, useEffect } from 'react';
import { AiOutlinePlus } from 'react-icons/ai';
import Todo from './Todo'; 
import { db } from './firebase'; 
import { query, collection, onSnapshot, updateDoc, doc, addDoc, deleteDoc, serverTimestamp } from 'firebase/firestore';
import { UserAuth } from './context/AuthContext';
import { useNavigate } from 'react-router-dom';

const style = {
  bg: `h-screen w-screen p-4 bg-gradient-to-r from-[#2F80ED] to-[#1CB5E0] overflow-y-auto`,
  container: `bg-slate-100 max-w-[500px] w-full m-auto rounded-md shadow-xl p-4`,
  heading: `text-3xl font-bold text-center text-gray-800 p-2`,
  form: `flex flex-col gap-2`,
  input: `border p-2 w-full text-xl`,
  select: `border p-2 w-full bg-white text-sm`,
  button: `border p-4 bg-purple-500 text-slate-100 flex justify-center items-center rounded`,
  count: `text-center p-2 font-semibold`,
  filterGroup: `flex gap-2 my-4 justify-center`
};

function TodoPage() {
  const { logOut,user } = UserAuth(); //
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      await logOut();
      navigate('/'); // Redirect to login page after logout
    } catch (error) {
      console.log(error);
    }
  };
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');
  const [priority, setPriority] = useState('Medium');
  const [category, setCategory] = useState('General');
  const [filter, setFilter] = useState('All');

  useEffect(() => {
    const q = query(collection(db, 'todos'));
    const unsubscribe = onSnapshot(q, (querySnapshot) => {
      let todosArr = [];
      querySnapshot.forEach((doc) => {
        todosArr.push({ ...doc.data(), id: doc.id });
      });
      setTodos(todosArr);
    });
    return () => unsubscribe();
  }, []);

  const createTodo = async (e) => {
    e.preventDefault();
    if (input === '') return;
    await addDoc(collection(db, 'todos'), {
      text: input,
      completed: false,
      priority,
      category,
      timestamp: serverTimestamp(),
    });
    setInput('');
  };

  const toggleComplete = async (todo) => {
    await updateDoc(doc(db, 'todos', todo.id), { completed: !todo.completed });
  };

  const updateTodo = async (id, newText) => {
    await updateDoc(doc(db, 'todos', id), { text: newText });
  };

  const deleteTodo = async (id) => {
    await deleteDoc(doc(db, 'todos', id));
  };

  const filteredTodos = todos.filter((t) => {
  if (filter === 'All') return true;
  
  // Use .includes() so "High" matches "🔥 High Priority"
  const priorityMatch = t.priority?.toLowerCase().includes(filter.toLowerCase());
  const categoryMatch = t.category?.toLowerCase().includes(filter.toLowerCase());
  
  return priorityMatch || categoryMatch;
});

  return (
    <div className={style.bg}>
      <div className={style.container}>
        <div className='flex justify-between items-center p-2'>
  <div className='flex items-center gap-2'>
    {/* Display Google Profile Picture */}
    {user?.photoURL && (
      <img 
        src={user.photoURL} 
        alt="Profile" 
        className='w-10 h-10 rounded-full border-2 border-white'
        referrerPolicy="no-referrer" 
      />
    )}
    <h3 className={style.heading}>To-Do Pro</h3>
  </div>
  
  <button 
    onClick={handleLogout} 
    className='bg-red-500 hover:bg-red-600 text-white px-4 py-1 rounded-md text-sm transition-colors'
  >
    Logout
  </button>
</div>
        <form onSubmit={createTodo} className={style.form}>
          <input value={input} onChange={(e) => setInput(e.target.value)} className={style.input} type='text' placeholder='Add a task...' />
          <div className='flex gap-2'>
            <select className={style.select} value={priority} onChange={(e) => setPriority(e.target.value)}>
              <option value="High">🔥 High </option>
              <option value="Medium">⚡ Medium</option>
              <option value="Low">💤 Low</option>
            </select>
            <select className={style.select} onChange={(e) => setCategory(e.target.value)}>
              <option value="Work">💼 Work</option>
              <option value="Personal">🏠 Personal</option>
              <option value="Study">📚 Study</option>
            </select>
          </div>
          <button className={style.button}><AiOutlinePlus size={30} /></button>
        </form>

        <div className={style.filterGroup}>
          {['All', 'High', 'Work', 'Study'].map((f) => (
            <button key={f} onClick={() => setFilter(f)} className='text-xs bg-white border px-3 py-1 rounded hover:bg-gray-200'>{f}</button>
          ))}
        </div>

        <ul>
          {filteredTodos.map((todo) => (
            <Todo key={todo.id} todo={todo} toggleComplete={toggleComplete} deleteTodo={deleteTodo} updateTodo={updateTodo} />
          ))}
        </ul>
        <p className={style.count}>{`Total: ${filteredTodos.length} Tasks`}</p>
      </div>
    </div>
  );
}

export default TodoPage;

