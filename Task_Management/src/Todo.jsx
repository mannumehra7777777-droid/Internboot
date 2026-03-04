import React, { useState } from 'react';
import { FaRegTrashAlt, FaEdit, FaCheck } from 'react-icons/fa';

const style = {
    li: `flex justify-between bg-slate-200 p-4 my-2 capitalize rounded-md`,
    liComplete: `flex justify-between bg-slate-400 p-4 my-2 capitalize rounded-md`,
    row: `flex items-center`,
    text: `ml-2 cursor-pointer`,
    textComplete: `ml-2 cursor-pointer line-through`,
    buttonGroup: `flex gap-3 items-center`
};

const Todo = ({ todo, toggleComplete, deleteTodo, updateTodo }) => {
    const [isEditing, setIsEditing] = useState(false);
    const [newText, setNewText] = useState(todo.text);

    const handleUpdate = () => {
        updateTodo(todo.id, newText);
        setIsEditing(false);
    };

    return (
        <li className={todo.completed ? style.liComplete : style.li}>
            <div className={style.row}>
                <input onChange={() => toggleComplete(todo)} type='checkbox' checked={todo.completed} />
                {isEditing ? (
                    <input 
                        className='ml-2 border p-1 text-black bg-white' 
                        value={newText} 
                        onChange={(e) => setNewText(e.target.value)} 
                    />
                ) : (
                    <p className={todo.completed ? style.textComplete : style.text}>
                        {todo.text} <span className="text-[10px] text-gray-600">({todo.priority})</span>
                    </p>
                )}
            </div>
            <div className={style.buttonGroup}>
                {isEditing ? (
                    <FaCheck onClick={handleUpdate} className='cursor-pointer text-green-600' />
                ) : (
                    <FaEdit onClick={() => setIsEditing(true)} className='cursor-pointer text-blue-600' />
                )}
                <FaRegTrashAlt onClick={() => deleteTodo(todo.id)} className='cursor-pointer text-red-600' />
            </div>
        </li>
    );
};

export default Todo;

